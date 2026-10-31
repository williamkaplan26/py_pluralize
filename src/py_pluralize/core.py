"""Core pluralisation logic for py_pluralize.

Design decision: the library exposes exactly two functions, ``pluralize`` and
``is_plural``.  ``pluralize`` always returns a string; when ``count == 1`` it
returns the singular form unchanged, otherwise it returns the plural form.
This mirrors the common ``pluralize(word, count)`` convention and avoids
surprising the caller with number-to-word conversion.

The irregular table is intentionally small and hand-curated.  We do not attempt
to derive Latin/Greek rules or handle uncountable nouns beyond a short list;
those cases are left to the caller because guessing wrong is worse than
returning a regular form.
"""

from __future__ import annotations

# Words that do not change between singular and plural.
_UNCOUNTABLE = frozenset(
    {
        "sheep",
        "fish",
        "deer",
        "series",
        "species",
        "money",
        "information",
        "equipment",
        "rice",
        "news",
    }
)

# Explicit irregular singular -> plural mappings.
_IRREGULAR = {
    "man": "men",
    "woman": "women",
    "child": "children",
    "person": "people",
    "foot": "feet",
    "tooth": "teeth",
    "goose": "geese",
    "mouse": "mice",
    "louse": "lice",
    "ox": "oxen",
    "die": "dice",
    "leaf": "leaves",
    "life": "lives",
    "knife": "knives",
    "wife": "wives",
    "wolf": "wolves",
    "shelf": "shelves",
    "loaf": "loaves",
    "potato": "potatoes",
    "tomato": "tomatoes",
    "hero": "heroes",
    "echo": "echoes",
    "veto": "vetoes",
    "cactus": "cacti",
    "focus": "foci",
    "fungus": "fungi",
    "nucleus": "nuclei",
    "syllabus": "syllabi",
    "analysis": "analyses",
    "basis": "bases",
    "crisis": "crises",
    "diagnosis": "diagnoses",
    "thesis": "theses",
    "phenomenon": "phenomena",
    "criterion": "criteria",
    "datum": "data",
    "medium": "media",
    "bacterium": "bacteria",
        "curriculum": "curricula",
        " memorandum": "memoranda",
    }

# Reverse lookup for is_plural.  Built once at import time.
_PLURAL_TO_SINGULAR = {v: k for k, v in _IRREGULAR.items()}


def _regular_plural(word: str) -> str:
    """Return the regular English plural of *word*.

    The rules are applied in order of specificity: consonant+y, sibilants,
    then the default ``+s``.  We lowercase only for suffix matching so that
    capitalisation of the input is preserved in the output.
    """
    lower = word.lower()
    if lower.endswith("y") and len(lower) > 1 and lower[-2] not in "aeiou":
        return word[:-1] + "ies"
    if lower.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"
    return word + "s"


def pluralize(word: str, count: int = 2) -> str:
    """Return the plural form of *word* unless *count* is exactly 1.

    ``count`` defaults to 2 so that ``pluralize("cat")`` returns ``"cats"``.
    Passing ``count=1`` returns the singular unchanged.  The function does not
    validate that *word* is a known English word; unknown words fall back to
    the regular rules.
    """
    if count == 1:
        return word
    lower = word.lower()
    if lower in _UNCOUNTABLE:
        return word
    if lower in _IRREGULAR:
        return _IRREGULAR[lower]
    return _regular_plural(word)


def is_plural(word: str) -> bool:
    """Return True if *word* looks like a plural form.

    This is a best-effort check: it recognises the irregular plurals in the
    table, uncountable nouns, and the regular suffix patterns.  It does not
    claim to be a full morphological analyser.
    """
    lower = word.lower()
    if lower in _UNCOUNTABLE:
        return True
    if lower in _PLURAL_TO_SINGULAR:
        return True
    if lower.endswith("ies") and len(lower) > 3:
        return True
    if lower.endswith(("es", "s")) and not lower.endswith("ss"):
        return True
    return False
