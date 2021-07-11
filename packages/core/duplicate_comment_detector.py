from typing import Optional

from ..helpers.buffered_list import BufferedList
from .comment_tuple import CommentTuple


class DuplicateCommentDetector:

    """Initialize the class with a buffered list of 300 items to keep track of comments."""

    def __init__(self) -> None:
        self.comment_list = BufferedList[CommentTuple](300)

    """Add a comment to the buffered list and yield comments that have been seen before."""

    def add_comment(self, comment: CommentTuple) -> Optional[CommentTuple]:
        for c in self.comment_list:
            # Check if comment was already stored in list
            if c.parent_id == comment.parent_id and c.body == comment.body:
                return c
        self.comment_list.append(comment)
