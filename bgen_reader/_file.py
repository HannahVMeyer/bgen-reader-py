from __future__ import unicode_literals

from os.path import join, abspath, basename, expanduser, exists, dirname
from os import getcwd, access, W_OK


def find_cache_filepath(bgen_filepath):
    r"""Unobtrusive filepath for cache.

    Get the first existing or writable file path in the following order:
    - ``join(abspath(bgen_filepath), "." + basename(bgen_filepath) + ".idx")``
    - ``join(expanduser('~'), "." + basename(bgen_filepath) + ".idx")``
    - ``join(getcwd(), "." + basename(bgen_filepath) + ".idx")``

    Parameters
    ----------
    bgen_filepath : str
        File path to bgen file.

    Returns
    -------
    str : Found file path; ``None`` otherwise.
    """
    bgen_filepath = _make_sure_unicode(bgen_filepath)
    base = _make_sure_unicode(basename(bgen_filepath))
    name = "." + base + ".idx"
    folders = [abspath(bgen_filepath), expanduser('~'), getcwd()]
    cands = [join(d, name) for d in folders]
    try:
        f = next(x for x in cands if exists(x) or access(dirname(x), W_OK))
    except StopIteration:
        raise FileNotFoundError
    return f


def _make_sure_unicode(s):
    try:
        return s.decode('utf-8')
    except AttributeError:
        pass
    return s
