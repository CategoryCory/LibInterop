# Library Interop Between Various Languages

The purpose of this repository is to demonstrate how to call libraries written in 
various compiled languages from other languages. One challenge that I've frequently
found is remembering the steps involved with this task, so I've created this repo
as a template and guide.

## The Library

Each of these libraries includes the same functionality, namely a few very simple
methods involving complex numbers:
- phase_deg: The phase in degrees
- phase_rad: The phase in radians
- magnitude: The magnitude of the complex number

For C, C++, and Rust, a `struct` is defined to represent complex numbers. The C++
directory also includes this functionality implemented as a class. The C# library
is implemented as a class.

## Setup

To set up this project, you will need to build the libraries. Follow the steps below.

- C: To build the C library, you will need [CMake](https://cmake.org/) installed. Change
  to the `libs/c` directory and follow these steps:
  - `cmake CMakeLists.txt`
  - `make`
- C++: Similarly to the C installation, you will need CMake. Change to the `libs/cpp` directory
  and follow the same commands listed in the C setup step.
- C#: To build the C# library, you will need the [.NET 8](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)
  SDK installed. Change to the `libs/cs` directory and follow these steps:
  - `dotnet build -c Release`
- Rust: To build the Rust library, you will need [Rust](https://www.rust-lang.org/tools/install) installed.
  Change to the `libs/rust/complex_rust` directory and follow these steps:
  - `cargo build --release`