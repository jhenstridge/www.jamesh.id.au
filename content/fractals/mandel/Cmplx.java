final class Cmplx {
  double r, i;
  
  public Cmplx ()                        { r = 0.0; i = 0.0; }
  public Cmplx (double x, double y)      { r = x;   i = y;   }
  
  public void set (double x, double y)   { r = x;   i = y;   }
  public double real ()                  { return r; }
  public double imag ()                  { return i; }  
  public double modsq ()                 { return r * r + i * i; }
  
  public Cmplx add (Cmplx p)     { r += p.real(); i += p.imag(); return this; }
  public Cmplx add (double p)    { r += p; return this; }
  public Cmplx add (int p)       { r += p; return this; }
  public Cmplx subtr (Cmplx p)   { r -= p.real(); i -= p.imag(); return this; }
  public Cmplx subtr (double p)  { r -= p; return this; }
  public Cmplx subtr (int p)     { r -= p; return this; }
  public Cmplx mult (double p)   { r *= p; i *= p; return this; }
  public Cmplx mult (int p)      { r *= p; i *= p; return this; }
  public Cmplx mult (Cmplx p) {
    r =  r * p.real() - i * p.imag();
    i =  i * p.real() + r * p.imag();
    return this;
  }
  public Cmplx divid (Cmplx p) {
    double tmp = p.modsq();
    r = (r * p.real() + i * p.imag()) / tmp;
    i = (i * p.real() - r * p.imag()) / tmp;
    return this;
  }
  
  public Cmplx sqr() {
    set(r * r - i * i, 2 * r * i);
    return this;
  }
  
  public Cmplx cube() {
    double r2 = r*r, i2 = i*i;
    
    set(r * (r2 - 3 * i2), i * (3 * r2 - i2));
    return this;
  }

  public Cmplx exp() {
    double e1 = Math.exp(r);
    
    set(e1 * Math.cos(i), e1 * Math.sin(i));
    return this;
  }
  
  public Cmplx sin() {
    double e1 = Math.exp(i), e2 = 1/e1;
    
    set(Math.sin(r) * (e1 + e2) / 2, Math.cos(r) * (e1 - e2) / 2);
    return this;
  }

  public Cmplx cos() {
    double e1 = Math.exp(i), e2 = 1/e1;
    
    set(Math.cos(r) * (e1 + e2) / 2, -Math.sin(r) * (e1 - e2) / 2);
    return this;
  }

  public Cmplx add (Cmplx p1, Cmplx p2)   { r = p1.real() + p2.real();
                                           i = p1.imag() + p2.imag();
                                           return this; }
  public Cmplx subtr (Cmplx p1, Cmplx p2) { r = p1.real() - p2.real();
                                           i = p1.imag() - p2.imag();
                                           return this; }
  public Cmplx mult (Cmplx p1, Cmplx p2) {
    r =  p1.real() * p2.real() - p1.imag() * p2.imag();
    i =  p1.imag() * p2.real() + p1.real() * p2.imag();
    return this;
  }
  public Cmplx divid (Cmplx p1, Cmplx p2) {
    double tmp = p2.modsq();
    r = (p1.real() * p2.real() + p1.imag() * p2.imag()) / tmp;
    i = (p1.imag() * p2.real() - p1.real() * p2.imag()) / tmp;
    return this;
  }

  public Cmplx sqr(Cmplx p) {
    r = p.real() * p.real() - p.imag() * p.imag();
    i = 2 * p.real() * p.imag();
    return this;
  }
  public Cmplx cube(Cmplx p) {
    double r2 = p.real() * p.real(), i2 = p.imag() * p.imag();
    
    set(p.real() * (r2 - 3 * i2), p.imag() * (3 * r2 - i2));
    return this;
  }

  public Cmplx exp(Cmplx p) {
    double e1 = Math.exp(p.real());
    
    set(e1 * Math.cos(p.imag()), e1 * Math.sin(p.imag()));
    return this;
  }
  
  public Cmplx sin(Cmplx p) {
    double e1 = Math.exp(p.imag()), e2 = 1/e1;
    
    set(Math.sin(p.real()) * (e1 + e2)/2, Math.cos(p.real()) * (e1 - e2)/2);
    return this;
  }

  public Cmplx cos(Cmplx p) {
    double e1 = Math.exp(p.imag()), e2 = 1/e1;
    
    set(Math.cos(p.real()) * (e1 + e2)/2, -Math.sin(p.real()) * (e1 - e2)/2);
    return this;
  }

}
