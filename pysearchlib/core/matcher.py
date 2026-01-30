def wildcard_match(pattern: str, text: str) -> bool:
    """
    Match text with wildcard pattern.
    Supported:
        *  -> matches any sequence of characters
        ?  -> matches exactly one character
    """

    p_len = len(pattern)
    t_len = len(text)

    # dp[i][j] => pattern[:i] matches text[:j]
    dp = [[False] * (t_len + 1) for _ in range(p_len + 1)]
    dp[0][0] = True

    # Handle patterns starting with *
    for i in range(1, p_len + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]

    for i in range(1, p_len + 1):
        for j in range(1, t_len + 1):
            if pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif pattern[i - 1] == '?' or pattern[i - 1] == text[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[p_len][t_len]


# tests
'''
a = wildcard_match("*.log", "error.log")     # True
b = wildcard_match("file?.txt", "file1.txt") # True
c = wildcard_match("file?.txt", "file12.txt")# False
d = wildcard_match("a*b", "axxxb")           # True

print( a, b, c, d , sep="\n", end="\n\n")
'''