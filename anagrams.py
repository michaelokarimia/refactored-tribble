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
    pass


print(compareWords("aa", "ab"))

