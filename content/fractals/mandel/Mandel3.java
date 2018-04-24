public class Mandel3 extends Mandel {
  public Cmplx transform(Cmplx z, Cmplx c)
  {
    return new Cmplx().cube(z).add(c);
  }
}