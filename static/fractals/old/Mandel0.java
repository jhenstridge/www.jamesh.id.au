/*    Mandelbrot Set Applet
 *  Copyright (C) 1996, James Henstridge <james@daa.com.au>
 *
 *  This Applet may be freely redistributed, provided that this source code
 *  is also distributed, intact,  with the applet.  This code may also be
 *  used to create other applets, provided credit is given to the
 *  original author (me).
 *
 *  Very simple, probably messy applet that draws a Mandelbrot Set, with
 *  no zoom, no Mandelbrot <-> Julia switching.  I would recommend my
 *  extended version (Mandel.java).
 */
 
import java.applet.Applet;
import java.awt.Color;
import java.awt.Event;
import java.awt.Graphics;
import java.awt.Rectangle;

public class Mandel0 extends Applet {
  int mset[][];
  Color clrs[];
  boolean calcdone, symetric;
  int step = 5;
  
  public void init()
  {
    String s;
    clrs = new Color[13];
    clrs[0] = Color.black;    clrs[1] = Color.blue;
    clrs[2] = Color.green;    clrs[3] = Color.red;
    clrs[4] = Color.cyan;     clrs[5] = Color.magenta;
    clrs[6] = Color.orange;   clrs[7] = Color.lightGray;
    clrs[8] = Color.gray;     clrs[9] = Color.darkGray;
    clrs[10] = Color.pink;    clrs[11] = Color.yellow;
    clrs[12] = Color.white;
    calcdone = false;
    symetric = false;
    s = getParameter("resolution");
    if (s != null) step = Integer.valueOf(s).intValue();
  }
  
  public void paint(Graphics g)
  {
    int i, j;
    
    if (!calcdone) {
      int ylim, iter;
      double initx, inity,  oldx, oldy,  newx, newy;
      mset = new int[bounds().width][bounds().height];

      if (symetric) ylim = bounds().height / 2; else ylim = bounds().height;
      for (j=0; j < ylim; j+=step) {
        for (i=0; i < bounds().width; i+=step) {
          initx = (double)i / bounds().width * 4.0 - 2.5;
          inity = 1.5 - (double)j / bounds().height * 3.0;
          newx = newy = oldx = oldy = 0.0;
          iter = 0;
          do {
            iter++;
            newx = (oldx - oldy)*(oldx + oldy) + initx;
            newy = 2 * oldx * oldy + inity;
            oldx = newx; oldy = newy; 
          } while ((newx*newx + newy*newy <= 4.0) && (iter <= 12));
          if (iter > 12) iter = 0;
          mset[i][j] = iter;
          g.setColor(clrs[mset[i][j]]);
          g.fillRect(i, j, step, step);
          if (symetric) {
            mset[bounds().height - i][j] = iter;
            g.fillRect(i, j, i+1, j);
          }
        }
      }
      calcdone = true;
    } else {
      for (j=0; j < size().height; j+=step)
        for (i=0; i < size().width; i+=step) {
          g.setColor(clrs[mset[i][j]]);
          g.fillRect(i, j, step, step);
        }
    }
    showStatus("Mandelbrot Applet Copyright (C) 1996, James Henstridge");
  }
  
}
