cmake_minimum_required(VERSION 3.10)
project(cpp-libzip)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(libzip REQUIRED)

add_executable(cpp-libzip main.cpp)
target_link_libraries(cpp-libzip PRIVATE libzip::zip)