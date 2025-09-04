#!/usr/bin/env python3
import os
import subprocess
import sys
import re

# Inputs
LIB_FILE = sys.argv[1] if len(sys.argv) > 1 else "libgslfull.a"
NM = "arm-none-eabi-nm"

if not os.path.isfile(LIB_FILE):
    print(f"Library {LIB_FILE} not found!")
    sys.exit(1)

# Run nm on the library
result = subprocess.run([NM, "-A", LIB_FILE], capture_output=True, text=True)
if result.returncode != 0:
    print(f"nm failed:\n{result.stderr}")
    sys.exit(1)

undefined_symbols = set()
defined_symbols = set()

# Parse output
# Example nm output: 
# file.o:00000000 T foo
# file.o:         U bar
pattern = re.compile(r"^(.*?):.*\s([A-Z])\s(\S+)$")

for line in result.stdout.splitlines():
    m = pattern.match(line.strip())
    if m:
        symbol_type = m.group(2)
        symbol_name = m.group(3)
        if symbol_type.upper() == "U":
            undefined_symbols.add(symbol_name)
        else:
            defined_symbols.add(symbol_name)

# Filter out undefined symbols that are actually defined in the library
true_undefined = sorted(undefined_symbols - defined_symbols)

print("Undefined symbols not defined in the library:")
for sym in true_undefined:
    print(sym)
