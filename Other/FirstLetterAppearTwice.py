def repeatedCharacter(self, s: str) -> str:
    seen_char = set()

    for c in s:
        if c in seen_char:
            return c
        else:
            seen_char.add(c)