import argparse
import hashlib
import os
import sys
import urllib

DOWNLOAD_URL = 'https://storage.googleapis.com/clementine-data.appspot.com/Build%20dependencies/'

FILES = [
    # filename, md5sum
    ('boost-1.50.tar.bz2', '5c0fdd406d965855e77f435d63a5d729'),
    ('chromaprint-1.1.tar.gz', '6db0b5240231b7d2e6628f49fc765b4a'),
    ('davidsansome-liblastfm-0.3.1-18-gcce698d.tar.gz',
     '09314a36fef950d5f6602fdca532b566'),
    ('davidsansome-qtsparkle-28721b5.tar.gz',
     '5d41ff15aaa85f43b9611bbf654b519e'),
    ('dlfcn-win32-static-r19.tar.bz2', '2c8d5b7767c2e2e4a38bf6a22364cc00'),
    ('faac-1.28.tar.gz', '80763728d392c7d789cde25614c878f6'),
    ('faad2-2.7.tar.gz', 'ee1b4d67ea2d76ee52c5621bc6dbf61e'),
    ('fftw-3.3.2.tar.gz', '6977ee770ed68c85698c7168ffa6e178'),
    ('flac-1.3.2.tar.xz', '454f1bfa3f93cc708098d7890d0499bd'),
    ('gettext-0.18.3.1.tar.gz', '3fc808f7d25487fc72b5759df7419e02'),
    ('glew-1.5.5-win32.zip', '48c8c982644ba11dfe94aaf756217eec'),
    ('glew-1.5.5.tar.bz2', '25afa3ff4cff7b67add612e148a54240'),
    ('glib-2.42.0.tar.xz', '71af99768063ac24033ac738e2832740'),
    ('glib-networking-2.42.0.tar.xz', 'd1935e6974da7f39d265303c87a8389b'),
    ('gmp-5.1.3.tar.xz', 'e5fe367801ff067b923d1e6a126448aa'),
    ('gnutls-3.4.17.tar.xz', '03ea7575a43f58964635a5064cce4dc0'),
    ('gst-libav-1.8.3.tar.xz', 'b51a736147bacb40f85827a4e0ae0d2c'),
    ('gst-plugins-bad-1.8.3.tar.xz', '955281a43e98c5464563fa049e0a0911'),
    ('gst-plugins-base-1.8.3.tar.xz', '4d03dd81828ea6b98a44c8f1ab7f4976'),
    ('gst-plugins-good-1.8.3.tar.xz', '473ebb1f15c67de99ddb6e4d027c0876'),
    ('gst-plugins-ugly-1.8.3.tar.xz', '4fc66c77253b0ad5ce224bda654b2e7d'),
    ('gstreamer-1.8.3.tar.xz', 'e88dad542df9d986822e982105d2b530'),
    ('lame-3.98.4.tar.gz', '8e9866ad6b570c6c95c8cba48060473f'),
    ('libarchive-2.8.4.tar.gz', '83b237a542f27969a8d68ac217dc3796'),
    ('libcdio-0.93.tar.gz', 'd154476feaac5a7b5f180e83eaf3d689'),
    ('libechonest-2.3.0.tar.gz', 'c0b39c5029809fbbdd0915ec54e732ba'),
    ('libffi-3.0.11.tar.gz', 'f69b9693227d976835b4857b1ba7d0e3'),
    ('libgcrypt-1.6.1.tar.bz2', 'a5a5060dc2f80bcac700ab0236ea47dc'),
    ('libgpg-error-1.25.tar.bz2', 'd9fa545922a5060cbfbd87464bc31686'),
    ('libgpod-0.8.0.3.tar.gz', 'e3633f4ddf1be74cdededb32e2022e2d'),
    ('libiconv-1.14.tar.gz', 'e34509b1623cec449dfeb73d7ce9c6c6'),
    ('libid3tag-0.15.1b.tar.gz', 'e5808ad997ba32c498803822078748c3'),
    ('liblastfm-1.0.9_2.high_sierra.bottle.tar.gz', '763d3b0f4dd8254b908bdb22b7f26635'),
    ('libmad-0.15.1b.tar.gz', '1be543bc30c56fb6bea1d7bf6a64e66c'),
    ('libmms-0.6.2.tar.gz', '9f63aa363deb4874e072a45850161bff'),
    ('libmms-win32.tar.gz', '82c856c6495ca351f6ce99b0b7057901'),
    ('libmpcdec-1.2.6.tar.bz2', '7f7a060e83b4278acf4b77d7a7b9d2c0'),
    ('libmtp-1.1.8.tar.gz', 'f76abc22fdbe96e96f0066e0f2dc0efd'),
    ('libmusicbrainz-2.1.5.tar.gz', 'd5e19bb77edd6ea798ce206bd05ccc5f'),
    ('libogg-1.2.0.tar.gz', 'c95b73759acfc30712beef6ce4e88efa'),
    ('liboil-0.3.17.tar.gz', '47dc734f82faeb2964d97771cfd2e701'),
    ('libplist-1.10.tar.bz2', 'fe642d0c8602d70c408994555c330dd1'),
    ('libproxy-0.4.11.tar.gz', '3cd1ae2a4abecf44b3f24d6639d2cd84'),
    ('libpsl-0.20.2.tar.gz', 'f604f7d30d64bc673870ecf84b860a1e'),
    ('libquicktime-1.1.5.tar.gz', '0fd45b3deff0317c2f85a34b1b106acf'),
    ('libsoup-2.65.1.tar.xz', 'bf90c902e232a9ec99bb2f672993f638'),
    ('libspotify-12.1.45-Darwin-universal.zip',
     '255ae97cb6a108575c66f6fad37a5990'),
    ('libspotify-12.1.45-win32-release.zip',
     '27651f4d0139c8683dd047a25095fc5e'),
    ('libtasn1-4.9.tar.gz', '3018d0f466a32b66dde41bb122e6cab6'),
    ('libtunepimp-0.5.3.tar.gz', '09649f983acef679a548344ba7a9bb2f'),
    ('libusb-1.0.8.tar.bz2', '37d34e6eaa69a4b645a19ff4ca63ceef'),
    ('libusb-win32-bin-1.2.0.0.zip', 'd8e940655e8c43235de9cf979c041bad'),
    ('libvorbis-1.3.6.tar.gz', 'd3190649b26572d44cd1e4f553943b31'),
    ('libxml2-2.9.1.tar.gz', '9c0cfef285d5c4a5c80d00904ddab380'),
    ('nettle-3.3.tar.gz', '10f969f78a463704ae73529978148dbe'),
    ('openssl-1.0.1m.tar.gz', 'd143d1555d842a069cb7cc34ba745a06'),
    ('opus-1.0.2.tar.gz', 'c503ad05a59ddb44deab96204401be03'),
    ('orc-0.4.16.tar.gz', 'e482932e544c847761449b106ecbc483'),
    ('p11-kit-0.23.2.tar.gz', '738af2442331fc22f440df9bee9b062a'),
    ('protobuf-2.6.1.tar.bz2', '11aaac2d704eef8efd1867a807865d85'),
    ('pthreads-win32-2.8.0.tar.gz', '66bba1fc3713f9bf070eca539139def8'),
    ('qjson-0.8.1.tar.gz', '4eef13da988edf8f91c260a3e1baeea9'),
    ('qjson-0.9.0_1.high_sierra.bottle.tar.gz', 'f5bf9443adacbcf1c8e6dd665ce8a8bd'),
    ('qt-everywhere-opensource-src-4.8.3.tar.gz',
     'a663b6c875f8d7caa8ac9c30e4a4ec3b'),
    ('qt-everywhere-opensource-src-4.8.6.tar.gz',
     '2edbe4d6c2eff33ef91732602f3518eb'),
    ('qt5-5.8.0_1.sierra.bottle.tar.gz', '183e8227d5c3c27ca1e287a5318043a5'),
    ('sparsehash-sparsehash-2.0.3.tar.gz', 'd8d5e2538c1c25577b3f066d7a55e99e'),
    ('speex-1.2.0.tar.gz', '8ab7bb2589110dfaf0ed7fa7757dc49c'),
    ('sqlite-amalgamation-3.7.0.tar.gz', '61b85f108760f91b79afc7833e6e6cb4'),
    ('taglib-1.11.tar.gz', 'be39fa2054df40664cb557126ad7cf7c'),
    ('wavpack-4.60.1.tar.bz2', '7bb1528f910e4d0003426c02db856063'),
    ('zlib-1.2.8.tar.gz', '44d667c142d7cda120332623eab69f40'),
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
