/*    Complex Number Fractal drawing  Applet
 *  Copyright (C) 1996, 1997, James Henstridge <james@daa.com.au>
 *
 *  This Applet may be freely redistributed, provided that this source code
 *  is also distributed, intact,  with the applet.  This code may also be
 *  used to create other applets, provided credit is given to the
 *  original author (me).
 *
 *  This applet uses my Complex number class stored in Cmplx.java, and
 *  consists of 3 other classes: Mandel, Controls and FracPanel.  The
 *  applet can take a number of different parameters, including 'top',
 *  'bottom, 'left' and 'right', which specify the original window on 
 *  the complex plane.  The 'type' parameter changes between Mandelbrot
 *  and Julia Set modes, and the parameters 'creal' and 'cimag' specify
 *  the value of c for the Julia Sets.  The 'resolution' parameter sets
 *  the resolution, and 'maxiter' sets the maximum number of iterations.
 *
 *  Different fractals can be created by extending the Mandel class, and
 *  overloading the transform method with your new function, as can be seen
 *  Mandel3.java.  These applets will also have all the functionality (zooming,
 *  lowres modes, Julia sets and the parameters.
 */

import java.awt.Panel;
import java.awt.Color;
import java.awt.Button;
import java.awt.Choice;
import java.awt.Event;
import java.awt.Graphics;
import java.awt.Rectangle;
 
class Controls extends Panel {
  Mandel ap;
  int newStep;
  
  public Controls(Mandel ap) {
    Choice ch = new Choice();
    int i;
  
    this.ap = ap;
    newStep = ap.step;
    
    ch.addItem("1");
    ch.addItem("2");
    ch.addItem("5");
    ch.addItem("10");
    ch.select(String.valueOf(ap.step));
    add(ch);
    add(new Button("Redraw"));

    add(new Button("Zoom In"));
    add(new Button("Switch (M<->J)"));
  }
  
  public void paint(Graphics g) {
    Rectangle r = bounds();
    
    g.setColor(Color.lightGray);
    g.draw3DRect(0, 0, r.width - 1, r.height - 1, true);
  }
  
  public boolean action(Event e, Object what) {
    String str;

    str = (String) what;
           // note: is a string is null, then the `equals'
           //       method always returns true
    if (str.equals("Zoom") || str.equals("Switch"))
      return true;  // every time I remove this, I get Thread dumps
    else if ((str != null) && (str.equals("1") || str.equals("2")
                            || str.equals("5") || str.equals("10"))) {
      newStep = Integer.valueOf(str).intValue();
      return true;
    } else if (e.target instanceof Button) {
      ap.step = newStep;
      if (((Button) e.target).getLabel().equals("Redraw")) {
        ap.message("Redraw");
      } else if (((Button) e.target).getLabel().equals("Zoom In")) {
        ap.message("Zoom");     // tell panel to zoom
      } else if (((Button) e.target).getLabel().equals("Switch (M<->J)")) {
        ap.message("Switch");   // tell panel to switch (M<->J)
      }
      return true;
    }
    return false;
  }
  
}

