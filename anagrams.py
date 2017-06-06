def compareWords(firstWord, secondWord):
    if firstWord == secondWord:
        return 100

    if len(firstWord) != len(secondWord):
        return 0

    sortedFirstWord = list(firstWord)

    sortedSecondWord = list(secondWord)

    sortedFirstWord.sort()

    sortedSecondWord.sort()

    if sortedFirstWord != sortedSecondWord:
        '''Not an anagram'''
        return 0
    else:
        swapsCount = countSwaps(firstWord, secondWord)

        return swapsCount * 5

def countSwaps(firstWord, secondWord):

    swaps = 0

    for x in xrange(len(secondWord)):
        if firstWord[x] != secondWord[x]:
            swaps =+ 1

    return swaps

print(compareWords("ABCDEF", "ABCDEF"))
print(compareWords("ABDCEF", "BBCDEF"))
print(compareWords("BBDCEF", "BBCDEF"))
print(compareWords("HARRIS", "HARIRS"))
print(compareWords("BACDFE", "ABCDEF"))
print(compareWords("ABCFDE", "ABCDEF"))
print(compareWords("ANNE", "ENNA"))
print(compareWords("FEDCBA", "ABCDEF"))
print(compareWords("GFEDCBA", "ABCDEFG"))