# Target compiler
host=i586-mingw32msvc

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
clementine_dlls=QtCore4.dll \
                QtGui4.dll \
                QtNetwork4.dll \
                QtOpenGL4.dll \
                QtSql4.dll \
                QtXml4.dll \
                avcodec-52.dll \
                avformat-52.dll \
                avutil-50.dll \
                glew32.dll \
                intl.dll \
                libarchive.dll \
                libexpat-1.dll \
                libfaac.dll \
                libfaad.dll \
                libfftw3-3.dll \
                libFLAC.dll \
                libgcc_s_dw2-1.dll \
                libgcrypt-11.dll \
                libgdk_pixbuf-2.0-0.dll \
                libgio-2.0-0.dll \
                libglib-2.0-0.dll \
                libgmodule-2.0-0.dll \
                libgnutls-26.dll \
                libgobject-2.0-0.dll \
                libgpg-error-0.dll \
                libgstaudio-0.10-0.dll \
                libgstbase-0.10-0.dll \
                libgstcontroller-0.10-0.dll \
                libgstfft-0.10-0.dll \
                libgstinterfaces-0.10-0.dll \
                libgstnet-0.10-0.dll \
                libgstnetbuffer-0.10-0.dll \
                libgstpbutils-0.10-0.dll \
                libgstreamer-0.10-0.dll \
                libgstriff-0.10-0.dll \
                libgstrtp-0.10-0.dll \
                libgstrtsp-0.10-0.dll \
                libgstsdp-0.10-0.dll \
                libgsttag-0.10-0.dll \
                libgthread-2.0-0.dll \
                libid3tag.dll \
                libimobiledevice-1.dll \
                liblastfm.dll \
                libmad.dll \
                libmms-0.dll \
                libmp3lame-0.dll \
                libofa.dll \
                libogg-0.dll \
                liboil-0.3-0.dll \
                liborc-0.4-0.dll \
                liborc-test-0.4-0.dll \
                libplist.dll \
                libpng14-14.dll \
                libprotobuf-lite-7.dll \
                libsoup-2.4-1.dll \
                libspeex-1.dll \
                libspotify.dll \
                libtag.dll \
                libtasn1-3.dll \
                libusbmuxd.dll \
                libvorbis-0.dll \
                libvorbisenc-2.dll \
                libxml2-2.dll \
                pthreadGC2.dll \
                python27.dll \
                zlib1.dll
clementine_gst_plugins=libgstapetag.dll \
                       libgstasf.dll \
                       libgstaudioconvert.dll \
                       libgstaudiofx.dll \
                       libgstaudioresample.dll \
                       libgstaudiotestsrc.dll \
                       libgstautodetect.dll \
                       libgstcoreelements.dll \
                       libgstdecodebin2.dll \
                       libgstdirectsoundsink.dll \
                       libgstequalizer.dll \
                       libgstfaac.dll \
                       libgstfaad.dll \
                       libgstffmpeg.dll \
                       libgstflac.dll \
                       libgstgio.dll \
                       libgsticydemux.dll \
                       libgstid3demux.dll \
                       libgstlame.dll \
                       libgstmad.dll \
                       libgstmms.dll \
                       libgstmpegaudioparse.dll \
                       libgstmusepack.dll \
                       libgstofa.dll \
                       libgstogg.dll \
                       libgstqtdemux.dll \
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
dont_strip=-not -name glew32.dll -not -name zlib1.dll -not -name libspotify.dll -not -name python27.dll

