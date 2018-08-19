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
import java.awt.BorderLayout;
import java.awt.Event;
import java.awt.Graphics;
import java.awt.Image;
 
class FracPanel extends Panel {
  Mandel parent;
  boolean capture = false, zoom = false;
  Cmplx tmp1, tmp2;
  Image image;
  Graphics boxDraw;
  
  public FracPanel(Mandel f) {
    parent = f;
    setBackground(Color.black);
  }

  public void updateImage() {
    image = createImage(parent);
    repaint();
  }
  
  public void paint(Graphics g) {
    //g.drawString("Please Wait.", 10, 10 + g.getFontMetrics().getHeight());
    g.drawImage(image, 0, 0, this);
    boxDraw = g.create();
    boxDraw.setXORMode(Color.white);
  }
  
  int tmpx1, tmpx2, tmpy1, tmpy2;
  
  public boolean mouseMove(Event e, int x, int y) {
    if (capture) {
      tmp1 = parent.translate(x, y);
      parent.showStatus("(" + String.valueOf(tmp1.real()) + 
                       ", " + String.valueOf(tmp1.imag()) +
                        ")");
      return true;
    } else
      return false;
  }      
  
  public boolean mouseDown(Event e, int x, int y) {
    if (capture) {
      tmp1 = parent.translate(x, y);
      if (zoom) {
        tmpx1 = tmpx2 = x; tmpy1 = tmpy2 = y;
        boxDraw.drawRect(tmpx1, tmpy1, tmpx2 - tmpx1, tmpy2 - tmpy1);
      }
      return true;
    } else
      return false;
  }
  
  public boolean mouseDrag(Event e, int x, int y) {
    if (capture) {
      tmp2 = parent.translate(x, y);
      if (zoom) {
        boxDraw.drawRect(tmpx1, tmpy1, tmpx2 - tmpx1, tmpy2 - tmpy1);
        tmpx2 = x; tmpy2 =y;
        boxDraw.drawRect(tmpx1, tmpy1, tmpx2 - tmpx1, tmpy2 - tmpy1);
        parent.showStatus("(" + String.valueOf(tmp1.real()) +
                         ", " + String.valueOf(tmp1.imag()) +
                        ")-(" + String.valueOf(tmp2.real()) +
                         ", " + String.valueOf(tmp2.imag()) +
                          ")");
      } else
        parent.showStatus("(" + String.valueOf(tmp2.real()) + 
                         ", " + String.valueOf(tmp2.imag()) +
                          ")");
      return true;
    } else
      return false;
  }
  
  public boolean mouseUp(Event e, int x, int y) {
    if (capture) {
      tmp2 = parent.translate(x, y);
      capture = false;
      if (zoom) {
        // boxDraw.drawRect(tmpx1, tmpy1, tmpx2 - tmpx1, tmpy2 - tmpy1);
        parent.tl = tmp1;
        parent.br = tmp2;
      } else {     //act == "Switch"
        parent.fType = "julia";
        parent.tl.set(-2.0, 1.5);
        parent.br.set(2.0, -1.5);
        parent.c = tmp2;
      }
      updateImage();
      return true;
    } else
      return false;
  }
  
}
