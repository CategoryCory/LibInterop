import ctypes
from pathlib import Path
from structs import Complex


def cpp_class_lib_example(lib_name: str) -> None:
    '''
    This method demonstrates using ctypes to load a library written in C++.
    The library contains a class, as well as exposes some helper methods
    to facilitate using the methods inside the class. Note that this will
    require manual cleanup.

        Parameters:
            lib_name (str): The name of the shared library to load.
        
        Returns:
            None
    '''
    lib_dir: Path = Path(__file__).parent / 'lib'
    full_lib_path: Path = lib_dir / lib_name

    try:
        # Open the library
        lib: ctypes.CDLL = ctypes.CDLL(str(full_lib_path))

        # Define methods contained in library
        lib.CreateComplex.restype = ctypes.POINTER(Complex)
        lib.CreateComplex.argtypes = [ctypes.c_double, ctypes.c_double]
        lib.DestroyComplex.restype = None
        lib.DestroyComplex.argtypes = [ctypes.POINTER(Complex)]
        lib.GetPhaseRad.restype = ctypes.c_double
        lib.GetPhaseRad.argtypes = [ctypes.POINTER(Complex)]
        lib.GetPhaseDeg.restype = ctypes.c_double
        lib.GetPhaseDeg.argtypes = [ctypes.POINTER(Complex)]
        lib.GetMagnitude.restype = ctypes.c_double
        lib.GetMagnitude.argtypes = [ctypes.POINTER(Complex)]

        # Create instance of complex struct
        c_num = lib.CreateComplex(3, 4)

        # Call library functions
        phase_rad: float = lib.GetPhaseRad(c_num)
        phase_deg: float = lib.GetPhaseDeg(c_num)
        mag: float = lib.GetMagnitude(c_num)

        # Clean up
        lib.DestroyComplex(c_num)

        # Display results
        print(f'Library name: {lib_name}')
        print(f'Phase (rad): {phase_rad}')
        print(f'Phase (deg): {phase_deg}')
        print(f'Magnitude: {mag}')
        print()
    except OSError as e:
        print(f'Error opening specified file: {e}')
