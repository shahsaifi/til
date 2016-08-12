def group_by_anagrams(words):
    anagrams = {}
    for word in words:
        i = ''.join(sorted(word))
        if i not in anagrams:
            anagrams[i] = list()
        anagrams[i].append(word)
    return anagrams.values()


def main():
    words = ['dog', 'elvis', 'forest', 'fortes', 'foster', 'goat',
             'god', 'heros', 'horse', 'lives', 'shore', 'softer']

    print group_by_anagrams(words)

main()
