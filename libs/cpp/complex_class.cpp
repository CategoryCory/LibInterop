#ifdef _WIN32
    #define EXPORT              __declspec(dllexport)
    #define CALLING_CONVENTION  __stdcall
#else
    #define EXPORT              __attribute__((visibility("default")))
    #define CALLING_CONVENTION
#endif

#include <cmath>
#include "complex_class.h"

ComplexCpp::ComplexCpp(double re, double im) : real(re), imag(im) { }

double ComplexCpp::phase_rad() const
{
    return atan2(imag, real);
}

double ComplexCpp::phase_deg() const
{
    return phase_rad() * 180.0 / M_PI;
}

double ComplexCpp::magnitude() const
{
    return sqrt(pow(real, 2) + pow(imag, 2));
}

extern "C"
{
    EXPORT ComplexCpp* CALLING_CONVENTION CreateComplex(double re, double im)
    {
        return new ComplexCpp(re, im);
    }

    EXPORT void CALLING_CONVENTION DestroyComplex(ComplexCpp* c)
    {
        delete c;
    }

    EXPORT double CALLING_CONVENTION GetPhaseRad(const ComplexCpp* c) 
    {
        return c->phase_rad();
    }

    EXPORT double CALLING_CONVENTION GetPhaseDeg(const ComplexCpp* c) 
    {
        return c->phase_deg();
    }

    EXPORT double CALLING_CONVENTION GetMagnitude(const ComplexCpp* c) 
    {
        return c->magnitude();
    }
}
