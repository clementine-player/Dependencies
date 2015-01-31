import argparse
import hashlib
import os
import sys
import urllib


DOWNLOAD_URL = 'https://googledrive.com/host/%s/%s'
FOLDER_ID = '0Byds9jlkR0IxbXVUa1Flb3h6bjQ'
FILES = [
    # filename, md5sum
    ('boost-1.50.tar.bz2', '5c0fdd406d965855e77f435d63a5d729'),
    ('davidsansome-qtsparkle-28721b5.tar.gz', '5d41ff15aaa85f43b9611bbf654b519e'),
    ('dlfcn-win32-static-r19.tar.bz2', '2c8d5b7767c2e2e4a38bf6a22364cc00'),
    ('faac-1.28.tar.gz', '80763728d392c7d789cde25614c878f6'),
    ('faad2-2.7.tar.gz', 'ee1b4d67ea2d76ee52c5621bc6dbf61e'),
    ('fftw-3.3.2.tar.gz', '6977ee770ed68c85698c7168ffa6e178'),
    ('flac-1.2.1.tar.gz', '153c8b15a54da428d1f0fadc756c22c7'),
    ('gettext-0.18.3.1.tar.gz', '3fc808f7d25487fc72b5759df7419e02'),
    ('glew-1.5.5-win32.zip', '48c8c982644ba11dfe94aaf756217eec'),
    ('glew-1.5.5.tar.bz2', '25afa3ff4cff7b67add612e148a54240'),
    ('glib-2.42.0.tar.xz', '71af99768063ac24033ac738e2832740'),
    ('glib-networking-2.42.0.tar.xz', 'd1935e6974da7f39d265303c87a8389b'),
    ('gmp-5.1.3.tar.xz', 'e5fe367801ff067b923d1e6a126448aa'),
    ('gnutls-3.2.12.tar.xz', 'f507365940de8f095e1d867c6f0842f6'),
    ('gst-libav-1.4.2.tar.xz', '782b250e71616fda12e3e4b2e2d63bb7'),
    ('gst-plugins-bad-1.4.2.tar.xz', 'ac73b4bb0151c05daa566d9d1ec80077'),
    ('gst-plugins-base-1.4.2.tar.xz', '560b43b2be7b9470a6dfcbdc21f882dc'),
    ('gst-plugins-good-1.4.2.tar.xz', '02fc204a20ecd68f76d271eb5cc653c2'),
    ('gst-plugins-ugly-1.4.2.tar.xz', 'f4bc6c20620ad6b265c1c24374aba0f7'),
    ('gstreamer-1.4.2.tar.xz', 'f9970ab3f2537b772074f97ecfb8430c'),
    ('lame-3.98.4.tar.gz', '8e9866ad6b570c6c95c8cba48060473f'),
    ('libarchive-2.8.4.tar.gz', '83b237a542f27969a8d68ac217dc3796'),
    ('libcdio-0.93.tar.gz', 'd154476feaac5a7b5f180e83eaf3d689'),
    ('libffi-3.0.11.tar.gz', 'f69b9693227d976835b4857b1ba7d0e3'),
    ('libgcrypt-1.6.1.tar.bz2', 'a5a5060dc2f80bcac700ab0236ea47dc'),
    ('libgpg-error-1.12.tar.bz2', '8f0eb41a344d19ac2aa9bd101dfb9ce6'),
    ('libgpod-0.8.0.tar.gz', '6660f74cc53293dcc847407aa5f672ce'),
    ('libiconv-1.14.tar.gz', 'e34509b1623cec449dfeb73d7ce9c6c6'),
    ('libid3tag-0.15.1b.tar.gz', 'e5808ad997ba32c498803822078748c3'),
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
    ('libquicktime-1.1.5.tar.gz', '0fd45b3deff0317c2f85a34b1b106acf'),
    ('libsoup-2.48.0.tar.xz', '51ccb76f5262945e1f0316fdc46de567'),
    ('libspotify-12.1.45-Darwin-universal.zip', '255ae97cb6a108575c66f6fad37a5990'),
    ('libspotify-12.1.45-win32-release.zip', '27651f4d0139c8683dd047a25095fc5e'),
    ('libtasn1-3.4.tar.gz', '21ec021c534b0f30b2834ce233c70f15'),
    ('libtunepimp-0.5.3.tar.gz', '09649f983acef679a548344ba7a9bb2f'),
    ('libusb-1.0.8.tar.bz2', '37d34e6eaa69a4b645a19ff4ca63ceef'),
    ('libusb-win32-bin-1.2.0.0.zip', 'd8e940655e8c43235de9cf979c041bad'),
    ('libvorbis-1.3.1.tar.gz', '016e523fac70bdd786258a9d15fd36e9'),
    ('libxml2-2.9.1.tar.gz', '9c0cfef285d5c4a5c80d00904ddab380'),
    ('nettle-2.7.tar.gz', '2caa1bd667c35db71becb93c5d89737f'),
    ('openssl-1.0.1i.tar.gz', 'c8dc151a671b9b92ff3e4c118b174972'),
    ('opus-1.0.2.tar.gz', 'c503ad05a59ddb44deab96204401be03'),
    ('orc-0.4.16.tar.gz', 'e482932e544c847761449b106ecbc483'),
    ('protobuf-2.5.0.tar.bz2', 'a72001a9067a4c2c4e0e836d0f92ece4'),
    ('pthreads-win32-2.8.0.tar.gz', '66bba1fc3713f9bf070eca539139def8'),
    ('qjson-0.7.1.tar.bz2', 'eea7099c762590531b336c4213cb00e7'),
    ('qt-everywhere-opensource-src-4.8.3.tar.gz', 'a663b6c875f8d7caa8ac9c30e4a4ec3b'),
    ('qt-everywhere-opensource-src-4.8.6.tar.gz', '2edbe4d6c2eff33ef91732602f3518eb'),
    ('sparsehash-2.0.2.tar.gz', '1db92ed7f257d9b5f14a309d75e8a1d4'),
    ('speex-1.2rc1.tar.gz', 'c4438b22c08e5811ff10e2b06ee9b9ae'),
    ('sqlite-amalgamation-3.7.0.tar.gz', '61b85f108760f91b79afc7833e6e6cb4'),
    ('taglib-1.9.1.tar.gz', '0d35df96822bbd564c5504cb3c2e4d86'),
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
