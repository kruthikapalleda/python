def word_count(str):
    count = dict()
    words = str.split("the quick brown fox jumps over the lazy dog.")
    for word in words:
        if word in count:  # count.get(word)
            count[word] += 1
        else:
            count[word] = 1
    return count

if __name__ == '__main__':

 print(word_count(str))





