# Target compiler
host=i686-w64-mingw32
cc=$(host)-gcc
cxx=$(host)-g++
ranlib=$(host)-ranlib

# Local compiler
build=i486-linux-gnu

# How many source files to build in parallel within each package
jobs=-j8

# Source and binary directories
src=/src
prefix=/target
work=$(src)/windows
stow=$(prefix)/stow

include ../makefile.common

# List of dlls that get included in the final package for Clementine
clementine_dlls=glew32.dll \
                libcdio-16.dll \
                libchromaprint.dll \
                libeay32.dll \
                libechonest.dll \
                libfaac.dll \
                libfaad.dll \
                libffi-6.dll \
                libfftw3-3.dll \
                libFLAC.dll \
                libgcrypt-20.dll \
                libgio-2.0-0.dll \
                libglib-2.0-0.dll \
                libgmodule-2.0-0.dll \
                libgmp-10.dll \
                libgnutls-28.dll \
                libgobject-2.0-0.dll \
                libgpg-error-0.dll \
                libgpod.dll \
                libgstapp-1.0-0.dll \
                libgstaudio-1.0-0.dll \
                libgstbase-1.0-0.dll \
                libgstcontroller-1.0-0.dll \
                libgstfft-1.0-0.dll \
                libgstnet-1.0-0.dll \
                libgstpbutils-1.0-0.dll \
                libgstreamer-1.0-0.dll \
                libgstriff-1.0-0.dll \
                libgstrtp-1.0-0.dll \
                libgstrtsp-1.0-0.dll \
                libgstsdp-1.0-0.dll \
                libgsttag-1.0-0.dll \
                libgstvideo-1.0-0.dll \
                libgthread-2.0-0.dll \
                libhogweed-2-4.dll \
                libiconv-2.dll \
                libid3tag.dll \
                libintl-8.dll \
                liblastfm.dll \
                libmad.dll \
                libmms-0.dll \
                libmp3lame-0.dll \
                libnettle-4-6.dll \
                libogg-0.dll \
                liboil-0.3-0.dll \
                libopus-0.dll \
                liborc-0.4-0.dll \
                liborc-test-0.4-0.dll \
                libplist.dll \
                libprotobuf-8.dll \
                libqjson.dll \
                libspeex-1.dll \
                libspotify.dll \
                libsqlite3-0.dll \
                libtag.dll \
                libtasn1-6.dll \
                libvorbis-0.dll \
                libvorbisenc-2.dll \
                libxml2-2.dll \
                pthreadGC2.dll \
                QtCore4.dll \
                QtGui4.dll \
                QtNetwork4.dll \
                QtOpenGL4.dll \
                QtSql4.dll \
                QtSvg4.dll \
                QtXml4.dll \
                ssleay32.dll \
                zlib1.dll
clementine_gst_plugins=libgstapetag.dll \
                       libgstapp.dll \
                       libgstasf.dll \
                       libgstaudioconvert.dll \
                       libgstaudiofx.dll \
                       libgstaudioparsers.dll \
                       libgstaudioresample.dll \
                       libgstaudiotestsrc.dll \
                       libgstautodetect.dll \
                       libgstcdio.dll \
                       libgstcoreelements.dll \
                       libgstdirectsoundsink.dll \
                       libgstequalizer.dll \
                       libgstfaac.dll \
                       libgstfaad.dll \
                       libgstflac.dll \
                       libgstgdp.dll \
                       libgstgio.dll \
                       libgsticydemux.dll \
                       libgstid3demux.dll \
                       libgstisomp4.dll \
                       libgstlame.dll \
                       libgstlibav.dll \
                       libgstmad.dll \
                       libgstmms.dll \
                       libgstogg.dll \
                       libgstopus.dll \
                       libgstplayback.dll \
                       libgstreplaygain.dll \
                       libgstsouphttpsrc.dll \
                       libgstspectrum.dll \
                       libgstspeex.dll \
                       libgsttaglib.dll \
                       libgsttcp.dll \
                       libgsttypefindfunctions.dll \
                       libgstudp.dll \
                       libgstvolume.dll \
                       libgstvorbis.dll \
                       libgstwavpack.dll \
                       libgstwavparse.dll
clementine_imageformats=qgif4.dll \
                        qjpeg4.dll
dont_strip=-not -name glew32.dll -not -name zlib1.dll -not -name libspotify.dll \
           -not -name ssleay32.dll -not -name libeay32.dll \
           -not -name ShellExecAsUser.dll \
           -not -name KillProc.dll \
           -not -name AccessControl.dll

