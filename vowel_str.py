def vowel_occur(s):
    vowels = 0
    res_vowels = ""
    vowel1= ['a','e','i','o','u']
    vowel2= ['A','E','I','O','U']

    for i in range(0,len(s),1):
        if s[i] in vowel1 or s[i] in vowel2:
            vowels = vowels+1
            res_vowels = res_vowels + s[i]

    print("total " + str(vowels))
    print("vowels :  " + res_vowels)

if __name__ == '__main__':
    sr = "guru"
    vowel_occur(sr)