/*    Popcorn fractal drawing Applet
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
 *      dots              -- specifies how many dots to draw for each starting
 *                           point.
 *      fgcolor, fgcolour -- specifies the foreground colour to use
 *      bgcolor, bgcolour -- specifies the background colour to use
 *      resolution        -- specifies the resolution of the starting points.
 *
 */

import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.Event;
import java.awt.Color;
import java.applet.Applet;

public class popcorn extends Applet implements Runnable {
  Thread drawThread = null;

  int h, w;
  int dots = 50;
  double t = 1.5, b = -1.5, l = -2.0, r = 2.0;
  int res = 10;
    
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
    s = getParameter("dots");             // get # dots to draw
    if (s != null) dots = Integer.valueOf(s).intValue();
    s = getParameter("resolution");       // get resolution
    if (s != null) res = Integer.valueOf(s).intValue();

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
    return x - 0.05 * Math.sin(y + Math.tan(3 * y));
  }
  
  public double newY(double x, double y)
  {
    return y - 0.05 * Math.sin(x + Math.tan(3 * x));
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
    
    for (j = 0; j <= h; j += res)
      for (i = 0; i <= w; i += res) {
        x = (double)i / w * (r - l) + l;
        y = (double)j / h * (b - t) + t;
        for (k = 0; k < dots; k++) {
          xnew = newX(x, y);
          ynew = newY(x, y);
          x = xnew; y = ynew;
          gcont.drawLine(transX(x), transY(y), transX(x), transY(y));
        }
        drawThread.yield();
      }
    showStatus("Popcorn Fractal Applet Copyright (C) 1996, James Henstridge");
  }

}