# Useful macros for building packages
pkgconfig=PKG_CONFIG_LIBDIR=$(prefix)/lib/pkgconfig
autoconf=ACLOCAL_PATH=$(prefix)/share/aclocal:/usr/share/aclocal
ldflags=-L$(prefix)/lib
# -O2 is required to work around link errors in gettext
cflags=-I$(prefix)/include -O2
cxxflags=$(cflags)
configure=$(pkgconfig) LDFLAGS=$(ldflags) CFLAGS="$(cflags)" CXXFLAGS="$(cxxflags)" ./configure --host=$(host) --build=$(build) --prefix=$(prefix)
cmake=$(pkgconfig) cmake .. -DCMAKE_TOOLCHAIN_FILE=$(src)/Toolchain-mingw32.cmake -DCMAKE_INSTALL_PREFIX=$(prefix) -DCMAKE_C_FLAGS="$(cflags)" -DCMAKE_CXX_FLAGS="$(cxxflags)"
make=make $(jobs)
extractpkg=tar -xvf $(1)
buildpkg=(cd $(1) && $(configure) && $(make))
buildpkgcmake=(cd $(1) && mkdir build ; cd build && $(cmake) && $(make))
installpkg=rm -rf $(stow)/$(1) && \
	cd $(1) && \
	make install DESTDIR=$(stow)/$(1) && \
	mv -fv $(stow)/$(1)$(prefix)/* $(stow)/$(1)/ && \
	cd $(stow) && \
	stow -R $(1) && \
	touch $(work)/$@
installpkgcmake=rm -rf $(stow)/$(1) && \
	cd $(1)/build && \
	make install DESTDIR=$(stow)/$(1) && \
	mv -fv $(stow)/$(1)$(prefix)/* $(stow)/$(1)/ && \
	cd $(stow) && \
	stow -R $(1) && \
	touch $(work)/$@

extractandbuild=$(call extractpkg,$(1)) && $(call buildpkg,$(2)) && $(call installpkg,$(2))
extractandbuildcmake=$(call extractpkg,$(1)) && $(call buildpkgcmake,$(2)) && $(call installpkgcmake,$(2))


# Top-level targets
clementine-build-deps: dlfcn boost liblastfm qt taglib \
                       libgpod glew gstreamer win7sdk qtsparkle chromaprint \
                       protobuf spotify qjson fftw sparsehash pthreads echonest
clementine-gst-plugins: gst-plugins-base gst-plugins-good gst-plugins-bad \
                        gst-plugins-ugly gst-libav

clementine-deps: clementine-build-deps clementine-gst-plugins openssl glibnetworking
	-rm -rf clementine-deps
	mkdir -p clementine-deps/gstreamer-plugins
	mkdir -p clementine-deps/imageformats
	mkdir -p clementine-deps/nsisplugins
	mkdir -p clementine-deps/gio-modules
	for f in $(clementine_dlls); do \
		cp -v $(prefix)/bin/$$f clementine-deps/ || exit 1; \
	done
	for f in $(clementine_gst_plugins); do \
		cp -v $(prefix)/lib/gstreamer-1.0/$$f clementine-deps/gstreamer-plugins || exit 1; \
	done
	for f in $(clementine_imageformats); do \
		cp -v $(prefix)/plugins/imageformats/$$f clementine-deps/imageformats || exit 1; \
	done
	cp -v $(prefix)/lib/gio/modules/libgiognutls.dll clementine-deps/gio-modules/
	cp -vr $(src)/mingwm10.dll $(src)/nsisplugins clementine-deps/
	cp -vr /mingw/$(host)/*/libgcc_s_sjlj-1.dll clementine-deps/
	cp -vr /mingw/$(host)/lib/libstdc++-6.dll clementine-deps/
	for f in `find clementine-deps/ -name '*.dll' $(dont_strip)`; do \
		$(host)-strip -v $$f; \
	done


# The actual commands for compiling each package follow

