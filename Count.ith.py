# Count of words whose i-th letter is either (i-1)-th, i-th, or (i+1)-th letter of given word
# Given a string str. The task is to count the words having the same length as str and each letter at the i-th position is either (i-1)-th, i-th, or (i+1)-th position letter of str.

def countWords(str, l):
    count = 1

    if (l == 1):
        return count


    if (str[0] == str[1]):
        count *= 1
    else:
        count *= 2

    for j in range(1, l - 1):

        if (str[j] == str[j - 1] and str[j] == str[j + 1]):
            count *= 1


        elif (str[j] == str[j - 1] or
              str[j] == str[j + 1] or
              str[j - 1] == str[j + 1]):
            count *= 2


        else:
            count *= 3


    if (str[l - 1] == str[l - 2]):
        count *= 1
    else:
        count *= 2

    return count



if __name__ == "__main__":
    str = "a"
    l = len(str)

    print(countWords(str, l))