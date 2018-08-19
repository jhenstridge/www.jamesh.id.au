/*    IFS drawing Applet
 *  Copyright (C) 1996, James Henstridge <james@daa.com.au>
 *
 *  This Applet may be freely redistributed, provided that this source code
 *  is also distributed, intact,  with the applet.  This code may also be
 *  used to create other applets, provided credit is given to the
 *  original author (me).
 *
 *  This Applet contains one class which extends the Applet class.
 *    It overides the following methods:
 *      init(), action(Event, Object) and paint(Graphics)
 *    It adds the following methods:
 *      setDemoMap()  -- sets up the default Sierpinski triangle
 *      transX()      -- translates IFS coordinates to screen coordinates
 *      transY()      --        "           "         "            "
 *
 *  The applet can take the following parameters from the HTML doc:
 *      top, bottom, left and right
 *                        -- sets the bounds for the IFS coordinates used.
 *      lines             -- the number of lines of IFS code
 *      line#             -- sets line # of the IFS code.  (first line = 0)
 *      dots              -- specifies how many dots to draw to make fractal.
 *      fgcolor, fgcolour -- specifies the foreground colour to use
 *      bgcolor, bgcolour -- specifies the background colour to use
 *
 *  The lines of IFS code consist of 7 space delimited numbers.  These
 *  numbers are in the same order as found in Fractint's 2D IFS files, so
 *  for more information on the format, look at Fractint's documentation.
 *
 */

import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.Event;
import java.awt.Color;
import java.applet.Applet;
import java.util.StringTokenizer;

public class ifs extends Applet implements Runnable {
  public final static int maxLines = 10;
  public int lines = 0;
  public double map[][];
  
  Thread drawThread = null;

  int h, w;
  long dots = 10000;
  double t = 1.0, b = -1.0, l = -1.0, r = 1.0;
    
  public void init()
  {
    String s;

    s =  getParameter("lines");  // get fractal information
    if (s == null)
      setDemoMap();
    else {
      int i = Integer.valueOf(s).intValue(), j;
      StringTokenizer st;
      
      map = new double[i][7];
      for (lines = 0; lines < i; lines++) {
        s = getParameter("line" + String.valueOf(lines));
        if (s == null)
          for (j = 0; j <7; j++)
            map[lines][j] = 0.0;
        else {
          st = new StringTokenizer(s);
          for (j = 0; (j < 7) && st.hasMoreTokens(); j++)
            map[lines][j] = Double.valueOf(st.nextToken()).doubleValue();
        }
      }
    }

    s = getParameter("top");              // get top bound
    if (s != null) t = Double.valueOf(s).doubleValue();
    s = getParameter("bottom");           // get bottom bound
    if (s != null) b = Double.valueOf(s).doubleValue();
    s = getParameter("left");             // get left bound
    if (s != null) l = Double.valueOf(s).doubleValue();
    s = getParameter("right");            // get right bound
    if (s != null) r = Double.valueOf(s).doubleValue();
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
  
  public void stop()
  {
    drawThread = null;
    gcont = null;
  }
  
  void setDemoMap()
  {
    map = new double[3][7];
    lines = 3;
    map[0][0] =  0.5;   map[1][0] =  0.5;   map[2][0] =  0.5;
    map[0][1] =  0.0;   map[1][1] =  0.0;   map[2][1] =  0.0;
    map[0][2] =  0.0;   map[1][2] =  0.0;   map[2][2] =  0.0;
    map[0][3] =  0.5;   map[1][3] =  0.5;   map[2][3] =  0.5;
    map[0][4] = -0.5;   map[1][4] = -0.5;   map[2][4] =  0.5;
    map[0][5] =  0.5;   map[1][5] = -0.5;   map[2][5] = -0.5;
    map[0][6] =  0.333; map[1][6] =  0.333; map[2][6] =  0.334;
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
    Rectangle r = bounds();
    long i;
    int x = r.width / 2, y = r.height / 2;
  
    double u = 0.0, v = 0.0, newu, newv, sum = 0.0, rnd;
    int l = 0;

    h = r.height; w = r.width;

    for (i = 1; i <= dots; i++) {
      rnd = Math.random();
      l = 0; sum = map[l][6];
      while ( (rnd > sum) && (l < lines) ) {
        l++;
        sum += map[l][6];
      }
      if (l < lines) {
        newu = map[l][0] * u + map[l][1] * v;
        newv = map[l][2] * u + map[l][3] * v;
        u = newu + map[l][4];
        v = newv + map[l][5];
      }
      
      gcont.drawLine(transX(u), transY(v), transX(u), transY(v));
      if (i % 5 == 0) drawThread.yield();
    }
    showStatus("IFS Applet Copyright (C) 1996, James Henstridge ");
    gcont = null;
  }

}
