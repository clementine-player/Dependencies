# Target compiler
host=x86_64-w64-mingw32
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
                libcdio-19.dll \
                libchromaprint.dll \
                libcrypto-1_1.dll \
                libfaad-2.dll \
                libffi-7.dll \
                libfftw3-3.dll \
                libFLAC-8.dll \
                libgcrypt-20.dll \
                libgio-2.0-0.dll \
                libglib-2.0-0.dll \
                libgmodule-2.0-0.dll \
                libgmp-10.dll \
                libgnutls-30.dll \
                libgobject-2.0-0.dll \
                libgpg-error-0.dll \
                libgstapp-1.0-0.dll \
                libgstaudio-1.0-0.dll \
                libgstbase-1.0-0.dll \
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
                libhogweed-6.dll \
                libiconv-2.dll \
                libintl-8.dll \
                liblastfm5.dll \
                libmms-0.dll \
                libmp3lame-0.dll \
                libnettle-8.dll \
                libogg-0.dll \
                liboil-0.3-0.dll \
                libopus-0.dll \
                liborc-0.4-0.dll \
                liborc-test-0.4-0.dll \
                libp11-kit-0.dll \
                libpcre-1.dll \
                libprotobuf-17.dll \
                libpsl-5.dll \
                libssl-1_1.dll \
                libsoup-2.4-1.dll \
                libspeex-1.dll \
                libspotify.dll \
                libsqlite3-0.dll \
                libtag.dll \
                libtasn1-6.dll \
                libunistring-2.dll \
                libvorbis-0.dll \
                libvorbisenc-2.dll \
                libxml2-2.dll \
                libwavpack-1.dll \
                Qt5Concurrent.dll \
                Qt5Core.dll \
                Qt5Gui.dll \
                Qt5Network.dll \
                Qt5OpenGL.dll \
                Qt5Sql.dll \
                Qt5Svg.dll \
                Qt5Widgets.dll \
                Qt5WinExtras.dll \
                Qt5Xml.dll \
                zlib1.dll
clementine_gst_plugins=libgstaiff.dll \
                       libgstapetag.dll \
                       libgstapp.dll \
                       libgstasf.dll \
                       libgstasfmux.dll \
                       libgstaudioconvert.dll \
                       libgstaudiofx.dll \
                       libgstaudioparsers.dll \
                       libgstaudioresample.dll \
                       libgstaudiotestsrc.dll \
                       libgstautodetect.dll \
                       libgstcdio.dll \
                       libgstcoreelements.dll \
                       libgstdirectsound.dll \
                       libgstequalizer.dll \
                       libgstfaad.dll \
                       libgstflac.dll \
                       libgstgdp.dll \
                       libgstgio.dll \
                       libgsticydemux.dll \
                       libgstid3demux.dll \
                       libgstid3tag.dll \
                       libgstisomp4.dll \
                       libgstlame.dll \
                       libgstlibav.dll \
                       libgstmms.dll \
                       libgstogg.dll \
                       libgstopus.dll \
                       libgstopusparse.dll \
                       libgstpbtypes.dll \
                       libgstplayback.dll \
                       libgstreplaygain.dll \
                       libgstrtp.dll \
                       libgstrtsp.dll \
                       libgstsoup.dll \
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

clementine_imageformats=qgif.dll qjpeg.dll qsvg.dll
dont_strip=-not -name glew32.dll \
           -not -name zlib1.dll \
           -not -name libspotify.dll \
           -not -name ShellExecAsUser.dll \
           -not -name KillProc.dll \
           -not -name AccessControl.dll

