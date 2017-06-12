import sys

def compareWords(firstWord, secondWord):
    if firstWord == secondWord:
        return 100

    if len(firstWord) != len(secondWord):
        return 0

    sortedFirstWord = list(firstWord)

    sortedSecondWord = list(secondWord)

    sortedFirstWord.sort()

    sortedSecondWord.sort()

    #quick way to check if they have the same letters, if not, its impossible for them to be anagrams
    if sortedFirstWord != sortedSecondWord:
        return 0
    else:
        swapsCount = countSwaps(list(firstWord), list(secondWord))

        score = swapsCount * 5

        if score > 100:
            return 0
        else:
            return (100 - score)

def countSwaps(firstword, secondword):

    swapcount = 0

    wordlength = len(secondword)
    j, i = 0,0
    #inspect each letter of both words in order, and check if the match one another
    while (wordlength > i):
        j = i
        while (firstword[j] != secondword[i]):
            j = j+1
            #they don't match, at least one swap is required
            swapcount = swapcount+1
        #swap the letters in the firstword with the next char
        while (j > i):
            chartoswap = firstword[j]
            firstword[j] = firstword[j-1]
            firstword[j-1] = chartoswap
            j = j-1
            #now that they are swapped, exit this while loop and check if the the newly swapped char, decrementing the current index j


        i = i+1

    return swapcount


words = input("Enter two comma separated words to check if they are anagrams: ")
firstword,secondword = words.split(',')
#secondword = words.split(',')[1]

print("Score of {} when comparing {} with {}".format(compareWords(firstword,secondword),firstword,secondword))


# print("Actual score:  {} \nExpected score 100".format(compareWords("ABCDEF", "ABCDEF")))
# print("Actual score:  {} \nExpected score 0".format(compareWords("ABDCEF", "BBCDEF")))
# print("Actual score:  {} \nExpected score 95".format(compareWords("BBDCEF", "BBCDEF")))
# print("Actual score:  {} \nExpected score 95".format(compareWords("HARRIS", "HARIRS")))
# print("Actual score:  {} \nExpected score 95".format(compareWords("HARRIS", "HRARIS")))
#
# print("Actual score:  {} \nExpected score 90".format(compareWords("BACDFE", "ABCDEF")))
# print("Actual score:  {} \nExpected score 90".format(compareWords("ABCFDE", "ABCDEF")))
#
# print("Actual score:  {} \nExpected score 75".format(compareWords("ANNE", "ENNA")))
# print("Actual score:  {} \nExpected score 25".format(compareWords("FEDCBA", "ABCDEF")))
# print("Actual score:  {} \nExpected score 0".format(compareWords("GFEDCBA", "ABCDEFG")))