# Useful macros for building packages
pkgconfig=PKG_CONFIG_LIBDIR=$(prefix)/lib/pkgconfig
configure=$(pkgconfig) ./configure --host=$(host) --build=$(build) --prefix=$(prefix)
cmake=$(pkgconfig) cmake .. -DCMAKE_TOOLCHAIN_FILE=$(src)/Toolchain-mingw32.cmake -DCMAKE_INSTALL_PREFIX=$(prefix)
make=make $(jobs)
extractpkg=tar -xvf $(1)
buildpkg=(cd $(1) && $(configure) && $(make))
installpkg=rm -rf $(stow)/$(1) && \
	cd $(1) && \
	make install DESTDIR=$(stow)/$(1) && \
	mv -fv $(stow)/$(1)$(prefix)/* $(stow)/$(1)/ && \
	cd $(stow) && \
	stow -R $(1) && \
	touch $(work)/$@

extractandbuild=$(call extractpkg,$(1)) && $(call buildpkg,$(2)) && $(call installpkg,$(2))


# Top-level targets
clementine-build-deps: dlfcn boost liblastfm qt taglib libimobiledevice gtk \
                       libgpod pyqt glew gstreamer win7sdk wmdm qtsparkle \
                       libarchive protobuf spotify
clementine-gst-plugins: gst-plugins-base gst-plugins-good gst-plugins-bad \
                        gst-plugins-ugly gst-ffmpeg

clementine-deps: clementine-build-deps clementine-gst-plugins
	-rm -rf clementine-deps
	mkdir -p clementine-deps/gstreamer-plugins
	mkdir -p clementine-deps/imageformats
	mkdir -p clementine-deps/nsisplugins
	for f in $(clementine_dlls); do \
		cp -v $(prefix)/bin/$$f clementine-deps/ || exit 1; \
	done
	for f in $(clementine_gst_plugins); do \
		cp -v $(prefix)/lib/gstreamer-0.10/$$f clementine-deps/gstreamer-plugins || exit 1; \
	done
	for f in $(clementine_imageformats); do \
		cp -v $(prefix)/plugins/imageformats/$$f clementine-deps/imageformats || exit 1; \
	done
	cp -vr $(src)/mingwm10.dll $(src)/nsisplugins clementine-deps/
	cp -vr /usr/lib/gcc/$(host)/*/libgcc_sjlj_1.dll clementine-deps/
	for f in `find clementine-deps/ -name '*.dll' $(dont_strip)`; do \
		i586-mingw32msvc-strip -v $$f; \
	done
	cp -vrL $(prefix)/DLLs clementine-deps/
	cp -vrL $(prefix)/Python27.zip clementine-deps/


# The actual commands for compiling each package follow

.done-gtk:
	unzip -o -d $(stow)/$(gtk) $(gtkzip)
	sed -i.bak -e's/^prefix=.*/prefix=\$(prefix)/' $(stow)/$(gtk)/lib/pkgconfig/*.pc
	cd $(stow) && stow $(gtk)
	touch $@

.done-win7sdk:
	cp -r $(src)/$(win7sdk) $(stow)/
	cd $(stow) && stow $(win7sdk)
	touch $@

.done-sqlite:
	$(call extractandbuild,$(sqlitetgz),$(sqlite))

.done-libxml:
	unzip -o -d $(stow)/$(xml) $(xmlzip)
	unzip -o -d $(stow)/$(xml) $(xmldevzip)
	sed -i.bak -e's/^prefix=.*/prefix=\$(prefix)/' $(stow)/$(xml)/lib/pkgconfig/*.pc
	cd $(stow) && stow $(xml)
	touch $@

