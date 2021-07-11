import unittest

from packages.core.duplicate_comment_detector import DuplicateCommentDetector
from packages.core.comment_tuple import CommentTuple


class TestDuplicateCommentDetector(unittest.TestCase):

    """Test the add_comment method on DuplicateCommentDetector."""

    def test_add_comment(self):
        # Create a dummy CommentTuple
        c1: CommentTuple = CommentTuple(1, "a", "b")
        # Create a DuplicateCommentDetector
        d: DuplicateCommentDetector = DuplicateCommentDetector()
        # Add the first comment
        res = d.add_comment(c1)
        # Assert that the comment is in the detector's list of comments
        self.assertEqual(d.comment_list[0], c1)
        # Assert that the returned result is None as there aren't any duplicate comments
        self.assertEqual(res, None)

    """Test if duplicate comments are caught when calling add_comment on DuplicateCommentDetector."""

    def test_add_comment_duplicate(self):
        # Create a dummy CommentTuple
        c1: CommentTuple = CommentTuple(1, "a", "b")
        # Create an identical CommentTuple
        c2: CommentTuple = CommentTuple(1, "a", "b")
        # Create a DuplicateCommentDetector
        d: DuplicateCommentDetector = DuplicateCommentDetector()
        # Add the first comment
        d.add_comment(c1)
        # Add the same comment again
        res = d.add_comment(c2)
        # Assert that the returned result is the first comment we passed
        self.assertEqual(res, c1)
