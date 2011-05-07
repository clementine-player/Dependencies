#!/bin/bash

path=$1

headers="aligned_storage archive assert bind call_traits checked_delete
        circular_buffer config cstdint current_function detail exception functional
        get_pointer implicit_cast integer is_placeholder iterator limits mem_fn
        memory_order mpl multi_index next_prior noncopyable operators
        preprocessor ref scoped_ptr serialization shared_ptr smart_ptr
        static_assert throw_exception tuple type type_traits utility version
        visit_each enable_shared_from_this scoped_array function"

if [ -z $path ]; then
  echo "Usage: $0 <path>"
  echo ""
  echo "Creates a package containing the useful parts of a Boost installation, eg:"
  echo "  $0 /usr/include"
  exit 1
fi

version=`grep "#define BOOST_LIB_VERSION" $path/boost/version.hpp | sed 's/^[^"]*//' | sed 's/"//g' | tr _ .`
dest=boost-$version

# Make the destination directory and create folders
rm -rf $dest
mkdir -vp $dest/include/boost

# Copy headers
for d in $headers; do
  cp -r $path/boost/$d* $dest/include/boost/
done

# Create the package
tar -cjf $dest.tar.bz2 $dest
rm -rf $dest
