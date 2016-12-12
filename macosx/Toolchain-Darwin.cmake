include(CMakeForceCompiler)
# the name of the target operating system
SET(CMAKE_SYSTEM_NAME Darwin)

# which compilers to use for C and C++
cmake_force_c_compiler(x86_64-apple-darwin-clang GNU)
cmake_force_cxx_compiler(x86_64-apple-darwin-clang++ GNU)

SET(CMAKE_OSX_SYSROOT /Developer/SDKs/MacOSX10.10.sdk)

# here is the target environment located
SET(CMAKE_FIND_ROOT_PATH ${CMAKE_OSX_SYSROOT} ${CMAKE_OSX_SYSROOT}/usr/bin)

# adjust the default behaviour of the FIND_XXX() commands:
# search headers and libraries in the target environment, search 
# programs in the host environment
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