# Useful macros for building packages
pkgconfig=PKG_CONFIG_LIBDIR=$(prefix)/lib/pkgconfig
autoconf=ACLOCAL_PATH=$(prefix)/share/aclocal:/usr/share/aclocal
ldflags=-L$(prefix)/lib -lpthread
# -O2 is required to work around link errors in gettext
cflags=-I$(prefix)/include -O2 -D__USE_MINGW_ANSI_STDIO
cxxflags=$(cflags)
configure=$(pkgconfig) LDFLAGS="$(ldflags)" CFLAGS="$(cflags)" CXXFLAGS="$(cxxflags)" ./configure --host=$(host) --build=$(build) --prefix=$(prefix)
cmake=$(pkgconfig) cmake .. -DCMAKE_TOOLCHAIN_FILE=$(src)/Toolchain-mingw32.cmake -DCMAKE_INSTALL_PREFIX=$(prefix) -DCMAKE_C_FLAGS="$(cflags)" -DCMAKE_CXX_FLAGS="$(cxxflags)"
make=make $(jobs)
extractpkg=tar -xf $(1) --no-same-owner
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
installpkgmeson=rm -rf $(stow)/$(1) && \
	cd $(1) && \
	DESTDIR=$(stow)/$(1) ninja -C _build install && \
	mv -fv $(stow)/$(1)$(prefix)/* $(stow)/$(1)/ ; \
	cd $(stow) && \
	stow -R $(1) && \
	touch $(work)/$@

extractandbuild=$(call extractpkg,$(1)) && $(call buildpkg,$(2)) && $(call installpkg,$(2))
extractandbuildcmake=$(call extractpkg,$(1)) && $(call buildpkgcmake,$(2)) && $(call installpkgcmake,$(2))


# Top-level targets
clementine-build-deps: dlfcn boost qt taglib liblastfm \
                       glew gstreamer win7sdk chromaprint \
                       protobuf spotify fftw sparsehash
clementine-gst-plugins: gst-plugins-base gst-plugins-good gst-plugins-bad \
                        gst-plugins-ugly gst-libav

clementine-deps: clementine-build-deps clementine-gst-plugins openssl glibnetworking
	-rm -rf clementine-deps
	mkdir -p clementine-deps/gio-modules clementine-deps/gstreamer-plugins
	mkdir -p clementine-deps/platforms clementine-deps/styles clementine-deps/imageformats
	mkdir -p clementine-deps/nsisplugins
	cp -v $(prefix)/plugins/platforms/qwindows.dll clementine-deps/platforms/ || exit 1
	cp -v $(prefix)/plugins/styles/qwindowsvistastyle.dll clementine-deps/styles/ || exit 1
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

	cp -vr /usr/lib/gcc/$(host)/*-posix/libstdc++-6.dll clementine-deps/
	cp -vr /usr/lib/gcc/$(host)/*-posix/libgcc_s_sjlj-1.dll clementine-deps/
	cp -vr /usr/$(host)/lib/libwinpthread-1.dll clementine-deps/

	# openSUSE
	#cp -vr /usr/$(host)/sys-root/mingw/bin/libstdc++-6.dll clementine-deps/
	#cp -vr /usr/$(host)/sys-root/mingw/bin/libgcc_s_sjlj-1.dll clementine-deps/
	#cp -vr /usr/$(host)/sys-root/mingw/bin/libwinpthread-1.dll clementine-deps/

	cp ../nsisplugins/* clementine-deps/nsisplugins/

	for f in `find clementine-deps/ -name '*.dll' $(dont_strip)`; do \
		$(host)-strip -v $$f; \
	done


# The actual commands for compiling each package follow

.done-liblastfm: .done-qt
	$(call extractpkg,$(lastfmtgz))
	-mkdir $(lastfm)/bin
	cd $(lastfm)/bin && $(cmake) -DBUILD_WITH_QT4=OFF -DBUILD_FINGERPRINT=OFF -DBUILD_TESTS=OFF
	cd $(lastfm)/bin && $(make)
	cd $(lastfm)/bin && make install DESTDIR=$(stow)/$(lastfm)
	cd $(lastfm)/bin && mv -fv $(stow)/$(lastfm)$(prefix)/* $(stow)/$(lastfm)
	cd $(stow) && stow -R $(lastfm)
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
	$(call buildpkg,$(gettext))
	$(call installpkg,$(gettext))

.done-pcre:
	$(call extractpkg,$(pcretgz))
	cd $(pcre) && $(configure) --enable-shared --disable-static --enable-pcre16 --enable-utf --enable-unicode-properties --enable-cpp --disable-pcregrep-libz --disable-pcregrep-libbz2 --disable-pcretest-libreadline
	cd $(pcre) && $(make)
	rm -rf $(stow)/$(pcre)
	cd $(pcre) && make install DESTDIR=$(stow)/$(pcre)
	mv -fv $(stow)/$(pcre)$(prefix)/* $(stow)/$(pcre)/
	cd $(stow) && stow -R $(pcre) && touch $(work)/$@
	touch $@

.done-glib: .done-zlib .done-gettext .done-ffi .done-pcre
	$(call extractpkg,$(glibtgz))
	cd $(glib) && meson --prefix=$(prefix) --cross-file ../cross-file.txt _build
	cd $(glib) && ninja -C _build
	$(call installpkgmeson,$(glib))

.done-gmp:
	rm -f $(prefix)/share/info/dir
	$(call extractpkg,$(gmptgz))
	cd $(gmp) && $(configure) --enable-shared --disable-static
	cd $(gmp) && $(make)
	$(call installpkg,$(gmp))

.done-nettle: .done-gmp
	rm -f $(prefix)/share/info/dir
	$(call extractpkg,$(nettletgz))
	cd $(nettle) && $(configure)
	cd $(nettle) && $(make)
	$(call installpkg,$(nettle))

.done-libgpgerror:
	rm -f $(prefix)/share/info/dir
	$(call extractandbuild,$(gpgerrortgz),$(gpgerror))

.done-gcrypt: .done-libgpgerror .done-gettext
	rm -f $(prefix)/share/info/dir
	$(call extractpkg,$(gcrypttgz))
	cd $(gcrypt) && $(configure) --with-gpg-error-prefix=$(prefix)
	cd $(gcrypt) && $(make)
	$(call installpkg,$(gcrypt))

.done-libtasn1:
	rm -f $(prefix)/share/info/dir
	$(call extractpkg,$(tasn1tgz))
	cd $(tasn1) && $(configure) --disable-gcc-warnings
	cd $(tasn1) && $(make)
	$(call installpkg,$(tasn1))

.done-libgnutls: .done-gcrypt .done-libtasn1 .done-nettle .done-unistring .done-gmp .done-p11kit
	$(call extractpkg,$(gnutlstgz))
	cd $(gnutls) && patch -p1 < ../patches/gnutls-1-fixes.patch
	cd $(gnutls) && $(configure) --disable-rpath --disable-nls --disable-guile --disable-doc --disable-tests --disable-silent-rules --enable-local-libopts CFLAGS='$(cflags) -D_WIN32_WINNT=0x0600'
	cd $(gnutls) && $(make)
	$(call installpkg,$(gnutls))

.done-win7sdk:
	cp -r $(src)/$(win7sdk) $(stow)/
	cd $(stow) && stow $(win7sdk)
	touch $@

.done-sqlite:
	$(call extractpkg,$(sqlitetgz),$(sqlite))
	# libtool dont like "-L$(prefix)/lib".
	cd $(sqlite) && $(pkgconfig) LDFLAGS="-lpthread" CFLAGS="$(cflags)" CXXFLAGS="$(cxxflags)" ./configure --host=$(host) --build=$(build) --prefix=$(prefix) --enable-shared --disable-static --enable-threadsafe --disable-readline
	cd $(sqlite) && $(make)
	$(call installpkg,$(sqlite))

.done-libxml: .done-iconv
	$(call extractpkg,$(xmltgz))
	cd $(xml) && $(configure) --without-python
	cd $(xml) && $(make)
	$(call installpkg,$(xml))

.done-glibnetworking: .done-glib .done-libgnutls
	$(call extractpkg,$(glibnetworkingtgz),$(glibnetworking))
	cd $(glibnetworking) && $(configure) --without-ca-certificates
	cd $(glibnetworking) && $(make)
	$(call installpkg,$(glibnetworking))

.done-libsoup: .done-glib .done-libxml .done-psl .done-libgnutls
	$(call extractpkg,$(souptgz))
	cd $(soup) && patch -p0 < ../patches/libsoup-01-winsock.patch
	(cd $(soup) && $(configure) && $(make))
	$(call installpkg,$(soup))
	touch $@

.done-gstreamer: .done-glib .done-libxml .done-orc
	$(call extractpkg,$(gsttgz))
	cd $(gst) && patch -p1 < ../patches/gstreamer-1-fixes.patch
	cd $(gst) && $(configure) CFLAGS="$(cflags) -DHAVE_PTHREAD" --disable-examples --disable-tests
	cd $(gst) && $(make)
	$(call installpkg,$(gst))

.done-gst-plugins-base: .done-gstreamer .done-ogg .done-vorbis .done-opus
	$(call extractpkg,$(gstbasetgz))
	cd $(gstbase) && patch -p1 < ../patches/gst-plugins-base-1-fixes.patch
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

.done-gst-plugins-good: .done-gstreamer .done-gst-plugins-base .done-flac .done-speex .done-libsoup .done-wavpack .done-lame
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

.done-flac: .done-ogg
	$(call extractpkg,$(flactgz))
	cd $(flac) && $(configure) --disable-sse --disable-avx --disable-asm-optimizations
	cd $(flac) && $(make) LDFLAGS='-fstack-protector'
	$(call installpkg,$(flac))

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

.done-gst-plugins-ugly: .done-gstreamer .done-gst-plugins-base .done-oil .done-cdio
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

.done-lame:
	$(call extractpkg,$(lametgz))
	cd $(lame) && patch -p1 < ../patches/lame-1-fixes.patch
	cd $(lame) && $(pkgconfig) LDFLAGS="$(ldflags)" CFLAGS="$(cflags) -march=native" CXXFLAGS="$(cxxflags)" ./configure --host=$(host) --build=$(build) --prefix=$(prefix) --disable-frontend --disable-gtktest
	$(call installpkg,$(lame))

.done-gst-plugins-bad: .done-gstreamer .done-gst-plugins-base .done-faad .done-libmms .done-oil .done-libmpcdec
	$(call extractpkg,$(gstbadtgz))
	cd $(gstbad) && patch -p1 < ../patches/gst-plugins-bad-1-fixes.patch
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
	cd $(faad) && patch -p1 < ../patches/faad2-1-fixes.patch
	cd $(faad) && $(configure)
	cd $(faad) && $(make)
	rm -rf $(stow)/$(faad)
	cd $(faad) && make install DESTDIR=$(stow)/$(faad)
	mv -fv $(stow)/$(faad)$(prefix)/* $(stow)/$(faad)/
	cd $(stow) && stow -R $(faad)
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

.done-dlfcn:
	-mkdir $(stow)/$(dlfcn)/
	tar -xjf $(dlfcntgz) -C $(stow)/$(dlfcn)/
	cd $(stow) && stow -R $(dlfcn)
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
	 cd $(qt) && ./configure \
		-I/target/include \
		-release \
		-xplatform win32-g++ \
		-device-option CROSS_COMPILE=/usr/bin/x86_64-w64-mingw32- \
		-prefix $(stow)/$(qt) \
		-confirm-license \
		-opensource \
		-no-compile-examples \
		-opengl desktop \
		-no-dbus \
		-openssl-runtime \
		-skip qt3d \
		-skip qtactiveqt \
		-skip qtandroidextras \
		-skip qtcanvas3d \
		-skip qtcharts \
		-skip qtconnectivity \
		-skip qtdatavis3d \
		-skip qtdeclarative \
		-skip qtdoc \
		-skip qtgamepad \
		-skip qtgraphicaleffects \
		-skip qtlocation \
		-skip qtmacextras \
		-skip qtmultimedia \
		-skip qtpurchasing \
		-skip qtquickcontrols \
		-skip qtquickcontrols2 \
		-skip qtremoteobjects \
		-skip qtscript \
		-skip qtscxml \
		-skip qtsensors \
		-skip qtserialbus \
		-skip qtspeech \
		-skip qttranslations \
		-skip qtvirtualkeyboard \
		-skip qtwayland \
		-skip qtwebchannel \
		-skip qtwebengine \
		-skip qtwebglplugin \
		-skip qtwebsockets \
		-skip qtwebview \
		-skip qtx11extras
	cd $(qt) && $(make)
	cd $(qt) && make install
	cd $(stow) && stow -R $(qt)
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

.done-curl:
	$(call extractandbuild,$(curltgz),$(curl))

.done-fftw:
	rm -f $(prefix)/share/info/dir
	$(call extractpkg,$(fftwtgz))
	cd $(fftw) && $(configure) \
		--with-our-malloc16 --with-windows-f77-mangling --enable-shared \
		--disable-static --enable-threads --with-combined-threads \
		--enable-portable-binary
	cd $(fftw) && $(make)
	$(call installpkg,$(fftw))

.done-protobuf:
	$(call extractpkg,$(protobuftgz))
	cd $(protobuf) && $(configure) --with-protoc=/usr/bin/protoc CXXFLAGS="$(cxxflags) --std=c++14"
	cd $(protobuf) && $(make)
	$(call installpkg,$(protobuf))

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

.done-openssl: .done-zlib
	$(call extractpkg,$(openssltgz))
	cd $(openssl) && ./Configure \
		zlib \
		--cross-compile-prefix="$(host)-" \
		--prefix=$(stow)/$(openssl) \
		--shared \
		mingw64 \
		LDFLAGS="-L/target/bin $(ldflags)" CFLAGS="$(cflags)"
	cd $(openssl) && make
	cd $(openssl) && make install
	cd $(stow) && stow -R $(openssl)
	touch $@

.done-sparsehash:
	$(call extractandbuild,$(sparsehashtgz),$(sparsehash))

.done-ffi:
	rm -f $(prefix)/share/info/dir
	$(call extractandbuild,$(ffitgz),$(ffi))

.done-opus:
	$(call extractpkg,$(opustgz))
	cd $(opus) && $(configure)
	cd $(opus) && $(make) LDFLAGS='-fstack-protector'
	$(call installpkg,$(opus))

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

.done-p11kit: .done-libtasn1 .done-ffi
	$(call extractandbuild,$(p11kittgz),$(p11kit))

.done-psl:
	$(call extractpkg,$(psltgz))
	cd $(psl) && LDFLAGS="$(ldflags) -lws2_32" CFLAGS="$(cflags)" CXXFLAGS="$(cxxflags)" ./configure --host=$(host) --build=$(build) --prefix=$(prefix)
	cd $(psl) && $(make)
	$(call installpkg,$(psl))

.done-unistring: .done-iconv
	rm -f $(prefix)/share/info/dir
	$(call extractpkg,$(unistringtgz))
	cd $(unistring) && $(configure) --enable-threads
	cd $(unistring) && $(make)
	$(call installpkg,$(unistring))
