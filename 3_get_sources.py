#!/usr/bin/env python3
import os
import re

# Directories
LIB_DIR = os.environ.get("LIB_DIR", "./GSL_DIR")
BUILD_DIR = os.environ.get("BUILD_DIR", "./BUILD_DIR")

# Output file for C sources
output_file = os.path.join(BUILD_DIR, "c_sources.txt")

# List to store C files
c_files = []

# Regex to match *_la_SOURCES lines
sources_line_pattern = re.compile(r'^(\S+_la_SOURCES)\s*=\s*(.*)$', re.IGNORECASE)

# Walk through each subdirectory of LIB_DIR
for root, dirs, files in os.walk(LIB_DIR):
    if 'Makefile.am' in files:
        makefile_path = os.path.join(root, 'Makefile.am')
        with open(makefile_path, 'r') as f:
            continuation = ""
            for line in f:
                line = line.strip()
                # Handle line continuation with \
                if line.endswith('\\'):
                    continuation += line[:-1].strip() + " "
                    continue
                else:
                    line = continuation + line
                    continuation = ""

                match = sources_line_pattern.match(line)
                if match:
                    sources = match.group(2).split()
                    for src in sources:
                        # Only .c files, ignore files with 'test' in the name
                        if src.endswith('.c') and 'test' not in os.path.basename(src).lower():
                            full_path = os.path.join(root, src)
                            c_files.append(full_path)

# Save the list to the output file
with open(output_file, 'w') as f:
    for c in c_files:
        f.write(c + "\n")

print(f"Saved {len(c_files)} C files to {output_file}")
