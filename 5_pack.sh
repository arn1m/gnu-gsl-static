#!/bin/bash
set -e

AR=arm-none-eabi-ar

# pack all objects into one library
# (you could also only use a subset for specific tasks ...)
$AR rcs libgslfull.a $BUILD_DIR/objs/*.o
