def checkIfPangram(sentence: str) -> bool:
    alphabet = set()

    for c in sentence:
        alphabet.add(c)

    return len(alphabet) == 26