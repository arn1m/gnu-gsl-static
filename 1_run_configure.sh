#!/bin/bash
set -e

# set up and run ./configure to obtain missing header files
export CC=arm-none-eabi-gcc
export AR=arm-none-eabi-ar
export RANLIB=arm-none-eabi-ranlib

# important here: nosys.specs, so configure can compile and link a minimal executable
# (since bare-metal compiler does not provide C runtime for functions like exit(), malloc(), ...)
export CFLAGS="-mcpu=cortex-a9 -mfpu=vfpv3 -mfloat-abi=hard -specs=nosys.specs"

cd $LIB_DIR
./configure --host=arm-xilinx-eabi CFLAGS="$(echo $CFLAGS)"
