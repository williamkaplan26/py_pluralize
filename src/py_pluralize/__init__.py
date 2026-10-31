"""py_pluralize: English pluralisation with irregular forms.

Public API:
    pluralize(word, count=2) -> str
    is_plural(word) -> bool
"""

from .core import pluralize, is_plural

__all__ = ["pluralize", "is_plural"]
