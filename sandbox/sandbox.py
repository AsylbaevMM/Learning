


def zipper(iterable1, iterable2):
    for i in range(min(len(iterable1), len(iterable2))):
        yield iterable1[i]
        yield iterable2[i]

print(*zipper([1, 2, 3, 4, 5, 6], ['a', 'b', 'c', 'd', 'e', 'f']))