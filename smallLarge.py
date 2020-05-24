#Given a string, find the minimum and the maximum length words in it.

def minMaxLengthWords(a):
    length = len(a)
    si = ei = 0
    min_length = length
    min_start_index = max_length = max_start_index = 0

    while ei <= length:
        if (ei < length) and (a[ei] != " "):
            ei += 1
        else:
            curr_length = ei - si

            if curr_length < min_length:
                min_length = curr_length
                min_start_index = si

            if curr_length > max_length:
                max_length = curr_length
                max_start_index = si
            ei += 1
            si = ei

    minWord = a[min_start_index:
                  min_start_index + min_length]

    maxWord = a[max_start_index: max_length]

    print("Minimum length word: ", minWord)
    print("Maximum length word: ", maxWord)


a = "The signatures is of your head"
minMaxLengthWords(a)
