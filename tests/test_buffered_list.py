import unittest

from packages.helpers.buffered_list import BufferedList


class TestBufferedList(unittest.TestCase):

    """Test if the buffered list exceeds its specified max items."""

    def test_max_items(self):
        buffered_list = BufferedList(max_items=3)
        for i in range(4):
            buffered_list.append(i)
        self.assertLessEqual(len(buffered_list), 3)
        self.assertListEqual([1, 2, 3], buffered_list)
