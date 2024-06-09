namespace ComplexCS;

class ComplexCS
{
    private double _real;
    private double _imag;

    public ComplexCS(double re, double im)
    {
        _real = re;
        _imag = im;
    }

    public double Real 
    {
        get => _real;
        set => _real = value;
    }

    public double Imag 
    {
        get => _imag;
        set => _imag = value;
    }

    public double PhaseRad()
    {
        return Math.Atan2(_imag, _real);
    }

    public double PhaseDeg()
    {
        return PhaseRad() * 180.0 / Math.PI;
    }

    public double Magnitude()
    {
        return Math.Sqrt(Math.Pow(_real, 2) + Math.Pow(_imag, 2));
    }
}