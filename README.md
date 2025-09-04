# GNU GSL Static
Manual build for GNU GSL (https://www.gnu.org/software/gsl/) as static library withouth using the included `autotools` workflow, which is helpful, e.g., for cross-compilation of the library.

Notes:
 - Handle with care, no warranty is given in any form.
 - The provided workflow is generated with ChatGPT and adapted to the author's needs.
 
## Workflow (last tested on 2025-09-03)
Environment:
 - Windows 11
 - cygwin (https://www.cygwin.com/) with 
    - `make`
    - `libtool`
    - `pkg-config` (not sure if needed)
- AMD Vitis Classic 2023.2, which brings the `arm-none-eabi` toolchain for bare-metal development on Zynq7000

Steps (adapt header of scripts to your needs):
 - `. 0_environment.sh`: sets up often needed environment variables)
 - `./1_run_configure.sh`: runs `./configure` in GSL directory which produces missing headers based on (cross-)compilers abilities
 - `./2_headers.sh`: collects all header files
 - `python 3_get_sources.py`: goes through GSL subdirectories and collects all relevant C files based on `Makefile.am` information
 - `./4_compile_sources.sg`: compiles previously determined C files
 - `./5_pack.sh`: packs object files into one archive `libgslfull.a` (which also includes CBLAS, but that could be changed)
 - `python 6_check_undefined.py`: checks the resulting library for undefined symbols (this should only list runtime functions and functions from `libm`)
