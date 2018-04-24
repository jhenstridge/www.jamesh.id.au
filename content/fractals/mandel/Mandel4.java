public class Mandel4 extends Mandel {
  public Cmplx transform(Cmplx z, Cmplx c)
  {
    return new Cmplx().sqr(z).sqr().add(c);
  }
}