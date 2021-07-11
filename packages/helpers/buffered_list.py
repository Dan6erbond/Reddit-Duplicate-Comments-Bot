from typing import TypeVar

T = TypeVar('T')


"""A custom list class that only stores the latest 300 items added to it."""


class BufferedList(list[T]):

    """Initialize items list."""

    def __init__(self, max_items: int) -> None:
        self.max_items = max_items
        super(BufferedList, self).__init__()

    """Add the given item and make sure list doesn't exceed specified length."""

    def append(self, item):
        if len(self) >= self.max_items:
            self.pop(0)
        super(BufferedList, self).append(item)
