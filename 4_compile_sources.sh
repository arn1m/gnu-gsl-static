#!/bin/bash
set -e

# Variables
CC="arm-none-eabi-gcc"
CFLAGS="-g -Og -mcpu=cortex-a9 -mfpu=vfpv3 -mfloat-abi=hard"
INCLUDES="-I$BUILD_DIR -I$BUILD_DIR/gsl"
SRC_LIST="$BUILD_DIR/c_sources.txt"
OBJ_DIR="$BUILD_DIR/objs"

mkdir -p "$OBJ_DIR"

if [[ ! -f "$SRC_LIST" ]]; then
    echo "Source list $SRC_LIST not found!"
    exit 1
fi

while read -r src; do
    src="${src%%$'\r'}"  # Remove CR if present
    [[ -z "$src" ]] && continue

    # Make path relative to LIB_DIR
    rel_path="$(realpath --relative-to="$LIB_DIR" "$src")"

    # Replace any / or \ with _
    obj_name="${rel_path//[\/\\]/_}"
    obj_name="${obj_name%.c}.o"
    obj="$OBJ_DIR/$obj_name"

    echo "Compiling $src -> $obj"
    $CC $CFLAGS $INCLUDES -c "$src" -o "$obj"
done < "$SRC_LIST"

echo "Compilation finished. Object files are in $OBJ_DIR"
