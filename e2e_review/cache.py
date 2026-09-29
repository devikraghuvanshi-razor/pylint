"""Second scratch file for incremental review E2E."""

_CACHE = {}


def remember(key, value, store=[]):
    # Seeded bug 5: mutable default argument shared across calls.
    store.append((key, value))
    _CACHE[key] = value
    return store
