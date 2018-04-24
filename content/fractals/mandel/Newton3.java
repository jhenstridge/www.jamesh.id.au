public class Newton3 extends Mandel {

  final Cmplx one = new Cmplx(1.0, 0.0);

  public int pixelColour(Cmplx pixel)
  {
    Cmplx z, z3 = new Cmplx(), z2 = new Cmplx(),
          test = new Cmplx();
    int iter = 0;
    
    if (fType.equals("mandel")) {
      z = new Cmplx(pixel.real(), pixel.imag());
      do {
        iter++;
        z2.sqr(z); z2.mult(3);
        test.cube(z);
        z3.set(test.real(), test.imag()); z3.mult(2); z3.add(one);
        z.divid(z3, z2);
        test.subtr(one);
      } while ( (test.modsq() >= 0.04) && (iter <= maxIter) );
    } else if (fType.equals("julia")) {
      z = new Cmplx(pixel.real(), pixel.imag());
      do {
        iter++;
        z2.sqr(z); z2.mult(3);
        test.cube(z);
        z3.set(test.real(), test.imag()); z3.mult(2); z3.add(c);
        z.divid(z3, z2);
        test.subtr(c);
      } while ( (test.modsq() >= 0.04) && (iter <= maxIter) );
    } else iter = 1;
    if (iter > maxIter)
      return -1;
    else
      return iter;
  }

}
