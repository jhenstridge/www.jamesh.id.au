/*    Orbit fractal (Gingerbread man) drawing Applet
 *  Copyright (C) 1996, James Henstridge <james@daa.com.au>
 *
 *  This Applet may be freely redistributed, provided that this source code
 *  is also distributed, intact,  with the applet.  This code may also be
 *  used to create other applets, provided credit is given to the
 *  original author (me).
 *
 *  The applet can take the following parameters from the HTML doc:
 *      top, bottom, left and right
 *                        -- sets the bounds for the IFS coordinates used.
 *      dots              -- specifies how many dots to draw.
 *      fgcolor, fgcolour -- specifies the foreground colour to use
 *      bgcolor, bgcolour -- specifies the background colour to use
 *
 */

import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.Event;
import java.awt.Color;
import java.applet.Applet;

public class gingerbread extends Applet implements Runnable {
  Thread drawThread = null;

  int h, w;
  long dots = 10000;
  public double t = 8.5, b = -4.5, l = -4.5, r = 8.5;
  public double startx = -0.1, starty = 0.0;
    
  public void init()
  {
    String s;

    s = getParameter("top");              // get top bound
    if (s != null) t = Double.valueOf(s).doubleValue();
    s = getParameter("bottom");           // get bottom bound
    if (s != null) b = Double.valueOf(s).doubleValue();
    s = getParameter("left");             // get left bound
    if (s != null) l = Double.valueOf(s).doubleValue();
    s = getParameter("right");            // get right bound
    if (s != null) r = Double.valueOf(s).doubleValue();
    
    s = getParameter("startx");           // get start x value
    if (s != null) startx = Double.valueOf(s).doubleValue();
    s = getParameter("starty");           // get start y value
    if (s != null) starty = Double.valueOf(s).doubleValue();
    
    s = getParameter("dots");             // get # dots to draw
    if (s != null) dots = Long.valueOf(s).longValue();

    s = getParameter("bgcolor");          // get background colour;
    if (s != null)
      setBackground(new Color(Integer.valueOf(s, 16).intValue()));
    s = getParameter("bgcolour");         // get background colour;
    if (s != null)
      setBackground(new Color(Integer.valueOf(s, 16).intValue()));

    s = getParameter("fgcolor");          // get foreground colour;
    if (s != null)
      setForeground(new Color(Integer.valueOf(s, 16).intValue()));
    s = getParameter("fgcolour");         // get foreground colour;
    if (s != null)
      setForeground(new Color(Integer.valueOf(s, 16).intValue()));
  }
  
  public double newX(double x, double y)
  {
    return 1 - y + Math.abs(x);
  }
  
  public double newY(double x, double y)
  {
    return x;
  }
  
  public void stop()
  {
    drawThread = null;
    gcont = null;
  }
  
  public boolean action(Event e)
  {
    switch (e.id) {
      case Event.WINDOW_DESTROY:
        System.exit(0);
        return true;
      default:
        return false;
    }
  }
  
  int transX(double x)
  {
    return (int)((double)(x - l) / (r - l) * w);
  }
  
  int transY(double y)
  {
    return (int)((double)(y - t) / (b - t) * h);
  }
  
  Graphics gcont;
  
  public void paint (Graphics g)
  {
    gcont = g.create();
    drawThread = new Thread(this, "Draw it");
    drawThread.start();
  }
  
  public void run()
  {
    Rectangle rect = bounds();
    double x, y, xnew, ynew;
    int i, j, k;
    
    h = rect.height; w = rect.width;
    x = startx;
    y = starty;
    for (k = 0; k < dots; k++) {
      xnew = newX(x, y);
      ynew = newY(x, y);
      x = xnew; y = ynew;
      gcont.drawLine(transX(x), transY(y), transX(x), transY(y));
      if (k % 5 == 0) drawThread.yield();
    }
    showStatus("Orbit Fractal Applet Copyright (C) 1996, James Henstridge");
  }

}
