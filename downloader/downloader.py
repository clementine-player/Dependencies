import argparse
import hashlib
import os
import sys
import urllib

#DOWNLOAD_URL = 'https://storage.googleapis.com/clementine-data.appspot.com/Build%20dependencies/'
DOWNLOAD_URL = 'https://files.jkvinge.net/packages/clementine-dependencies/'

FILES = [
    # filename, md5sum
    ('boost-1.50.tar.bz2', '5c0fdd406d965855e77f435d63a5d729'),
    ('chromaprint-1.5.0.tar.gz', '77f133f01047c54605e7f2fccd96ff34'),
    ('dlfcn-win32-61ad60f.tar.gz', '99f4512982e24ea6029dd840e81e4aff'),
    ('dlfcn-win32-static-r19.tar.bz2', '2c8d5b7767c2e2e4a38bf6a22364cc00'),
    ('faad2-2.8.8.tar.gz', '28f6116efdbe9378269f8a6221767d1f'),
    ('fftw-3.3.8.tar.gz', '8aac833c943d8e90d51b697b27d4384d'),
    ('flac-1.3.3.tar.xz', '26703ed2858c1fc9ffc05136d13daa69'),
    ('gettext-0.20.2.tar.xz', '0cf5f68338d5d941bbf9ac93b847310f'),
    ('glew-1.5.5.tar.bz2', '25afa3ff4cff7b67add612e148a54240'),
    ('glew-1.5.5-win32.zip', '48c8c982644ba11dfe94aaf756217eec'),
    ('glib-2.58.3.tar.xz', '8058c7bde846dcffe5fa453eca366d73'),
    ('glib-networking-2.54.1.tar.xz', '99867463f182c2767bce0c74bc9cc981'),
    ('gmp-6.2.0.tar.xz', 'a325e3f09e6d91e62101e59f9bda3ec1'),
    ('gnutls-3.6.13.tar.xz', 'bb1fe696a11543433785b4fc70ca225f'),
    ('gst-libav-1.16.2.tar.xz', 'eacebd0136ede3a9bd3672eeb338806b'),
    ('gst-plugins-bad-1.16.2.tar.xz', 'ccc7404230afddec723bbdb63c89feec'),
    ('gst-plugins-base-1.16.2.tar.xz', '3fdb32823535799a748c1fc14f978e2c'),
    ('gst-plugins-good-1.16.2.tar.xz', 'bd025f8f14974f94b75ac69a9d1b9c93'),
    ('gst-plugins-ugly-1.16.2.tar.xz', '10283ff5ef1e34d462dde77042e329bd'),
    ('gstreamer-1.16.2.tar.xz', '0e661ed5bdf1d8996e430228d022628e'),
    ('lame-3.100.tar.gz', '83e260acbe4389b54fe08e0bdbf7cddb'),
    ('libcdio-2.1.0.tar.bz2', 'aa7629e8f73662a762f64c444b901055'),
    ('libffi-3.3.tar.gz', '6313289e32f1d38a9df4770b014a2ca7'),
    ('libgcrypt-1.8.5.tar.bz2', '348cc4601ca34307fc6cd6c945467743'),
    ('libgpg-error-1.38.tar.bz2', 'f164ce3400c820907965fdc53e43acfc'),
    ('libgpod-0.8.0.3.tar.gz', 'e3633f4ddf1be74cdededb32e2022e2d'),
    ('libiconv-1.16.tar.gz', '7d2a800b952942bb2880efb00cfd524c'),
    ('libid3tag-0.15.1b.tar.gz', 'e5808ad997ba32c498803822078748c3'),
    ('liblastfm-1.0.9.tar.gz', '8748f423f66f2fbc38c39f9153d01a71'),
    ('libmms-0.6.2.tar.gz', '9f63aa363deb4874e072a45850161bff'),
    ('libmms-win32.tar.gz', '82c856c6495ca351f6ce99b0b7057901'),
    ('libmpcdec-1.2.6.tar.bz2', '7f7a060e83b4278acf4b77d7a7b9d2c0'),
    ('libmtp-1.1.8.tar.gz', 'f76abc22fdbe96e96f0066e0f2dc0efd'),
    ('libogg-1.3.4.tar.gz', 'b9a66c80bdf45363605e4aa75fa951a8'),
    ('liboil-0.3.17.tar.gz', '47dc734f82faeb2964d97771cfd2e701'),
    ('libplist-2.1.0.tar.gz', '051a93535f3b825eea5cdf284257e16d'),
    ('libpsl-0.21.0.tar.gz', '171e96d887709e36a57f4ee627bf82d2'),
    ('libsoup-2.65.1.tar.xz', 'bf90c902e232a9ec99bb2f672993f638'),
    ('libspotify-12.1.45-Darwin-universal.zip', '255ae97cb6a108575c66f6fad37a5990'),
    ('libspotify-12.1.45-win32-release.zip', '27651f4d0139c8683dd047a25095fc5e'),
    ('libtasn1-4.16.0.tar.gz', '531208de3729d42e2af0a32890f08736'),
    ('libunistring-0.9.10.tar.xz', 'db08bb384e81968957f997ec9808926e'),
    ('libvorbis-1.3.6.tar.gz', 'd3190649b26572d44cd1e4f553943b31'),
    ('libxml2-2.9.10.tar.gz', '10942a1dc23137a8aa07f0639cbfece5'),
    ('nettle-3.6.tar.gz', 'c45ee24ed7361dcda152a035d396fe8a'),
    ('openssl-1.1.1g.tar.gz', '76766e98997660138cdaf13a187bd234'),
    ('opus-1.3.1.tar.gz', 'd7c07db796d21c9cf1861e0c2b0c0617'),
    ('orc-0.4.29.tar.xz', '25799917c7d31a891d5e32b83ad08f6d'),
    ('p11-kit-0.23.20.tar.xz', 'c9b3076475c6a57ca62005c43e77cd64'),
    ('p11-kit-0.23.2.tar.gz', '738af2442331fc22f440df9bee9b062a'),
    ('pcre-8.44.tar.bz2', 'cf7326204cc46c755b5b2608033d9d24'),
    ('protobuf-cpp-3.6.1.tar.gz', '406d5b8636576b1c86730ca5cbd1e576'),
    ('qt-everywhere-src-5.15.0.tar.xz', '610a228dba6ef469d14d145b71ab3b88'),
    ('sparsehash-sparsehash-2.0.3.tar.gz', 'd8d5e2538c1c25577b3f066d7a55e99e'),
    ('speex-1.2.0.tar.gz', '8ab7bb2589110dfaf0ed7fa7757dc49c'),
    ('sqlite-autoconf-3320100.tar.gz', 'bc7afc06f1e30b09ac930957af68d723'),
    ('taglib-47342f6974ac0faccabd8c8b7d00fdfcd483d086.tar.gz', 'd0badb06aeb937ccff269516c92e8c57'),
    ('wavpack-5.3.0.tar.bz2', '77f8fbf9c877a1e4d1178107fbc12450'),
    ('zlib-1.2.11.tar.xz', '85adef240c5f370b308da8c938951a68'),
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
      url = DOWNLOAD_URL + name

      print 'Downloading %s...' % name
      urllib.urlretrieve(url, path)
      actual_md5_checksum = Md5File(path)

    # If the checksum still didn't match the download must have failed.
    if actual_md5_checksum != md5_checksum:
      raise Exception(
          'Download failed - checksums do not match (got %s, expected %s)' %
          (actual_md5_checksum, md5_checksum))

  print 'All files are up-to-date'


def Main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('--output', default='.')
  flags = parser.parse_args(argv[1:])

  DownloadFiles(flags)


if __name__ == '__main__':
  Main(sys.argv)
