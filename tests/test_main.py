"""test main module."""
import unittest
import json
import os
from shutil import copyfile
try:  # py3
    from unittest import mock
except ImportError:  # py2
    import mock

import pytest


@pytest.mark.skip(reason='Invalid ELF Header error.')
def test_import():
    """test import the module.

    error raised because
    test runner disable IO and profile populator require it to run.
    """
    with pytest.raises(IOError):
        import main  # NOQA


@pytest.mark.skip(reason='Invalid ELF Header error.')
def test_import_and_mock_populator():
    """test import the module and mock profile_populator.

    it raise error because no profile is found.
    """
    with mock.patch('melissa.profile_populator.profile_populator'):
        with pytest.raises(IOError):
            from main import main  # NOQA

def test_main():
    """test func."""
    with mock.patch('main.signal') as m_signal, \
            mock.patch('main.subprocess') as m_subprocess, \
            mock.patch('main.load_profile') as load_profile, \
            mock.patch('main.snowboydecoder') as m_snowboydecoder:
        import main
        main.main()
        # test
