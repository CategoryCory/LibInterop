from ctypes import c_double, Structure


class Complex(Structure):
    _fields_ = [('real', c_double),
                ('imag', c_double)]
