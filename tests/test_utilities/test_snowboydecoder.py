"""test module."""
from unittest import TestCase
try:  # py3
    from unittest import mock
except ImportError:  # py2
    import mock

import pytest


class RingBufferTest(TestCase):
    """test for RingBuffer class."""

    def test_init(self):
        """test init."""
        with mock.patch('melissa.utilities.snowboydecoder.snowboyDetect') \
                as m_snowboy_detect:
            from melissa.utilities import snowboydecoder
            rb = snowboydecoder.RingBuffer()
