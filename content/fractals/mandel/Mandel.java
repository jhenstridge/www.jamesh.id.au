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
 
import java.applet.Applet;
import java.awt.Color;
import java.awt.BorderLayout;
import java.awt.Event;
import java.awt.Rectangle;
import java.awt.Image;
import java.awt.image.ImageProducer;
import java.awt.image.ImageConsumer;
import java.awt.image.ColorModel;
import java.awt.image.DirectColorModel;

public class Mandel extends Applet implements ImageProducer, Runnable {
  protected int maxIter = 40;
  public int step = 5;
  public String fType = "mandel";
  public Cmplx c = null;
  public Cmplx tl = new Cmplx(-2.0,1.5), br = new Cmplx(2.0,-1.5);
  public FracPanel fracpanel;

  Thread drawThread;
  boolean killThread = false;
  ColorModel cm = new DirectColorModel(8, 1+2, 4+8+16, 32+64+128);
  ImageConsumer ic;
  Rectangle imgSize;

  public void init() {
    String s;
    double r = 0.0, i = 0.0;
    s = getParameter("resolution");    // get resolution parameter
    if (s != null) step = Integer.valueOf(s).intValue();
    
    s = getParameter("maxiter");       // get Maximum Iteration Value
    if (s != null) maxIter = Integer.valueOf(s).intValue();
    
    s = getParameter("type");          // get type (mandel/julia)
    if ((s != null) && (s.equals("mandel") || s.equals("julia")))
      fType = s;
      
    s = getParameter("creal");           // get value of `c'
    if (s != null) r = Double.valueOf(s).doubleValue();
    s = getParameter("cimag");
    if (s != null) i = Double.valueOf(s).doubleValue();
    
    c = new Cmplx(r, i);
    
    fracpanel = new FracPanel(this);
    Controls ctrl = new Controls(this);

    fracpanel.updateImage();

    setLayout(new BorderLayout());
    add("Center", fracpanel);
    
    s = getParameter("nocontrols");
    if ((s == null) || !(s.equals("true")))
      add("South", ctrl);

    s = getParameter("left");           // get value of `tl'
    if (s != null) tl.set(Double.valueOf(s).doubleValue(), tl.imag());
    s = getParameter("top");
    if (s != null) tl.set(tl.real(), Double.valueOf(s).doubleValue());
    
    s = getParameter("right");           // get value of `br'
    if (s != null) br.set(Double.valueOf(s).doubleValue(), br.imag());
    s = getParameter("bottom");
    if (s != null) br.set(br.real(), Double.valueOf(s).doubleValue());
    
  }
  
  public boolean action(Event e) {
    switch (e.id)
    {
      case Event.WINDOW_DESTROY:
        System.exit(0);
        return true;
      default:
        return false;
    }
  }
  
  public Cmplx transform(Cmplx z, Cmplx c) {
    return new Cmplx().sqr(z).add(c);
  }
  
  public Cmplx initz() {
    return new Cmplx(0.0, 0.0);
  }
  
  public int pixelColour(Cmplx pixel) {
    Cmplx z = null;
    int iter = 0;
    
    if (fType.equals("mandel")) {
      z = initz();
      do {
        iter++;
        z = transform(z, pixel);
      } while ( (z.modsq() <= 4.0) && (iter <= maxIter) );
    } else if (fType.equals("julia")) {
      initz();
      z = pixel;
      do {
        iter++;
        z = transform(z, c);
      } while ( (z.modsq() <= 4.0) && (iter <= maxIter) );
    } else iter = 1;
    if (iter > maxIter)
      return -1;
    else
      return iter;
  }

  public synchronized void addConsumer(ImageConsumer ic) {
    this.ic = ic;
  }

  public synchronized boolean isConsumer(ImageConsumer ic) {
    return (ic == this.ic);
  }

  public synchronized void removeConsumer(ImageConsumer ic) {
    if (this.ic == ic) {
      this.ic = null;
    }
  }

  public void startProduction(ImageConsumer ic) {
    imgSize = fracpanel.bounds();
    this.ic = ic;
    this.ic.setDimensions(imgSize.width, imgSize.height);
    this.ic.setHints(ImageConsumer.TOPDOWNLEFTRIGHT |
                     ImageConsumer.COMPLETESCANLINES |
                     ImageConsumer.SINGLEFRAME);
    drawThread = new Thread(this, "Draw Fractal");
    killThread = false;
    drawThread.start();
  }

  public void requestTopDownLeftRightResend(ImageConsumer ic) {
    // Not needed.  The data is always in TDLR format.
  }

  public Cmplx translate(int x, int y) {
    return new Cmplx(
      tl.real() + (double)x / imgSize.width * (br.real() - tl.real()),
      tl.imag() + (double)y / imgSize.height * (br.imag() - tl.imag()));
  }

  public void run() {
    int scanLine[] = new int[imgSize.width];
    int i, j, clr, num;
    Cmplx pixel, z;

    for (j=0; j < imgSize.height; j+= step) {
      for (i=0; i < imgSize.width; i+= step) {
        pixel = translate(i, j);
        clr = pixelColour(pixel);
        if (clr == -1)
          for (num=0; num < step && i+num < imgSize.width; num++)
            scanLine[i + num] = 0;
        else
          for (num=0; num < step && i+num < imgSize.width; num++)
            scanLine[i + num] = (clr - 1) % 255 + 1;
        if (i%5 == 0) {
          drawThread.yield();
          if (killThread) {
            killThread = false;
            ic.imageComplete(ImageConsumer.STATICIMAGEDONE);
            return;
          }
        }
      }
      for (num=0; num < step && j+num < imgSize.height; num++)
        ic.setPixels(0, j+num, imgSize.width, 1,
                     cm, scanLine, 0, imgSize.width);
    }
    showStatus("Complex Number Fractal Applet Copyright (C) 1996, James Henstridge");
    ic.imageComplete(ImageConsumer.STATICIMAGEDONE);
  }

  public void message(String act) {
    killThread = true;
    while (drawThread.isAlive() && drawThread != null)
      Thread.currentThread().yield();
    if (drawThread != null) drawThread.stop();
    killThread = false;
    if (act.equals("Zoom")) {
      fracpanel.capture = true;
      fracpanel.zoom = true;
    } else if (act.equals("Redraw"))
      fracpanel.updateImage();
    else {
      if (fType.equals("mandel")) {
        fType = "julia";
        fracpanel.capture = true;
        fracpanel.zoom = false;
      } else {
        fType = "mandel";
        tl.set(-2.0, 1.5);
        br.set(2.0, -1.5);
        fracpanel.updateImage();
      }
    }
  }
}

