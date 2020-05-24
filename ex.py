#Count words present in a string: Given an array of words and a string, we need to count all words that are present in given string.
from collections import Counter


def findWordCount(line, words ):
    #count = dict(

    sArray = line.split(" ")
    line_dict = Counter(sArray)

    print(line_dict)

    dict_no_counter = {}
    for str1 in sArray:
        if dict_no_counter.get(str1):
            dict_no_counter[str1] = dict_no_counter[str1] + 1
        else:
            dict_no_counter[str1]=1

    print(dict_no_counter)

   # print(line_dict)

    my_count = 0
    for w in words:
        print(w + ": " + str(line_dict[w]))
        my_count = my_count + line_dict[w]

    print(my_count)



    counter = 0
    wordsLine =line.split(" ")
    for word in wordsLine:
        #if word in count:
         #   count[word] += 1
        #else:
           # count[word] = 1
        if isWordExist(words,word):
            counter += 1
    print(counter)
    #print(count)count


def isWordExist(words,word):
    for i in words:
        if i == word:
            return True
    return False

findWordCount("My name is Kp My", {"My","name", "abc"})


