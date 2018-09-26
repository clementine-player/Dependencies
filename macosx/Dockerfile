FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y curl xz-utils build-essential gobjc++ git python stow pkg-config libglib2.0-dev bison flex protobuf-compiler cmake unzip vim intltool gettext yasm
#RUN curl -SL https://github.com/tpoechtrager/osxcross/raw/master/tarballs/cctools-895-ld64-274.2_8e9c3f2.tar.xz | tar -xJ
#RUN cd cctools-895-ld64-274.2_8e9c3f2/cctools && ./configure --prefix=/usr --target=x86_64-apple-darwin && make && make install

RUN git clone https://github.com/tpoechtrager/apple-libtapi.git
RUN cd apple-libtapi && INSTALLPREFIX=/usr ./build.sh && ./install.sh

RUN git clone https://github.com/tpoechtrager/cctools-port.git
RUN cd cctools-port/cctools && ./configure --prefix=/usr --with-libtapi=/usr --target=x86_64-apple-darwin && make && make install

RUN mkdir -p /Developer/SDKs
RUN curl -SL https://storage.googleapis.com/clementine-data.appspot.com/Build%20dependencies/MacOSX10.13.sdk.tar.xz | tar -xJC /Developer/SDKs
RUN curl -SL https://releases.llvm.org/7.0.0/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz | tar -xJ --strip-components=1 -C /usr
RUN ln -s /usr/bin/clang /usr/bin/x86_64-apple-darwin-clang
RUN ln -s /usr/bin/clang++ /usr/bin/x86_64-apple-darwin-clang++
RUN ln -s /usr/bin/clang /usr/bin/x86_64-apple-darwin-gcc
RUN ln -s /usr/bin/clang++ /usr/bin/x86_64-apple-darwin-g++
RUN git clone --branch=master https://github.com/clementine-player/Dependencies /src
RUN mkdir -p /target/stow
RUN mkdir -p /target/lib
RUN mkdir -p /target/bin
RUN cd /src/macosx && make all-downloads
ADD glib.cache /src/macosx/
ADD mpcdec.cache /src/macosx/
ADD oil.cache /src/macosx/
RUN chmod -w /src/macosx/*.cache
ENV GLIB_GENMARSHAL /usr/bin/glib-genmarshal
ADD Makefile /src/macosx/Makefile
ADD patches/qt-03-objc.patch /src/macosx/patches
ADD patches/qt-04-highsierra.patch /src/macosx/patches
ADD Toolchain-Darwin.cmake /src/macosx/Toolchain-Darwin.cmake
ADD https://raw.githubusercontent.com/Homebrew/brew/master/Library/Homebrew/os/mac/pkgconfig/10.13/libxml-2.0.pc /target/lib/pkgconfig/libxml-2.0.pc
RUN cd /src/macosx && make clementine-deps
