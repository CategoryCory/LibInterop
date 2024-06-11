#ifdef _WIN32
    #define EXPORT              __declspec(dllexport)
    #define CALLING_CONVENTION  __stdcall
#else
    #define EXPORT              __attribute__((visibility("default")))
    #define CALLING_CONVENTION
#endif

#include <cmath>

extern "C"
{
    typedef struct
    {
        double real;
        double imag;
    } Complex;

    EXPORT double CALLING_CONVENTION phase_rad(const Complex* c)
    {
        return atan2(c->imag, c->real);
    }

    EXPORT double CALLING_CONVENTION phase_deg(const Complex* c)
    {
        return phase_rad(c) * 180.0 / M_PI;
    }
    
    EXPORT double CALLING_CONVENTION magnitude(const Complex* c)
    {
        return sqrt(pow(c->real, 2) + pow(c->imag, 2));
    }
}