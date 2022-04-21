#!/bin/bash

export AI_PROJECT_ROOT=`pwd`

# Handle ARM GCC
ARM_GCC_DIR=$AI_PROJECT_ROOT
ARM_GCC_DIR+="/"
ARM_GCC_DIR+="gcc-arm-none-eabi-9-2019-q4-major"

echo $PATH | grep -q -s "$ARM_GCC_DIR/bin"
if [ $? -eq 1 ] ; then
    PATH=$PATH:$ARM_GCC_DIR/bin
    export PATH
    ARMGCC_DIR=$ARM_GCC_DIR
    export ARMGCC_DIR
fi

# Handle RISCV GCC
RISCV_GCC_DIR=$AI_PROJECT_ROOT
RISCV_GCC_DIR+="/"
RISCV_GCC_DIR+="xPacks/riscv-none-embed-gcc/8.3.0-1.1"

echo $PATH | grep -q -s "$RISCV_GCC_DIR/bin"
if [ $? -eq 1 ] ; then
    PATH=$PATH:$RISCV_GCC_DIR/bin
    export PATH
    RISCVGCC_DIR=$RISCV_GCC_DIR
    export RISCVGCC_DIR
fi

export MAXIM_PATH="$AI_PROJECT_ROOT/ai8x-synthesis/sdk/"
