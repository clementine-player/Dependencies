FROM i386/ubuntu:eoan

RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections

RUN apt-get update && apt-get install -y -q \
  autoconf \
  bison \
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
  python \
  stow \
  sudo \
  texinfo \
  unzip \
  wget \
  wine-stable \
  yasm

RUN update-alternatives --set i686-w64-mingw32-gcc /usr/bin/i686-w64-mingw32-gcc-posix
RUN update-alternatives --set i686-w64-mingw32-g++ /usr/bin/i686-w64-mingw32-g++-posix
COPY /target /target
