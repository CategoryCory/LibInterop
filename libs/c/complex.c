#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

typedef struct
{
    double real;
    double imag;
} Complex;

double phase_rad(const Complex* c)
{
    return atan2(c->imag, c->real);
}

double phase_deg(const Complex* c)
{
    return phase_rad(c) * 180.0 / M_PI;
}

double magnitude(const Complex* c)
{
    return sqrt(pow(c->real, 2) + pow(c->imag, 2));
}
