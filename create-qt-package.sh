#!/bin/bash

path=$1
version=$2
dest=qt-$version

modules="QtCore QtGui QtNetwork QtSql QtSvg QtTest QtWebKit QtXml QtOpenGL"
src="3rdparty corelib gui network opengl plugins sql xml testlib"
imageformats="qgif qjpeg qico qsvg"
sqldrivers="qsqlite"
extradlls="libgcc_s_dw2-1.dll mingwm10.dll"

if [ -z $path -o -z $version ]; then
  echo "Usage: $0 <path> <version>"
  echo ""
  echo "Creates a package containing the useful parts of a Qt win32 SDK installation."
  echo "Install the Qt SDK with wine, then run this script on the install directory, eg:"
  echo "  $0 ~/.wine/drive_c/Qt/4.6.3 4.6.3"
  exit 1
fi

# Make the destination directory and create folders
rm -rf $dest
mkdir -v $dest
for f in bin src plugins lib include; do mkdir -v $dest/$f; done
for f in imageformats sqldrivers; do mkdir -v $dest/plugins/$f; done

# Extra libs
for f in $extradlls; do
  cp $path/bin/$f $dest/bin
done

for m in $modules; do
  # Bin
  cp $path/bin/${m}4.dll $dest/bin

  # Lib
  cp $path/lib/lib${m}4.a $dest/lib
  cp $path/lib/${m}.prl $dest/lib

  # Include
  mkdir $dest/include/$m
  cp -r $path/include/$m/* $dest/include/$m
done

# Src
for s in $src; do
  mkdir -v $dest/src/$s
  cp -r $path/src/$s/* $dest/src/$s
done

# Image format plugins
for i in $imageformats; do
  cp $path/plugins/imageformats/lib${i}4.a $dest/plugins/imageformats/
  cp $path/plugins/imageformats/${i}4.dll $dest/plugins/imageformats/
done

# SQL plugins
for s in $sqldrivers; do
  cp $path/plugins/sqldrivers/lib${s}4.a $dest/plugins/sqldrivers/
  cp $path/plugins/sqldrivers/${s}4.dll $dest/plugins/sqldrivers/
done

# Create the package
tar -cjf $dest.tar.bz2 $dest
rm -rf $dest
