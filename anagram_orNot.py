def is_anagram(s1,s2):
    list1_s1=list(s1)
    list1_s1.sort()
    list2_s2=list(s2)
    list2_s2.sort()

    if (list1_s1==list2_s2):
        print("Is anagram")
    else:
        print("Not an anagram")

if __name__ == '__main__':
    s1="madam"
    s2="you"
    is_anagram(s1,s2)