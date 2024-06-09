use std::f64::consts::PI;

#[repr(C)]
pub struct Complex {
    real: f64,
    imag: f64,
}

#[no_mangle]
pub extern "C" fn phase_rad(c: *const Complex) -> f64 {
    if c.is_null() {
        return 0.0;
    }

    let complex_num = unsafe { &*c };

    f64::atan2(complex_num.imag, complex_num.real)
}

#[no_mangle]
pub extern "C" fn phase_deg(c: *const Complex) -> f64 {
    if c.is_null() {
        return 0.0;
    }

    phase_rad(c) * 180.0 / PI
}

#[no_mangle]
pub extern "C" fn magnitude(c: *const Complex) -> f64 {
    if c.is_null() {
        return 0.0;
    }

    let complex_num = unsafe { &*c };

    (f64::powi(complex_num.real, 2) + f64::powi(complex_num.imag, 2)).sqrt()
}
