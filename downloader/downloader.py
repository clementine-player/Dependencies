import argparse
import hashlib
import os
import sys
import urllib


DOWNLOAD_URL = 'https://googledrive.com/host/%s/%s'
#FOLDER_ID = '0Byds9jlkR0IxbXVUa1Flb3h6bjQ'
FOLDER_ID = '0B2sP0ipqSXQCUC03Z1FvNFhwYUk'
FILES = [
    # filename, md5sum
    ('boost-1.50.tar.bz2', '5c0fdd406d965855e77f435d63a5d729'),
    ('chromaprint-1.3.2.tar.gz', 'cba6ed3209516518d2ecfda887dabdaf'),
    ('davidsansome-liblastfm-0.3.1-17-g6748fcf.tar.gz', 'f8e739e24c91f74fca2d6a67106d8f7a'),
    ('davidsansome-qtsparkle-28721b5.tar.gz', '5d41ff15aaa85f43b9611bbf654b519e'),
    ('dlfcn-win32-static-r19.tar.bz2', '2c8d5b7767c2e2e4a38bf6a22364cc00'),
    ('faac-1.28.tar.gz', '80763728d392c7d789cde25614c878f6'),
    ('faad2-2.7.tar.gz', 'ee1b4d67ea2d76ee52c5621bc6dbf61e'),
    ('fftw-3.3.4.tar.gz', '2edab8c06b24feeb3b82bbb3ebf3e7b3'),
    ('flac-1.3.1.tar.xz', 'b9922c9a0378c88d3e901b234f852698'),
    ('gettext-0.19.8.1.tar.gz', '97e034cf8ce5ba73a28ff6c3c0638092'),
    ('gettext-0.18.3.2.tar.gz', '241aba309d07aa428252c74b40a818ef'),
    ('glew-2.0.0.tgz', '2a2cd7c98f13854d2fcddae0d2b20411'),
    ('glib-2.48.1.tar.xz', '67bd3b75c9f6d5587b457dc01cdcd5bb'),
    ('glib-networking-2.48.2.tar.xz', 'd7cf81d52c856b0c66f7821021f40e08'),
    ('gmp-6.1.1.tar.xz', 'e70e183609244a332d80529e7e155a35'),
    ('gnutls-3.4.9.tar.xz', '1b3b6d55d0e2b6d01a54f53129f1da9b'),
    ('gst-libav-1.8.2.tar.xz', '95bc3dd0ea2dc664b4f3a96897005013'),
    ('gst-plugins-bad-1.8.2.tar.xz', '83abc2e70684e7b195f18ca2992ef6e8'),
    ('gst-plugins-base-1.8.2.tar.xz', 'f55254ca18b845a9a7d8fe671bc09c24'),
    ('gst-plugins-good-1.8.2.tar.xz', '1ad652a98c2106f6d839dfba8d310d23'),
    ('gst-plugins-ugly-1.8.2.tar.xz', 'f781790cf64b44522b01ab560f16d4de'),
    ('gstreamer-1.8.2.tar.xz', '0f011ee793cbcfa96d6b51d8271349fa'),
    ('lame-3.99.5.tar.gz', '84835b313d4a8b68f5349816d33e07ce'),
    ('libarchive-2.8.4.tar.gz', '83b237a542f27969a8d68ac217dc3796'),
    ('libcdio-0.93.tar.gz', 'd154476feaac5a7b5f180e83eaf3d689'),
    ('libechonest-2.3.1.tar.gz', 'c4f84633d9b2dc2097078ccb0e8eb50a'),
    ('libffi-3.2.1.tar.gz', '83b89587607e3eb65c70d361f13bab43'),
    ('libgcrypt-1.7.2.tar.bz2', 'ec7b21dd2134af4b3aece5e5dfd3a700'),
    ('libgpg-error-1.24.tar.bz2', 'feb42198c0aaf3b28eabe8f41a34b983'),
    ('libgpod-0.8.0.3.tar.gz', 'e3633f4ddf1be74cdededb32e2022e2d'),
    ('libiconv-1.14.tar.gz', 'e34509b1623cec449dfeb73d7ce9c6c6'),
    ('libid3tag-0.15.1b.tar.gz', 'e5808ad997ba32c498803822078748c3'),
    ('libmad-0.15.1b.tar.gz', '1be543bc30c56fb6bea1d7bf6a64e66c'),
    ('libmms-0.6.4.tar.gz', 'd6b665b335a6360e000976e770da7691'),
    ('libmms-win32.tar.gz', '82c856c6495ca351f6ce99b0b7057901'),
    ('libmpcdec-1.2.6.tar.bz2', '7f7a060e83b4278acf4b77d7a7b9d2c0'),
    ('libmtp-1.1.11.tar.gz', 'eea14dd30ddd08bbe39cfcb57564a4b8'),
    ('libmusicbrainz-2.1.5.tar.gz', 'd5e19bb77edd6ea798ce206bd05ccc5f'),
    ('libogg-1.3.2.tar.gz', 'b72e1a1dbadff3248e4ed62a4177e937'),
    ('liboil-0.3.17.tar.gz', '47dc734f82faeb2964d97771cfd2e701'),
    ('pcre-8.39.tar.bz2', 'e3fca7650a0556a2647821679d81f585'),
    ('libplist-1.12.tar.bz2', '8b04b0f09f2398022dcd4fba75012997'),
    ('libproxy-0.4.13.tar.gz', 'de293bb311f185a2ffa3492700a694c2'),
    ('libquicktime-1.2.4.tar.gz', '81cfcebad9b7ee7e7cfbefc861d6d61b'),
    ('libsoup-2.54.1.tar.xz', '73b1fb774de16c29b380f87016f9f9dd'),
    ('libspotify-12.1.51-Darwin-universal.zip', '41d019fd85c83ca4c28b823f825a9311'),
    ('libspotify-12.1.51-win32-release.zip', '6f62c551be9d28290fc5adcef7b01496'),
    ('libtasn1-4.9.tar.gz', '3018d0f466a32b66dde41bb122e6cab6'),
    ('libtunepimp-0.5.3.tar.gz', '09649f983acef679a548344ba7a9bb2f'),
    ('libusb-1.0.8.tar.bz2', '37d34e6eaa69a4b645a19ff4ca63ceef'),
    ('libusb-win32-bin-1.2.0.0.zip', 'd8e940655e8c43235de9cf979c041bad'),
    ('libvorbis-1.3.5.tar.gz', '7220e089f3be3412a2317d6fde9e3944'),
    ('libxml2-2.9.1.tar.gz', '9c0cfef285d5c4a5c80d00904ddab380'),
    ('nettle-3.2.tar.gz', 'afb15b4764ebf1b4e6d06c62bd4d29e4'),
    ('openssl-1.0.2h.tar.gz', '9392e65072ce4b614c1392eefc1f23d0'),
    ('opus-1.1.3.tar.gz', '32bbb6b557fe1b6066adc0ae1f08b629'),
    ('orc-0.4.25.tar.xz', '8582a28b15f53110c88d8043d9f55bcf'),
    ('protobuf-2.6.1.tar.gz', 'f3916ce13b7fcb3072a1fa8cf02b2423'),
    ('pthreads-win32-2.8.0.tar.gz', '66bba1fc3713f9bf070eca539139def8'),
    ('qjson-0.8.1.tar.gz', '4eef13da988edf8f91c260a3e1baeea9'),
    ('qt-everywhere-opensource-src-4.8.7.tar.gz', 'd990ee66bf7ab0c785589776f35ba6ad'),
    ('sparsehash-2.0.3.tar.gz', '69d662c690d6c9da82b99cec86357fa1'),
    ('speex-1.2rc1.tar.gz', 'c4438b22c08e5811ff10e2b06ee9b9ae'),
    ('sqlite-amalgamation-3.7.0.tar.gz', '61b85f108760f91b79afc7833e6e6cb4'),
    ('taglib-1.11.tar.gz', 'be39fa2054df40664cb557126ad7cf7c'),
    ('wavpack-4.80.0.tar.bz2', '0f2f1184813dce1caf51b52af615ec17'),
    ('zlib-1.2.8.tar.gz', '44d667c142d7cda120332623eab69f40')
]


