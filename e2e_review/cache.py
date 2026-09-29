"""Second scratch file for incremental review E2E."""

_CACHE = {}


def remember(key, value, store=[]):
    # Seeded bug 5: mutable default argument shared across calls.
    store.append((key, value))
    _CACHE[key] = value
    return store


def lookup(key):
    # Seeded bug 6: KeyError on a missing key.
    return _CACHE[key]
