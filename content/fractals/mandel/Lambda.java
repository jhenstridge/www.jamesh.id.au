public class Lambda extends Mandel {
  Cmplx one = new Cmplx(1.0, 0.0);
  
  public Cmplx initz()
  {
    return new Cmplx(0.5, 0.0);
  }
  
  public Cmplx transform(Cmplx z, Cmplx c)
  {
    return new Cmplx(1.0, 0.0).subtr(z).mult(z).mult(c);
  }
}