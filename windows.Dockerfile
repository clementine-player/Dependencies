FROM ubuntu:noble

RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections

RUN apt-get update && apt-get install -y -q \
  autoconf \
  bison \
  bzip2 \
  cmake \
  flex \
  gettext \
  git-core \
  intltool \
  libglib2.0-dev \
  libtool \
  mingw-w64 \
  nsis \
  pkg-config \
  protobuf-compiler \
  python3 \
  python3-dev \
  stow \
  sudo \
  texinfo \
  unzip \
  wget \
  wine-stable \
  xz-utils \
  yasm

RUN update-alternatives --set i686-w64-mingw32-gcc /usr/bin/i686-w64-mingw32-gcc-posix
RUN update-alternatives --set i686-w64-mingw32-g++ /usr/bin/i686-w64-mingw32-g++-posix

RUN mkdir -p /src
RUN mkdir -p /target/stow

COPY . /src
WORKDIR /src/windows

# Separate this step to cache it before any build failures.
RUN make all-downloads

RUN make