def Md5File(path):
  """Returns the MD5 checksum of a file, or None if it doesn't exist."""

  file_hash = hashlib.md5()
  try:
    with open(path) as fh:
      while True:
        chunk = fh.read(4096)
        if len(chunk) == 0:
          break
        file_hash.update(chunk)
  except IOError:
    return None

  return file_hash.hexdigest()


def DownloadFiles(flags):
  # Create the output directory if it doesn't exist.
  base_path = os.path.expanduser(flags.output)
  try:
    os.makedirs(base_path)
  except OSError:
    pass

  for name, md5_checksum in FILES:
    # Get the checksum of the file on disk.
    path = os.path.join(base_path, name)
    actual_md5_checksum = Md5File(path)

    # Download it if the file doesn't exist or if the checksum doesn't match.
    if actual_md5_checksum != md5_checksum:
      url = DOWNLOAD_URL % (FOLDER_ID, name)

      print 'Downloading %s...' % name
      urllib.urlretrieve(url, path)
      actual_md5_checksum = Md5File(path)

    # If the checksum still didn't match the download must have failed.
    if actual_md5_checksum != md5_checksum:
      raise Exception(
          'Download failed - checksums do not match (got %s, expected %s)' % (
              actual_md5_checksum, md5_checksum))

  print 'All files are up-to-date'


def Main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('--output', default='.')
  flags = parser.parse_args(argv[1:])

  DownloadFiles(flags)


if __name__ == '__main__':
  Main(sys.argv)
