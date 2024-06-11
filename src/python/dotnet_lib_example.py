import sys
from pathlib import Path


def dotnet_lib_example(lib_name: str) -> None:
    '''
    This method demonstrates loading a library written in C# and calling methods
    within.

        Parameters:
            lib_name (str): The name of the shared library to load.
        
        Returns:
            None
    '''
    lib_dir: Path = Path(__file__).parent / 'lib'
    full_lib_path: Path = lib_dir / lib_name

    # Verify files exist before continuing
    if not Path.exists(full_lib_path):
        raise OSError('The specified file could not be found.')

    # Set runtime info
    from pythonnet import load
    load('coreclr')

    # Import dotnet assemblies
    import clr
    import System

    sys.path.append(str(lib_dir))

    # Load assembly and verify that it loaded correctly
    try:
        clr.AddReference('ComplexCS')

        # Import the namespace from the library
        # TODO: Is there a way to parameterize this?
        from ComplexCS import ComplexCS

        # Create instance of class
        c_num = ComplexCS(3, 4)

        phase_rad: float = c_num.PhaseRad()
        phase_deg: float = c_num.PhaseDeg()
        mag: float = c_num.Magnitude()

        # Display results
        print(f'Library name: {lib_name}')
        print(f'Phase (rad): {phase_rad}')
        print(f'Phase (deg): {phase_deg}')
        print(f'Magnitude: {mag}')
        print()
    except System.IO.FileNotFoundException as ex:
        raise ImportError('Error loading assembly') from ex
