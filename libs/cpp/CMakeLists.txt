cmake_minimum_required(VERSION 3.22.1)
project(ComplexCpp)
add_library(complex_cpp SHARED complex.cpp)
add_library(complex_class_cpp SHARED complex_class.cpp complex_class.h)