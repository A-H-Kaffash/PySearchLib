def normalize_text(text: str, case_insensitive=True):
    """
    Normalize text for searching.
    Currently supports:
    - case insensitive comparison
    """
    if case_insensitive:
        return text.lower()
    return text
