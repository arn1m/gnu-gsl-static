#!/bin/bash
set -e

# Destination for headers
DEST_DIR="$BUILD_DIR/gsl"

# Create destination directory
mkdir -p "$DEST_DIR"

# Find and copy headers (flat)
find "$LIB_DIR" -name "*.h" -type f | while read -r header; do
    cp "$header" "$DEST_DIR/"
done

echo "All headers copied flat to $DEST_DIR"
