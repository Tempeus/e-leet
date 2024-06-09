def areOccurrencesEqual(s: str) -> bool:
    count = {}

    for c in s:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    
    distinct = set()
    for num in count.values():
        distinct.add(num)

    return len(distinct) == 1