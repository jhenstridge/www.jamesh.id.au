/*    Inverse Julia Set drawing Applet
 *  Copyright (C) 1996, James Henstridge <james@daa.com.au>
 *
 *  This Applet may be freely redistributed, provided that this source code
 *  is also distributed, intact,  with the applet.  This code may also be
 *  used to create other applets, provided credit is given to the
 *  original author (me).
 *
 *  The applet can take the following parameters from the HTML doc:
 *      depth             -- specifies number of times each pixel can be
 *                           overwritten.
 *      fgcolor, fgcolour -- specifies the foreground colour to use
 *      bgcolor, bgcolour -- specifies the background colour to use
 *      c_x, c_y          -- specifies value of c
 *
 */

import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.Event;
import java.awt.Color;
import java.applet.Applet;

public class inv_julia extends Applet implements Runnable {
  Thread drawThread = null;

  int h, w;
  int depth = 4;
  double t = 1.5, b = -1.5, l = -2.0, r = 2.0;
  boolean drawing = false;
  
//  double c_x = -0.74543, c_y = 0.11301;
  double c_x = -0.11, c_y = 0.6556999999999999;
  
  byte map[][];
    
  public void init()
  {
    String s;

    s = getParameter("depth");             // get dot depth
    if (s != null) depth = Integer.valueOf(s).intValue();

    s = getParameter("c_x");            // get Re(c)
    if (s != null) c_x = Double.valueOf(s).doubleValue();
    s = getParameter("c_y");             // get Im(c)
    if (s != null) c_y = Double.valueOf(s).intValue();

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
  
  public void stop()
  {
    drawThread = null;
//    g = null;
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
  
  public boolean mouseMove(Event e, int x, int y) {
    double x1, y1;
    
    x1 = (double)x / w * (r - l) + l;
    y1 = (double)y / h * (b - t) + t;
                    
    showStatus("(" + x1 + ", " + y1 + ")");
    return false;
  }
  
  public boolean mouseUp(Event e, int x, int y) {
    if (!drawing) {
      c_x = (double)x / w * (r - l) + l;
      c_y = (double)y / h * (b - t) + t;
      repaint();
      return true;
    } else
      return false;
  }
  
  int transX(double x)
  {
    return (int)((double)(x - l) / (r - l) * w);
  }
  
  int transY(double y)
  {
    return (int)((double)(y - t) / (b - t) * h);
  }
  
  Graphics g;
  
  public void paint (Graphics g)
  {
    this.g = g.create();
    drawThread = new Thread(this, "Draw it");
    drawThread.start();
  }
  
  public void run()
  {
    Rectangle rect = bounds();
    
    drawing = true;
    h = rect.height; w = rect.width;
    map = new byte[w][h];
    
    plot(1.0, 1.0);
    
    map = null;
    
    showStatus("Inverse Julia Set Applet Copyright (C) 1996, James Henstridge");
    drawing = false;
  }
  
  void plot(double x, double y) {
    double r, newx, newy;
    int sgn;
    int xtmp = transX(x), ytmp = transY(y);

    map[xtmp][ytmp]++;
    g.drawLine(xtmp, ytmp, xtmp, ytmp);
    drawThread.yield();
  
    if (map[xtmp][ytmp] < depth) {
      x -= c_x; y -= c_y;
      r = Math.sqrt(x*x + y*y);
      sgn = (y>0)?1:(y<0)?-1:0;
      newx = Math.sqrt((r + x) / 2);
      newy = Math.sqrt((r - x) / 2) * sgn;
      
      plot(newx, newy);
      plot(-newx, -newy);
    }
  }

}
