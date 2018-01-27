from __future__ import unicode_literals

import os
from os.path import join
import pytest
from numpy import array
from numpy.testing import assert_allclose, assert_equal
from bgen_reader import convert_to_dosage, read_bgen
from ._support import download, url_filename, filehash, TmpDir, extract

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


def _do_bgen_reader(cache):
    folder = os.path.dirname(os.path.abspath(__file__)).encode()
    filepath = os.path.join(folder, b"example.32bits.bgen")
    bgen = read_bgen(filepath, verbose=False, cache=cache)
    variants = bgen['variants']
    samples = bgen['samples']

    assert_equal(variants.loc[0, 'chrom'], '01')
    assert_equal(variants.loc[0, 'id'], 'SNPID_2')
    assert_equal(variants.loc[0, 'nalleles'], 2)
    assert_equal(variants.loc[0, 'allele_ids'], "A,G")
    assert_equal(variants.loc[0, 'pos'], 2000)
    assert_equal(variants.loc[0, 'rsid'], 'RSID_2')

    assert_equal(variants.loc[7, 'chrom'], '01')
    assert_equal(variants.loc[7, 'id'], 'SNPID_9')
    assert_equal(variants.loc[7, 'nalleles'], 2)
    assert_equal(variants.loc[7, 'allele_ids'], "A,G")
    assert_equal(variants.loc[7, 'pos'], 9000)
    assert_equal(variants.loc[7, 'rsid'], 'RSID_9')

    n = variants.shape[0]
    assert_equal(variants.loc[n - 1, 'chrom'], '01')
    assert_equal(variants.loc[n - 1, 'id'], 'SNPID_200')
    assert_equal(variants.loc[n - 1, 'nalleles'], 2)
    assert_equal(variants.loc[n - 1, 'allele_ids'], "A,G")
    assert_equal(variants.loc[n - 1, 'pos'], 100001)
    assert_equal(variants.loc[n - 1, 'rsid'], 'RSID_200')

    assert_equal(samples.loc[0, 'id'], 'sample_001')
    assert_equal(samples.loc[7, 'id'], 'sample_008')

    n = samples.shape[0]
    assert_equal(samples.loc[n - 1, 'id'], 'sample_500')


def test_bgen_reader_without_cache():
    _do_bgen_reader(False)
    _do_bgen_reader(False)


def test_bgen_reader_with_cache():
    _do_bgen_reader(True)
    _do_bgen_reader(True)


def test_bgen_reader_file_notfound():
    folder = os.path.dirname(os.path.abspath(__file__)).encode()
    filepath = os.path.join(folder, b"example.33bits.bgen")
    with pytest.raises(FileNotFoundError):
        read_bgen(filepath, verbose=False)


def test_bgen_reader_convert_to_dosage():
    folder = os.path.dirname(os.path.abspath(__file__)).encode()
    filepath = os.path.join(folder, b"example.32bits.bgen")
    bgen = read_bgen(filepath, verbose=False)
    genotype = bgen['genotype']
    dosage = convert_to_dosage(genotype, verbose=False)
    assert_allclose(dosage[0, 1:3], array([1.93575854, 1.91558579]), rtol=1e-5)


def test_bgen_reader_chr21():
    h = "a66b681bcdad14083c5cc5b603201a3f5934028629bb9d0449a072ce62bf7f77"
    url = "https://s3.eu-west-2.amazonaws.com/bgen-examples/chr21.bgen.bz2"
    with TmpDir() as fld:
        download(url, fld)
        fp = join(fld, url_filename(url))
        if filehash(fp) != h:
            raise RuntimeError("File hash mismatch.")
        extract(fp, verbose=False)
        fp = fp[:-4]
        read_bgen(fp, verbose=True)
