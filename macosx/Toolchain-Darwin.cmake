# the name of the target operating system
set(CMAKE_SYSTEM_NAME Darwin)

# which compilers to use for C and C++
set(CMAKE_C_COMPILER x86_64-apple-darwin-clang)
set(CMAKE_CXX_COMPILER x86_64-apple-darwin-clang++)

set(CMAKE_OSX_SYSROOT /Developer/SDKs/MacOSX10.10.sdk)

# here is the target environment located
set(CMAKE_FIND_ROOT_PATH /target ${CMAKE_OSX_SYSROOT})

# adjust the default behaviour of the FIND_XXX() commands:
# search headers and libraries in the target environment, search 
# programs in the host environment
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