.done-libsoup:
	unzip -o -d $(stow)/$(soup) $(soupzip)
	unzip -o -d $(stow)/$(soup) $(soupdevzip)
	sed -i.bak -e's/^prefix=.*/prefix=\$(prefix)/' $(stow)/$(soup)/lib/pkgconfig/*.pc
	cd $(stow) && stow $(soup)
	touch $@

.done-libplist: .done-libxml .done-gtk
	tar -xzf $(plisttgz)
	-mkdir $(plist)/build
	cd $(plist) && patch -p0 < ../patches/libplist-01-winsock.patch
	cd $(plist)/build && $(cmake)
	cd $(plist)/build && $(make)
	rm -rf $(stow)/$(plist)
	cd $(plist)/build && make install DESTDIR=$(stow)/$(plist)
	mv -fv $(stow)/$(plist)$(prefix)/* $(stow)/$(plist)/
	cd $(stow) && stow $(plist)
	touch $@

.done-libgpod: .done-sqlite .done-libplist
	$(call extractpkg,$(gpodtgz))
	cd $(gpod) && patch -p0 < ../patches/libgpod-01-nousb.patch
	cd $(gpod) && autoreconf
	$(call buildpkg,$(gpod))
	$(call installpkg,$(gpod))

.done-gstreamer: .done-gtk .done-libxml .done-orc
	$(call extractpkg,$(gsttgz))
	cd $(gst) && $(configure) --disable-examples --disable-tests
	cd $(gst) && $(make)
	$(call installpkg,$(gst))

.done-gst-plugins-base: .done-gstreamer .done-ogg .done-vorbis
	$(call extractpkg,$(gstbasetgz))
	cd $(gstbase) && patch -p1 < ../patches/gst-plugins-base-01-tcp.patch
	cd $(gstbase) && patch -p1 < ../patches/gst-plugins-base-02-tcp-no-gdp.patch
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

.done-gst-plugins-good: .done-gstreamer .done-gst-plugins-base .done-flac .done-speex .done-libsoup .done-directx .done-wavpack
	$(call extractpkg,$(gstgoodtgz))
	cd $(gstgood) && patch -p0 < ../patches/gst-plugins-good-01-directsound.patch
	cd $(gstgood) && $(configure) --disable-shout2 --disable-examples --disable-x 
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

.done-directx:
	tar -xzf $(directxtgz) -C $(stow)
	cd $(stow) && stow -R $(directx)
	touch $@

.done-gst-plugins-ugly: .done-gstreamer .done-gst-plugins-base .done-oil .done-mad .done-lame
	$(call extractpkg,$(gstuglytgz))
	cd $(gstugly) && LDFLAGS="-L$(prefix)/bin" \
	                 $(configure) --disable-examples --disable-x 
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
		-version-info 3:0:3 *.lo -lz

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
	$(call buildpkg,$(mad))

	# libtool is retarded and doesn't link this dll properly
	cd $(mad) && /bin/bash ./libtool --mode=link $(host)-gcc \
		-Wall -march=i486 -g -O -fforce-mem -fforce-addr -fthread-jumps \
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

.done-gst-plugins-bad: .done-gstreamer .done-gst-plugins-base .done-faad .done-faac .done-libmms .done-oil .done-ofa .done-libmpcdec
	$(call extractpkg,$(gstbadtgz))
	cd $(gstbad) && patch -p0 < ../patches/gst-plugins-bad-01-librfb-winsock.patch
	cd $(gstbad) && LDFLAGS="-L$(prefix)/bin" $(configure) --disable-acm --disable-examples --disable-x
	sed -i.bak 's/$$ECHO "$$win32_libid_type"/$$ECHO "x86 DLL"/' $(gstbad)/libtool
	cd $(gstbad) && $(make)
	$(call installpkg,$(gstbad))

.done-gst-ffmpeg: .done-gstreamer .done-gst-plugins-base
	$(call extractpkg,$(gstffmpegtgz))
	cd $(gstffmpeg) && patch -p1 < ../patches/gst-ffmpeg-01-off_t.patch
	cd $(gstffmpeg) && patch -p1 < ../patches/gst-ffmpeg-02-dlls.patch
	cd $(gstffmpeg) && patch -p0 < ../patches/gst-ffmpeg-03-no-missing-prototypes.patch
	cd $(gstffmpeg) && autoreconf
	cd $(gstffmpeg) && $(configure) --with-ffmpeg-extra-configure="--enable-shared --disable-debug"
	cd $(gstffmpeg) && $(make)
	rm -rf $(stow)/$(gstffmpeg)
	cd $(gstffmpeg) && make install DESTDIR=$(stow)/$(gstffmpeg)
	mv -fv $(stow)/$(gstffmpeg)$(prefix)/* $(stow)/$(gstffmpeg)/
	-mkdir $(stow)/$(gstffmpeg)/bin/
	cp $(gstffmpeg)/gst-libs/ext/ffmpeg/lib*/*.dll* $(stow)/$(gstffmpeg)/bin/
	cd $(stow) && stow -R $(gstffmpeg)
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

