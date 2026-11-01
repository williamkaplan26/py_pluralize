# py_pluralize

English pluralisation with a small irregular table, standard library only.

```python
from py_pluralize import pluralize, is_plural

pluralize("cat")        # 'cats'
pluralize("child")      # 'children'
pluralize("sheep")      # 'sheep'
pluralize("cat", 1)     # 'cat'
is_plural("mice")       # True
is_plural("mouse")      # False
```

## Why this exists

Most pluralisation snippets either over-reach into Latin and Greek rules and get
English wrong, or they only append ``s``.  This library makes one clear trade-off:
it handles a curated set of irregulars and uncountable nouns, and otherwise applies
the regular English suffix rules.  Unknown words fall back to the regular rules
rather than raising, because callers usually want a best-effort string, not an
exception.

## The awkward edge

``is_plural`` is a heuristic.  It returns True for words that end in ``s`` or
``es`` (except double-s words like ``grass``) and for known irregular plurals.
It will call ``bus`` plural because it ends in ``s``, and it cannot know that
``series`` is both singular and plural.  If you need certainty, keep your own
lexicon; this function is for display and filtering, not for parsing.
