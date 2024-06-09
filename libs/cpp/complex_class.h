class ComplexCpp
{
private:
    double real;
    double imag;
public:
    ComplexCpp(double re, double im);
    double phase_rad() const;
    double phase_deg() const;
    double magnitude() const;
};
