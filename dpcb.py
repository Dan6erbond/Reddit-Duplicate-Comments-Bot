import logging
import sys

import praw
from praw.reddit import Comment

from packages.core import CommentTuple, DuplicateCommentDetector

logger = logging.getLogger("Duplicate Comments Bot")
logger.setLevel(logging.DEBUG)

message = """Hey there! It looks like your comment is a duplicate. This can happen on occassion when the Reddit service or the app makes a mistake.

[Original comment]({original_comment.permalink})

[Duplicate comment]({comment.permalink})

^([View Source](https://github.com/Dan6erbond/DuplicateCommentsBot) | [Feedback to u/Dan6erbond](https://www.reddit.com/message/compose?to=Dan6erbond&subject=Feedback%20on%20Duplicate%20Comments%20Bot))"""

reddit = praw.Reddit("dpcb", user_agent="Duplicate comment detector.")
duplicate_comment_detector = DuplicateCommentDetector()

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
# Set the console logging level to info only if the -i flag was added in the arguments.
if "-i" in sys.argv:
    console_handler.setLevel(logging.INFO)
# Set the console logging level to debug only if the -d flag was added in the arguments.
if "-d" in sys.argv:
    console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
# Log verbose messages to a file, dpcb.log.
file_handler = logging.FileHandler("dpcb.log", encoding="utf8")
logger.addHandler(file_handler)

# Output a test message to the logger.
logger.debug("Test.")

# Stream over the latest Reddit comments and check whether they're a duplicate.
for comment in reddit.subreddit("all").stream.comments():
    comment: Comment
    # Log the comment ID.
    logger.debug(f"Comment found: {comment.permalink}")
    # Convert the comment to a CommentTuple so we can use it in the duplicate detector.
    comment_tuple = CommentTuple(id=comment.id, parent_id=comment.parent_id, body=comment.body)
    # Add the comment tuple to the duplicate detector and check if it's a duplicate.
    if original_comment_tuple := duplicate_comment_detector.add_comment(comment_tuple):
        # Get a comment instance of the original comment.
        original_comment = reddit.comment(id=original_comment_tuple.id)
        # Log the duplicate comment as an info.
        logger.info(f"Duplicate comment found: {original_comment.permalink}")
        try:
            # Respond to the comment with a message.
            comment.reply(message.format(original_comment=original_comment, comment=comment))
        except Exception as e:
            # Handle the error.
            logger.error(f"Error replying to duplicate comment: {e}")
