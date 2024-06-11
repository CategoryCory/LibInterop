import ctypes
from pathlib import Path
from structs import Complex


def simple_lib_example(lib_name: str) -> None:
    '''
    This method demonstrates the usage of ctypes to load a simple shared library.
    Supported libaries are not object oriented.

        Parameters:
            lib_name (str): The name of the shared library to load.
        
        Returns:
            None
    '''
    lib_dir: Path = Path(__file__).parent.parent / 'lib'
    full_lib_path: Path = lib_dir / lib_name

    try:
        # Open the library
        lib: ctypes.CDLL = ctypes.CDLL(str(full_lib_path))

        # Define methods contained in library
        lib.phase_rad.restype = ctypes.c_double
        lib.phase_rad.argtypes = [ctypes.POINTER(Complex)]
        lib.phase_deg.restype = ctypes.c_double
        lib.phase_deg.argtypes = [ctypes.POINTER(Complex)]
        lib.magnitude.restype = ctypes.c_double
        lib.magnitude.argtypes = [ctypes.POINTER(Complex)]

        # Create instance of complex struct
        c_num: Complex = Complex(3, 4)

        # Call library functions
        phase_rad: float = lib.phase_rad(c_num)
        phase_deg: float = lib.phase_deg(c_num)
        mag: float = lib.magnitude(c_num)

        # Display results
        print(f'Library name: {lib_name}')
        print(f'Phase (rad): {phase_rad}')
        print(f'Phase (deg): {phase_deg}')
        print(f'Magnitude: {mag}')
        print()
    except OSError as e:
        print(f'Error opening specified file: {e}')
