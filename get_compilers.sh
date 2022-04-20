#!/bin/bash

# ARM NONE EABI 9-2019-q4-major
wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2019q4/gcc-arm-none-eabi-9-2019-q4-major-x86_64-linux.tar.bz2
tar -xvf gcc-arm-none-eabi-9-2019-q4-major-x86_64-linux.tar.bz2

# riscv-none-embed-gcc-xpack
wget https://github.com/xpack-dev-tools/riscv-none-embed-gcc-xpack/releases/download/v8.3.0-1.1/xpack-riscv-none-embed-gcc-8.3.0-1.1-linux-x64.tgz
tar -xvf xpack-riscv-none-embed-gcc-8.3.0-1.1-linux-x64.tgz

