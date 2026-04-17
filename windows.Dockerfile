FROM ubuntu:noble

# Use a fast EU mirror before any package operations.
RUN set -eux; \
  mirror='http://ftp.fau.de/ubuntu'; \
  if [ -f /etc/apt/sources.list.d/ubuntu.sources ]; then \
    sed -i "s|http://archive.ubuntu.com/ubuntu|${mirror}|g; s|http://security.ubuntu.com/ubuntu|${mirror}|g" /etc/apt/sources.list.d/ubuntu.sources; \
  fi; \
  if [ -f /etc/apt/sources.list ]; then \
    sed -i "s|http://archive.ubuntu.com/ubuntu|${mirror}|g; s|http://security.ubuntu.com/ubuntu|${mirror}|g" /etc/apt/sources.list; \
  fi

RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections

RUN apt-get update && apt-get install -y -q \
  autoconf \
  autopoint \
  bison \
  build-essential \
  bzip2 \
  cmake \
  flex \
  gettext \
  git-core \
  gtk-doc-tools \
  intltool \
  libglib2.0-dev \
  libtool \
  mingw-w64 \
  nsis \
  pkg-config \
  protobuf-compiler \
  python-is-python3 \
  python3 \
  python3-dev \
  python3-setuptools \
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