.done-qjson: .done-qt
	$(call extractpkg,$(qjsontgz))
	cd $(qjson) && patch -p0 < ../patches/qjson-01-pkgconfig.patch
	mkdir -p $(qjson)/build
	cd $(qjson)/build && $(cmake) \
		-DQT_HEADERS_DIR=$(prefix)/include/ \
		-DQT_LIBRARY_DIR=$(prefix)/bin
	cd $(qjson)/build && $(make)
	sed -e 's/QtCore//' -i $(qjson)/build/QJson.pc
	rm -rf $(stow)/$(qjson)
	cd $(qjson)/build && make install DESTDIR=$(stow)/$(qjson)
	cd $(qjson)/build && mv -fv $(stow)/$(qjson)$(prefix)/* $(stow)/$(qjson)
	cd $(stow) && stow -R $(qjson)
	touch $@

.done-zlib:
	$(call extractpkg,$(zlibtgz))
	cd $(zlib) && PREFIX="$(host)-" CC=$(cc) CXX=$(cxx) RANLIB=$(ranlib) ./configure --prefix=$(prefix)
	cd $(zlib) && make -f win32/Makefile.gcc PREFIX="$(host)-" CC=$(cc) CXX=$(cxx) LDSHAREDLIBC="" SHARED_MODE=1
	cd $(zlib) && make -f win32/Makefile.gcc \
		PREFIX="$(host)-" CC=$(cc) CXX=$(cxx) \
		BINARY_PATH=$(stow)/$(zlib)/bin \
		INCLUDE_PATH=$(stow)/$(zlib)/include \
		LIBRARY_PATH=$(stow)/$(zlib)/lib \
		LDSHAREDLIBC="" SHARED_MODE=1 install
	cd $(stow) && stow -R $(zlib)
	touch $@

.done-iconv:
	$(call extractpkg,$(libiconvtgz))
	$(call buildpkg,$(libiconv))
	rm -rf $(stow)/$(libiconv)
	cd $(libiconv) && make install DESTDIR=$(stow)/$(libiconv)
	mv -fv $(stow)/$(libiconv)$(prefix)/* $(stow)/$(libiconv)
	rm -f $(stow)/$(libiconv)/lib/charset.alias
	cd $(stow) && stow -R $(libiconv)
	touch $@

.done-gettext: .done-iconv
	$(call extractpkg,$(gettexttgz))
	patch -d $(gettext) -p1 < patches/gettext-01-woe32.patch
	patch -d $(gettext) -p1 < patches/gettext-02-reloc.patch
	$(call buildpkg,$(gettext))
	$(call installpkg,$(gettext))

.done-glib: .done-zlib .done-gettext .done-ffi
	$(call extractandbuild,$(glibtgz),$(glib))

.done-gmp:
	$(call extractpkg,$(gmptgz))
	cd $(gmp) && $(configure) --enable-shared --disable-static
	cd $(gmp) && $(make)
	$(call installpkg,$(gmp))

.done-nettle: .done-gmp
	$(call extractpkg,$(nettletgz))
	cd $(nettle) && $(configure)
	cd $(nettle) && $(make) libnettle-4-6.dll
	cd $(nettle) && $(make) libhogweed-2-4.dll
	$(call installpkg,$(nettle))

.done-libgpgerror:
	$(call extractandbuild,$(gpgerrortgz),$(gpgerror))

.done-gcrypt: .done-libgpgerror .done-gettext
	$(call extractpkg,$(gcrypttgz))
	cd $(gcrypt) && $(configure) --with-gpg-error-prefix=$(prefix)
	cd $(gcrypt) && $(make)
	$(call installpkg,$(gcrypt))

.done-libtasn1:
	$(call extractandbuild,$(tasn1tgz),$(tasn1))

.done-libgnutls: .done-gcrypt .done-libtasn1 .done-nettle
	$(call extractandbuild,$(gnutlstgz),$(gnutls))

.done-win7sdk:
	cp -r $(src)/$(win7sdk) $(stow)/
	cd $(stow) && stow $(win7sdk)
	touch $@

.done-sqlite:
	$(call extractpkg,$(sqlitetgz),$(sqlite))
	(cd $(sqlite) && $(configure) && $(make))
	$(call installpkg,$(sqlite))

.done-libxml: .done-iconv
	$(call extractpkg,$(xmltgz))
	cd $(xml) && $(configure) --without-python
	cd $(xml) && $(make)
	$(call installpkg,$(xml))

.done-glibnetworking: .done-glib .done-libgnutls
	$(call extractandbuild,$(glibnetworkingtgz),$(glibnetworking))

.done-libsoup: .done-glib .done-libxml
	$(call extractpkg,$(souptgz))
	cd $(soup) && patch -p0 < ../patches/libsoup-01-winsock.patch
	(cd $(soup) && $(configure) && $(make))
	$(call installpkg,$(soup))
	touch $@

.done-libplist: .done-libxml .done-glib
	tar -xf $(plisttgz)
	-mkdir $(plist)/build
	cd $(plist)/build && $(cmake)
	cd $(plist)/build && make
	rm -rf $(stow)/$(plist)
	cd $(plist)/build && make install DESTDIR=$(stow)/$(plist)
	mv -fv $(stow)/$(plist)$(prefix)/* $(stow)/$(plist)/
	cd $(stow) && stow $(plist)
	touch $@

.done-libgpod: .done-sqlite .done-libplist .done-glib
	$(call extractandbuildcmake,$(gpodtgz),$(gpod))

.done-gstreamer: .done-glib .done-libxml .done-orc
	$(call extractpkg,$(gsttgz))
	cd $(gst) && $(configure) --disable-examples --disable-tests
	cd $(gst) && $(make)
	$(call installpkg,$(gst))

.done-gst-plugins-base: .done-gstreamer .done-ogg .done-vorbis .done-opus
	$(call extractpkg,$(gstbasetgz))
	cd $(gstbase) && autoreconf
	cd $(gstbase) && $(configure) --disable-examples --disable-x --disable-xvideo --disable-xshm
	cd $(gstbase) && $(make)
	$(call installpkg,$(gstbase))

.done-orc:
	$(call extractandbuild,$(orctgz),$(orc))

.done-ogg:
	$(call extractandbuild,$(oggtgz),$(ogg))

.done-vorbis: .done-ogg
	$(call extractandbuild,$(vorbistgz),$(vorbis))

.done-gst-plugins-good: .done-gstreamer .done-gst-plugins-base .done-flac .done-speex .done-libsoup .done-wavpack
	$(call extractpkg,$(gstgoodtgz))
	cd $(gstgood) && patch -p1 < ../patches/gst-plugins-good-02-equalizer-writeable-buffers.patch

	cd $(gstgood) && $(configure) --disable-shout2 --disable-examples --disable-x --disable-deinterlace
	sed -i.bak 's/$$ECHO "$$win32_libid_type"/$$ECHO "x86 DLL"/' $(gstgood)/libtool
	cd $(gstgood) && $(make)
	$(call installpkg,$(gstgood))

.done-libmpcdec:
	$(call extractpkg,$(mpcdectgz))
	cd $(mpcdec) && \
		CFLAGS="-fno-common" \
		CXXFLAGS="-fno-common" \
		LDFLAGS="-Wl,-no-undefined" \
			$(configure) ac_cv_func_memcmp_working=yes
	cd $(mpcdec) && $(make)
	rm -rf $(stow)/$(mpcdec)
	cd $(mpcdec) && make install DESTDIR=$(stow)/$(mpcdec)
	mv -fv $(stow)/$(mpcdec)$(prefix)/* $(stow)/$(mpcdec)/
	cp $(mpcdec)/include/mpcdec/config_win32.h $(stow)/$(mpcdec)/include/mpcdec/
	cd $(stow) && stow -R $(mpcdec)
	touch $(work)/$@

.done-wavpack:
	$(call extractpkg,$(wavpacktgz))
	cd $(wavpack) && \
		CPPFLAGS="-D__MSVCRT_VERSION__=0x0601" \
		CFLAGS="-fno-common" \
		CXXFLAGS="-fno-common" \
		LDFLAGS="-Wl,-no-undefined" \
			$(configure)
	cd $(wavpack) && $(make)
	$(call installpkg,$(wavpack))

.done-flac:
	$(call extractpkg,$(flactgz))
	cd $(flac) && patch -p0 < ../patches/flac-01-size-t-max.patch
	cd $(flac) && patch -p0 < ../patches/flac-02-include.patch
	cd $(flac) && $(configure)
	cd $(flac) && $(make)

	# libtool is retarded and doesn't link this dll properly
	cd $(flac)/src/libFLAC && /bin/bash ../../libtool --mode=link $(host)-gcc \
		--shared  -I/target/include -O3 -funroll-loops -finline-functions \
		-Wall -W -Winline -g -O2 -o libFLAC.dll -rpath $(prefix)/lib \
		-version-info 10:0:2 -lm -lws2_32 *.lo -L$(prefix)/lib -logg

	rm -rf $(stow)/$(flac)
	cd $(flac) && make install DESTDIR=$(stow)/$(flac)
	mv -fv $(stow)/$(flac)$(prefix)/* $(stow)/$(flac)/
	cp $(flac)/src/libFLAC/libFLAC.dll $(stow)/$(flac)/bin
	rm -f $(stow)/$(flac)/lib/libFLAC.*
	sed -i.bak -e's/\/lib/\/bin/' $(stow)/$(flac)/lib/pkgconfig/*.pc
	cd $(stow) && stow -R $(flac)
	touch $@

.done-speex: .done-ogg
	$(call extractpkg,$(speextgz))
	cd $(speex) && $(configure)
	cd $(speex) && $(make)

	rm -rf $(stow)/$(speex)
	cd $(speex) && make install DESTDIR=$(stow)/$(speex)
	mv -fv $(stow)/$(speex)$(prefix)/* $(stow)/$(speex)/
	rm -f $(stow)/$(speex)/lib/libspeex.*
	sed -i.bak -e's/\/lib/\/bin/' $(stow)/$(speex)/lib/pkgconfig/*.pc
	sed -i.bak2 -e's/-lspeex/-lspeex-1/' $(stow)/$(speex)/lib/pkgconfig/speex.pc
	cd $(stow) && stow -R $(speex)
	touch $@

.done-gst-plugins-ugly: .done-gstreamer .done-gst-plugins-base .done-oil .done-mad .done-lame .done-cdio
	$(call extractpkg,$(gstuglytgz))
	cd $(gstugly) && \
		$(pkgconfig) LDFLAGS="-L/target/bin $(ldflags)" CFLAGS="$(cflags)" \
		./configure --host=$(host) --build=$(build) --prefix=$(prefix) \
		--disable-examples
	sed -i.bak 's/$$ECHO "$$win32_libid_type"/$$ECHO "x86 DLL"/' $(gstugly)/libtool
	cd $(gstugly) && $(make)
	$(call installpkg,$(gstugly))

.done-oil:
	$(call extractandbuild,$(oiltgz),$(oil))

.done-id3tag:
	$(call extractpkg,$(id3tagtgz))
	cd $(id3tag) && $(configure)
	cd $(id3tag) && $(make)

	# libtool is retarded and doesn't link this dll properly
	cd $(id3tag) && /bin/bash ./libtool --mode=link $(host)-gcc \
		-Wall -g -O2 --shared  -o libid3tag.dll -rpath /target/lib \
		-version-info 3:0:3 *.lo -L/target/lib -lz

	rm -rf $(stow)/$(id3tag)
	cd $(id3tag) && make install DESTDIR=$(stow)/$(id3tag)
	mv -fv $(stow)/$(id3tag)$(prefix)/* $(stow)/$(id3tag)/
	-mkdir $(stow)/$(id3tag)/bin/
	cp $(id3tag)/libid3tag.dll $(stow)/$(id3tag)/bin/
	rm -f $(stow)/$(id3tag)/lib/libid3tag.*
	cd $(stow) && stow -R $(id3tag)
	touch $@

.done-mad: .done-id3tag
	$(call extractpkg,$(madtgz))
	cd $(mad) && patch -p0 < ../patches/libmad-01-force-mem.patch
	$(call buildpkg,$(mad))

	# libtool is retarded and doesn't link this dll properly
	cd $(mad) && /bin/bash ./libtool --mode=link $(host)-gcc \
		-Wall -march=i486 -g -O -fforce-addr -fthread-jumps \
		-fcse-follow-jumps -fcse-skip-blocks -fexpensive-optimizations \
		-fregmove -fschedule-insns2 -fstrength-reduce --shared  \
		-o libmad.dll -rpath /target/lib -version-info 2:1:2 *.lo

	rm -rf $(stow)/$(mad)
	cd $(mad) && make install DESTDIR=$(stow)/$(mad)
	mv -fv $(stow)/$(mad)$(prefix)/* $(stow)/$(mad)/
	-mkdir $(stow)/$(mad)/bin/
	cp $(mad)/libmad.dll $(stow)/$(mad)/bin/
	rm -f $(stow)/$(mad)/lib/libmad.*
	cd $(stow) && stow -R $(mad)
	touch $@

.done-lame:
	$(call extractandbuild,$(lametgz),$(lame))

.done-gst-plugins-bad: .done-gstreamer .done-gst-plugins-base .done-faad .done-faac .done-libmms .done-oil .done-libmpcdec
	$(call extractpkg,$(gstbadtgz))
	cd $(gstbad) && \
		$(pkgconfig) LDFLAGS="-L/target/bin $(ldflags)" CFLAGS="$(cflags)" \
		./configure --host=$(host) --build=$(build) --prefix=$(prefix) \
		--disable-acm \
		--disable-apexsink \
		--disable-examples \
		--disable-dccp \
		--disable-dtls
	sed -i.bak 's/$$ECHO "$$win32_libid_type"/$$ECHO "x86 DLL"/' $(gstbad)/libtool
	cd $(gstbad) && $(make)
	$(call installpkg,$(gstbad))

.done-gst-libav: .done-gstreamer .done-gst-plugins-base
	$(call extractpkg,$(gstlibavtgz))
	cd $(gstlibav) && autoreconf
	cd $(gstlibav) && $(configure) --with-ffmpeg-extra-configure="--enable-shared --disable-debug"
	cd $(gstlibav) && $(make)
	rm -rf $(stow)/$(gstlibav)
	cd $(gstlibav) && make install DESTDIR=$(stow)/$(gstlibav)
	mv -fv $(stow)/$(gstlibav)$(prefix)/* $(stow)/$(gstlibav)/
	-mkdir $(stow)/$(gstlibav)/bin/
	cp $(gstlibav)/ext/libav/.libs/*.dll $(stow)/$(gstlibav)/bin/
	cd $(stow) && stow -R $(gstlibav)
	touch $@

.done-faad:
	$(call extractpkg,$(faadtgz))
	cd $(faad) && patch -p0 < ../patches/faad-01-off_t.patch
	$(call buildpkg,$(faad))

	# libtool is retarded and doesn't link this dll properly
	cd $(faad)/libfaad && /bin/bash ../libtool --mode=link $(host)-gcc \
		-iquote ../include -g -O2 --shared -o libfaad.dll -rpath $(prefix)/bin \
		-version-info 2:0:0 *.lo -lm

	rm -rf $(stow)/$(faad)
	cd $(faad) && make install DESTDIR=$(stow)/$(faad)
	mv -fv $(stow)/$(faad)$(prefix)/* $(stow)/$(faad)/
	-mkdir $(stow)/$(faad)/bin/
	cp $(faad)/libfaad/libfaad.dll $(stow)/$(faad)/bin/
	rm -f $(stow)/$(faad)/lib/libfaad.*
	cd $(stow) && stow -R $(faad)
	touch $@

.done-faac:
	$(call extractpkg,$(faactgz))
	cd $(faac) && patch -p0 < ../patches/faac-01-buildfixes.patch
	$(call buildpkg,$(faac))

	# libtool is retarded and doesn't link this dll properly
	cd $(faac)/libfaac && /bin/bash ../libtool --mode=link $(host)-gcc \
		-iquote ../include -g -O2 --shared -o libfaac.dll -rpath $(prefix)/bin \
		-version-info 2:0:0 *.lo -lm

	rm -rf $(stow)/$(faac)
	cd $(faac) && make install DESTDIR=$(stow)/$(faac)
	mv -fv $(stow)/$(faac)$(prefix)/* $(stow)/$(faac)/
	-mkdir $(stow)/$(faac)/bin/
	cp $(faac)/libfaac/libfaac.dll $(stow)/$(faac)/bin/
	rm -f $(stow)/$(faac)/lib/libfaac.*
	cd $(stow) && stow -R $(faac)
	touch $@

.done-libmms: .done-glib
	$(call extractpkg,$(mmswin32tgz))
	cd $(mmswin32) && $(autoconf) ./autogen.sh
	cd $(mmswin32) && patch -p0 < ../patches/mms-01-buildfixes.patch
	cd $(mmswin32) && $(configure)
	cd $(mmswin32) && patch -p0 < ../patches/mms-02-config.patch
	cd $(mmswin32) && patch -p0 < ../patches/mms-03-off_t.patch
	cd $(mmswin32) && $(make)
	$(call installpkg,$(mmswin32))

# Not working - requires iconv.h
.done-libquicktime: .done-dlfcn
	$(call extractpkg,$(quicktimetgz))
	cd $(quicktime) && patch -p0 < ../patches/libquicktime-01-configure.patch
	cd $(quicktime) && autoconf
	cd $(quicktime) && $(configure) --without-doxygen --without-ffmpeg --without-libiconv-prefix
	cd $(quicktime) && $(make)
	$(call installpkg,$(quicktime))

.done-dlfcn:
	-mkdir $(stow)/$(dlfcn)/
	tar -xjf $(dlfcntgz) -C $(stow)/$(dlfcn)/
	cd $(stow) && stow -R $(dlfcn)
	touch $@

.done-usb:
	unzip -o -d $(stow) $(usbwin32zip)
	mv $(stow)/$(usbwin32)/bin/x86/* $(stow)/$(usbwin32)/bin
	mv $(stow)/$(usbwin32)/lib/gcc/* $(stow)/$(usbwin32)/lib
	-rm -f $(stow)/$(usbwin32)/lib/pkgconfig/libusb-1.0.pc
	patch -d $(stow)/$(usbwin32) -p0 < patches/libusb-01-pkgconfig.patch
	cp $(stow)/$(usbwin32)/include/usb.h $(stow)/$(usbwin32)/include/libusb.h
	cd $(stow) && stow $(usbwin32)
	touch $@

.done-pthreads:
	tar -xzf $(pthreadstgz) -C $(stow)
	patch -d $(stow)/$(pthreads) -p0 < patches/pthreads-01-timespec.patch
	cd $(stow) && stow $(pthreads)
	touch $@

.done-taglib: .done-glib
	$(call extractpkg,$(taglibtgz))
	-mkdir $(taglib)/build

	cd $(taglib)/build && $(cmake) -DWITH_ASF=ON -DWITH_MP4=ON -DBUILD_SHARED_LIBS=ON
	cd $(taglib)/build && $(make)
	rm -rf $(stow)/$(taglib)
	cd $(taglib)/build && make install DESTDIR=$(stow)/$(taglib)
	cd $(taglib)/build && mv -fv $(stow)/$(taglib)$(prefix)/* $(stow)/$(taglib)
	cd $(stow) && stow -R $(taglib)
	touch $@

.done-qt: .done-openssl .done-sqlite .done-glib
	$(call extractpkg,$(qttgz))
	patch -d $(qt) -p0 < patches/qt-01-codecs.patch
	patch -d $(qt) -p0 < patches/qt-02-dir.patch
	patch -d $(qt) -p1 < patches/qt-03-config.patch
	cd $(qt) && OPENSSL_LIBS="-llibeay32 -lssleay32" ./configure \
		-opensource -confirm-license \
		-platform linux-g++-32 \
		-xplatform win32-g++ -device-option CROSS_COMPILE=i686-w64-mingw32- \
		-prefix $(stow)/$(qt) \
		-no-phonon -no-webkit -no-xmlpatterns -no-qt3support \
		-no-declarative -no-audio-backend \
		-no-script -no-scripttools \
		-nomake demos -nomake examples \
		-no-exceptions \
		-qt-sql-sqlite -system-sqlite \
		-openssl-linked
	cd $(qt) && $(make)
	cd $(qt) && make install
	mv -fv $(stow)/$(qt)/lib/*.dll $(stow)/$(qt)/bin/
	cd $(stow) && stow -R $(qt)
	touch $@

.done-liblastfm: .done-qt
	$(call extractpkg,$(lastfmtgz))
	-mkdir $(lastfm)/build
	cd $(lastfm)/build && $(cmake) \
		-DQT_HEADERS_DIR=$(prefix)/include/ \
		-DQT_LIBRARY_DIR=$(prefix)/bin
	cd $(lastfm)/build && $(make)
	rm -rf $(stow)/$(lastfm)
	cd $(lastfm)/build && make install DESTDIR=$(stow)/$(lastfm)
	cd $(lastfm)/build && mv -fv $(stow)/$(lastfm)$(prefix)/* $(stow)/$(lastfm)
	cd $(stow) && stow -R $(lastfm)
	touch $@

.done-glew:
	unzip -o -d $(stow)/ $(glewwin32zip)
	-rm $(stow)/$(glew)/*.txt
	cd $(stow) && stow -R $(glew)
	touch $@

.done-boost:
	tar -xf $(boosttgz) -C $(stow)
	cd $(stow) && stow -R $(boost)
	touch $@

.done-qtsparkle:
	$(call extractpkg,$(qtsparkletgz))
	-mkdir $(qtsparkle)/build
	cd $(qtsparkle)/build && $(cmake) \
		-DQT_HEADERS_DIR=$(prefix)/include/ \
		-DQT_LIBRARY_DIR=$(prefix)/bin \
		-DCMAKE_BUILD_TYPE=Release
	cd $(qtsparkle)/build && $(make)
	rm -rf $(stow)/$(qtsparkle)
	cd $(qtsparkle)/build && make install DESTDIR=$(stow)/$(qtsparkle)
	cd $(qtsparkle)/build && mv -fv $(stow)/$(qtsparkle)$(prefix)/* $(stow)/$(qtsparkle)
	cd $(stow) && stow -R $(qtsparkle)
	touch $@

.done-curl:
	$(call extractandbuild,$(curltgz),$(curl))

.done-fftw:
	$(call extractpkg,$(fftwtgz))
	cd $(fftw) && $(configure) \
		--with-our-malloc16 --with-windows-f77-mangling --enable-shared \
		--disable-static --enable-threads --with-combined-threads \
		--enable-portable-binary
	cd $(fftw) && $(make)
	$(call installpkg,$(fftw))

.done-libarchive: .done-libxml
	$(call extractpkg,$(archivetgz))
	-mkdir $(archive)/bin
	cd $(archive) && patch -p0 < ../patches/libarchive-01-no-iconv.patch
	cd $(archive) && patch -p0 < ../patches/libarchive-02-pkgconfig.patch
	cd $(archive)/bin && $(cmake) \
		-DENABLE_OPENSSL=OFF \
		-DENABLE_TAR=OFF \
		-DENABLE_CPIO=OFF \
		-DENABLE_XATTR=OFF \
		-DENABLE_ACL=OFF \
		-DENABLE_TEST=OFF
	cd $(archive)/bin && $(make)
	rm -rf $(stow)/$(archive)
	cd $(archive)/bin && make install DESTDIR=$(stow)/$(archive)
	mv -fv $(stow)/$(archive)$(prefix)/* $(stow)/$(archive)/
	cd $(stow) && stow $(archive)
	touch $@

.done-protobuf:
	# Compile a host version first for protoc
	$(call extractpkg,$(protobuftgz))
	-cd $(protobuf) && make clean
	cd $(protobuf) && ./configure --prefix=$(prefix)
	cd $(protobuf) && $(make)
	cd $(protobuf) && make install
	-rm -fv $(prefix)/lib/libproto*.la
	-rm -fv $(prefix)/lib/libproto*.a
	-rm -rfv $(prefix)/include/google
	-rm -rf $(prefix)/lib/pkgconfig/protobuf*.pc
	cd $(protobuf) && make clean

	# Now do the target build
	$(call extractandbuild,$(protobuftgz),$(protobuf))

.done-spotify:
	-mkdir -p $(stow)/$(spotifywin32)
	unzip -o -d $(stow)/$(spotifywin32) $(spotifywin32zip)
	rm -rf $(stow)/$(spotifywin32)/README
	rm -rf $(stow)/$(spotifywin32)/LICENSE
	rm -rf $(stow)/$(spotifywin32)/ChangeLog
	rm -rf $(stow)/$(spotifywin32)/*.txt
	rm -rf $(stow)/$(spotifywin32)/*.xhtml
	rm -rf $(stow)/$(spotifywin32)/docs
	rm -rf $(stow)/$(spotifywin32)/examples
	rm -rf $(stow)/$(spotifywin32)/images
	-mkdir $(stow)/$(spotifywin32)/bin
	-mkdir -p $(stow)/$(spotifywin32)/lib/pkgconfig
	mv -v $(stow)/$(spotifywin32)/lib/libspotify.dll $(stow)/$(spotifywin32)/bin/
	cp $(src)/libspotify.pc $(stow)/$(spotifywin32)/lib/pkgconfig
	cd $(stow) && stow $(spotifywin32)
	touch $@

.done-cdio:
	$(call extractpkg,$(cdiotgz))
	cd $(cdio) && $(configure) \
		--without-cd-drive --without-cd-info \
		--without-cdda-player --without-cd-read --without-iso-info \
		--without-iso-read --disable-largefile
	cd $(cdio) && $(make)
	rm -rf $(stow)/$(cdio)
	cd $(cdio) && make install DESTDIR=$(stow)/$(cdio)
	mv -fv $(stow)/$(cdio)$(prefix)/* $(stow)/$(cdio)/
	rm -rf $(stow)/$(cdio)/share/info
	cd $(stow) && stow $(cdio)
	touch $@

.done-openssl:
	$(call extractpkg,$(openssltgz))
	cd $(openssl) && ./Configure \
		--cross-compile-prefix="$(host)-" \
		--prefix=$(stow)/$(openssl) \
		--shared \
		mingw
	cd $(openssl) && make
	cd $(openssl) && make install
	cd $(stow) && stow -R $(openssl)
	touch $@

.done-sparsehash:
	$(call extractandbuild,$(sparsehashtgz),$(sparsehash))

.done-ffi:
	$(call extractandbuild,$(ffitgz),$(ffi))

.done-opus:
	$(call extractandbuild,$(opustgz),$(opus))

.done-echonest: .done-qt .done-qjson
	$(call extractpkg,$(echonesttgz))
	-mkdir $(echonest)/build
	cd $(echonest)/build && $(cmake) \
		-DQT_HEADERS_DIR=$(prefix)/include/ \
		-DQT_LIBRARY_DIR=$(prefix)/bin \
		-DCMAKE_BUILD_TYPE=Release
	cd $(echonest)/build && $(make)
	rm -rf $(stow)/$(echonest)
	cd $(echonest)/build && make install DESTDIR=$(stow)/$(echonest)
	cd $(echonest)/build && mv -fv $(stow)/$(echonest)$(prefix)/* $(stow)/$(echonest)
	cd $(stow) && stow -R $(echonest)
	touch $@

.done-chromaprint: .done-fftw
	$(call extractpkg,$(chromaprinttgz))
	-mkdir $(chromaprint)/build
	cd $(chromaprint)/build && $(cmake) \
		-DQT_HEADERS_DIR=$(prefix)/include/ \
		-DQT_LIBRARY_DIR=$(prefix)/bin \
		-DCMAKE_BUILD_TYPE=Release
	cd $(chromaprint)/build && $(make)
	rm -rf $(stow)/$(chromaprint)
	cd $(chromaprint)/build && make install DESTDIR=$(stow)/$(chromaprint)
	cd $(chromaprint)/build && mv -fv $(stow)/$(chromaprint)$(prefix)/* $(stow)/$(chromaprint)
	cd $(stow) && stow -R $(chromaprint)
	touch $@
