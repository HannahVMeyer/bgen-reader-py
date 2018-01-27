import bz2
import sys
import os
import tarfile
from tempfile import mkdtemp
import random
import shutil
import hashlib

PY2 = sys.version_info < (3, )

if PY2:
    from urllib import urlretrieve
    from urlparse import urlparse
else:
    from urllib.request import urlretrieve
    from urllib.parse import urlparse


class TmpDir(object):
    def __enter__(self):
        try:
            self.name = mkdtemp()
        except (PermissionError, FileExistsError):
            i = random.randint(0, 999999)
            tmp_name = ".tmp-limix-{}".format(i)
            try:
                os.mkdir(tmp_name)
                self.name = tmp_name
            except (PermissionError, FileExistsError):
                home = os.path.expanduser('~')
                tmp_name = os.path.join(home, tmp_name)
                os.mkdir(tmp_name)
                self.name = tmp_name
        return self.name

    def __exit__(self, *_):
        shutil.rmtree(self.name)


def url_filename(url):
    a = urlparse(url)
    return os.path.basename(a.path)


def download(url, dest=None, verbose=True):
    if dest is None:
        dest = os.getcwd()

    filepath = os.path.join(dest, url_filename(url))
    if os.path.exists(filepath):
        if verbose:
            print("File {} already exists.".format(filepath))
        return

    if verbose:
        print("Downloading {}...".format(url))
    urlretrieve(url, filepath)


def filehash(filepath):
    r"""Compute sha256 from a given file."""
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()

    with open(filepath, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


def extract(filepath, verbose=True):

    if verbose:
        print("Extracting {}...".format(filepath))

    try:
        tar = tarfile.open(filepath)
        tar.extractall()
        tar.close()
        return
    except tarfile.ReadError:
        pass

    filename = os.path.splitext(filepath)[0]

    if os.path.exists(filename):
        if verbose:
            print("File {} already exists.".format(filename))
        return

    with open(filepath, 'rb') as f:
        o = bz2.decompress(f.read())

    with open(filename, 'wb') as f:
        f.write(o)
