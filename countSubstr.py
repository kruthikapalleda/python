#We are given a string S, we need to find count of all contiguous substrings starting and ending with same character.

def checkEquality(s):
    return (ord(s[0]) == ord(s[len(s) - 1]));

def countSubstringWithEqualEnds(s):
    result = 0;
    n = len(s);

    for i in range(n):

        for j in range(1, n - i + 1):

            if (checkEquality(s[i:i + j])):
                result += 1;
    return result;

s = "abcki"
print(countSubstringWithEqualEnds(s));
