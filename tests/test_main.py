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


def test_import():
    """test import the module.

    error raised because
    test runner disable IO and profile populator require it to run.
    """
    with pytest.raises(IOError):
        import main  # NOQA


def test_import_and_mock_populator():
    """test import the module and mock profile_populator.

    it raise error because no profile is found.
    """
    with mock.patch('melissa.profile_populator.profile_populator'):
        with pytest.raises(IOError):
            from start import main  # NOQA


class WithProfileTest(unittest.TestCase):
    """test case using temp profile."""

    def setUp(self):
        """setup func."""
        mock_name = 'user'
        mock_tts = 'xxxx'
        mock_va_gender = 'female'
        mock_va_name = 'Melissa'
        mock_stt = 'keyboard'
        profile = {
            'actions_db_file': ':memory:',
            'modules': 'melissa.actions',
            'name': mock_name,
            'tts': mock_tts,
            'va_gender': mock_va_gender,
            'va_name': mock_va_name,
            'stt': mock_stt,
        }
        self.json_file = 'profile.json'
        self.bak_file = self.json_file + 'main-mod.bak'
        if os.path.isfile(self.json_file):
            self.json_file_exist = True
            copyfile(self.json_file, self.bak_file)
        else:
            self.json_file_exist = False
        with open(self.json_file, 'w') as f:
            json.dump(profile, f)

    def tearDown(self):
        """tear down func."""
        os.remove(self.json_file)
        # restore the backup
        if self.json_file_exist:
            copyfile(self.bak_file, self.json_file)

    def test_import(self):
        """test simple import."""
        with pytest.raises(IOError):
            from start import main  # NOQA

    def test_import_and_mock_stt(self):
        """test simple import but with mocked stt."""
        with mock.patch('melissa.stt.stt') as mock_stt:
            mock_stt.side_effect = [
                'hello world',
                KeyboardInterrupt,
            ]
            with pytest.raises(KeyboardInterrupt):
                from start import main  # NOQA
            assert mock_stt.call_count == 2
