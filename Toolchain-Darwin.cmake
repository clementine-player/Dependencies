include(CMakeForceCompiler)
# the name of the target operating system
SET(CMAKE_SYSTEM_NAME Darwin)

# which compilers to use for C and C++
cmake_force_c_compiler(i686-apple-darwin9-gcc-4.2.1 GNU)
cmake_force_cxx_compiler(i686-apple-darwin9-g++-4.2.1 GNU)

SET(CMAKE_OSX_SYSROOT /Developer/SDKs/MacOSX10.5.sdk)

# here is the target environment located
SET(CMAKE_FIND_ROOT_PATH  /home/john/mac ${CMAKE_OSX_SYSROOT} ${CMAKE_OSX_SYSROOT}/usr/bin)

include_directories(${CMAKE_OSX_SYSROOT}/usr/lib/gcc/i686-apple-darwin10/4.2.1/include)
include_directories(${CMAKE_OSX_SYSROOT}/usr/lib/i686-apple-darwin10/4.2.1)
link_directories(${CMAKE_OSX_SYSROOT}/usr/lib/i686-apple-darwin10/4.2.1)
link_directories(${CMAKE_OSX_SYSROOT}/usr/lib/gcc/i686-apple-darwin10/4.2.1)

# adjust the default behaviour of the FIND_XXX() commands:
# search headers and libraries in the target environment, search 
# programs in the host environment
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
