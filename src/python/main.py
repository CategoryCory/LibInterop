from simple_lib_example import simple_lib_example
from cpp_class_lib_example import cpp_class_lib_example
from dotnet_lib_example import dotnet_lib_example


def main() -> None:
    # Run demo for simple libs written in C, C++, and Rust
    simple_libs: list[str] = ['libcomplex_c.so', 'libcomplex_cpp.so', 'libcomplex_rust.so']
    for lib in simple_libs:
        simple_lib_example(lib)
    
    # Run demo for C++ lib with class
    cpp_class_lib_example('libcomplex_class_cpp.so')

    # Run demo for .NET lib
    try:
        dotnet_lib_example('ComplexCS.dll')
    except OSError as ose:
        print(f'An error occurred while loading library: {ose}')
    except ImportError as ime:
        print(f'An error occurred while loading the assembly: {ime}')

if __name__ == '__main__':
    main()
