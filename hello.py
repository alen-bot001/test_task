"""Small demo module used to verify the test pipeline for this repository."""

DEFAULT_NAME = "alen-bot001"


def greet(name: str = DEFAULT_NAME) -> str:
    """Return a greeting for *name*.

    Leading and trailing whitespace is ignored.

    Raises:
        TypeError: If *name* is not a string.
        ValueError: If *name* is empty or contains only whitespace.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")

    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")

    return f"Hello, {name}!"