.done-libmms: .done-gtk
	$(call extractpkg,$(mmswin32tgz))
	cd $(mmswin32) && ./autogen.sh
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

.done-usbmuxd: .done-usb .done-pthreads .done-libplist
	$(call extractpkg,$(usbmuxdtgz))
	-cd $(usbmuxd) && mkdir build
	patch -d $(usbmuxd) -p0 < patches/usbmuxd-02-errno.patch
	patch -d $(usbmuxd) -p0 < patches/usbmuxd-03-pthreads.patch
	patch -d $(usbmuxd) -p0 < patches/usbmuxd-04-notools.patch
	cd $(usbmuxd)/build && $(cmake)
	cd $(usbmuxd)/build && $(make)
	rm -rf $(stow)/$(usbmuxd)
	cd $(usbmuxd)/build && make install DESTDIR=$(stow)/$(usbmuxd)
	mv -fv $(stow)/$(usbmuxd)$(prefix)/* $(stow)/$(usbmuxd)/
	cd $(stow) && stow $(usbmuxd)
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
	cd $(stow) && stow $(pthreads)
	touch $@

.done-libimobiledevice: .done-usbmuxd .done-libgnutls .done-libplist
	$(call extractpkg,$(imobtgz))
	patch -d $(imob) -p0 < patches/libimobiledevice-02-sleep.patch
	patch -d $(imob) -p0 < patches/libimobiledevice-03-asprintf.patch
	patch -d $(imob) -p0 < patches/libimobiledevice-04-userpref-stdint.patch
	patch -d $(imob) -p0 < patches/libimobiledevice-05-no-tools.patch
	cd $(imob) && $(configure) --without-swig
	cd $(imob) && $(make)
	$(call installpkg,$(imob))

.done-libgnutls:
	unzip -o -d $(stow)/$(tls) $(tlszip)
	cd $(stow) && stow $(tls)
	touch $@

.done-taglib:
	$(call extractpkg,$(taglibtgz))
	-mkdir $(taglib)/build
	patch -d $(taglib) -p0 < patches/taglib-01-pkgconfig.patch
	cd $(taglib)/build && $(cmake) -DWITH_ASF=ON -DWITH_MP4=ON
	cd $(taglib)/build && $(make)
	rm -rf $(stow)/$(taglib)
	cd $(taglib)/build && make install DESTDIR=$(stow)/$(taglib)
	cd $(taglib)/build && mv -fv $(stow)/$(taglib)$(prefix)/* $(stow)/$(taglib)
	cd $(stow) && stow -R $(taglib)
	touch $@

.done-qt:
	tar -xf $(qttgz) -C $(stow)
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

.done-wmdm:
	tar -xf $(wmdmtgz) -C $(stow)
	cd $(stow) && stow -R $(wmdm)
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

.done-python:
	-rm -rf $(pythonwin32)
	unzip -o $(pythonwin32zip)

	# Compile python libraries
	mv $(pythonwin32)/Lib/site-packages/* $(pythonwin32)/Lib/
	cd $(pythonwin32) && wine python.exe -m compileall -f Lib || true

	# Move sip and pyqt out of site-packages
	mkdir $(pythonwin32)/DLLs/PyQt4
	mv $(pythonwin32)/Lib/PyQt4/*.pyc $(pythonwin32)/DLLs/PyQt4/
	mv $(pythonwin32)/Lib/PyQt4/*.pyd $(pythonwin32)/DLLs/PyQt4/
	mv $(pythonwin32)/Lib/PyQt4/uic   $(pythonwin32)/DLLs/PyQt4/
	find $(pythonwin32)/DLLs -name '*.py' -delete
	mv $(pythonwin32)/Lib/sip.pyd $(pythonwin32)/DLLs/
	mkdir -p $(pythonwin32)/share/sip
	mv $(pythonwin32)/sip/PyQt4 $(pythonwin32)/share/sip/

	# Make a zip with all the pyc files
	cd $(pythonwin32)/Lib && \
		find -name test -prune \
		 -or -name distutils -prune \
		 -or -name idlelib -prune \
		 -or -name lib2to3 -prune \
		 -or -name lib-tk -prune \
		 -or -name pydoc_data -prune \
		 -or -name PyQt4 -prune \
		 -or -not -name '*.py' \
		     -not -name pydoc.pyc \
		     -not -name doctest.pyc | zip ../Python27.zip -@
	cd $(pythonwin32)/Lib && zip ../Python27.zip os.py

	# Rearrange directory structure to be more unixey
	mkdir $(pythonwin32)/bin
	mkdir $(pythonwin32)/lib
	mv $(pythonwin32)/python27.dll $(pythonwin32)/bin/
	mv $(pythonwin32)/libs/* $(pythonwin32)/lib/
	rmdir $(pythonwin32)/libs
	rm $(pythonwin32)/*.exe
	rm $(pythonwin32)/*.txt
	rm -rf $(pythonwin32)/Lib

	-rm -rf $(stow)/$(pythonwin32)
	cp -r $(pythonwin32) $(stow)
	cd $(stow) && stow $(pythonwin32)
	touch $@

.done-sip: .done-python
	$(call extractpkg,$(siptgz))
	cd $(sip) && python configure.py --bindir /bin \
		LFLAGS+=-m32 CFLAGS+=-m32 CXXFLAGS+=-m32
	cd $(sip)/sipgen && $(make)
	rm -rf $(stow)/$(sip)
	cd $(sip)/sipgen && make install DESTDIR=$(stow)/$(sip)
	cd $(stow) && stow -R $(sip)
	touch $@

.done-ofa: .done-curl .done-fftw
	$(call extractpkg,$(ofatgz))
	cd $(ofa) && patch -p0 < ../patches/libofa-01-math-utils.patch
	cd $(ofa) && $(configure)
	cd $(ofa) && cp config.h config_win32.h
	cd $(ofa) && $(make)

	# libtool is retarded and doesn't link this dll properly
	cd $(ofa)/lib && /bin/bash ../libtool --mode=link i586-mingw32msvc-g++  \
		-g -O2 -Wall -o libofa.dll --shared  fftlibw3_op.lo fft_op.lo \
		frametracker_op.lo mainprint.lo signal_op.lo trackdata_op.lo \
		trackframe_op.lo tracklist_op.lo AFLIB/libaflib.la -lm -lfftw3
	
	rm -rf $(stow)/$(ofa)
	cd $(ofa) && make install DESTDIR=$(stow)/$(ofa)
	mv -fv $(stow)/$(ofa)$(prefix)/* $(stow)/$(ofa)/
	-mkdir $(stow)/$(ofa)/bin/
	cp $(ofa)/lib/libofa.dll $(stow)/$(ofa)/bin/
	rm -f $(stow)/$(ofa)/lib/libofa.*
	sed -i.bak -e's/\/lib/\/bin/' $(stow)/$(ofa)/lib/pkgconfig/*.pc
	cd $(stow) && stow -R $(ofa)
	touch $@

.done-curl:
	$(call extractandbuild,$(curltgz),$(curl))

.done-fftw:
	$(call extractpkg,$(fftwtgz))
	cd $(fftw) && $(configure) \
		--with-our-malloc16 --with-windows-f77-mangling --enable-shared \
		--disable-static --enable-threads --with-combined-threads \
		--enable-portable-binary --enable-sse2
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
	unzip -o -d $(stow)/$(spotifywin32) $(spotifywin32zip)
	rm -rf $(stow)/$(spotifywin32)/*.txt
	rm -rf $(stow)/$(spotifywin32)/*.xhtml
	rm -rf $(stow)/$(spotifywin32)/images
	rm -rf $(stow)/$(spotifywin32)/examples
	-mkdir $(stow)/$(spotifywin32)/bin
	-mkdir -p $(stow)/$(spotifywin32)/lib/pkgconfig
	mv -v $(stow)/$(spotifywin32)/lib/libspotify.dll $(stow)/$(spotifywin32)/bin/
	cp $(src)/libspotify.pc $(stow)/$(spotifywin32)/lib/pkgconfig
	cd $(stow) && stow $(spotifywin32)
	touch $@
