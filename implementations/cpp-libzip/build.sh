#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )"

mkdir build
cd build
cmake ..
make
cd ..