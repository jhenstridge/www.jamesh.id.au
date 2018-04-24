public class Phoenix extends Mandel {
  Cmplx y;
  
  public Cmplx initz()
  {
    y = new Cmplx(0.0, 0.0);
    return new Cmplx(0.0, 0.0);
  }
  
  public Cmplx transform(Cmplx z, Cmplx c)
  {
    Cmplx oldy = y;
    
    y = z;
    return new Cmplx().sqr(z).add(c.real()).add(oldy.mult(c.imag()));
  }
}