#Given N and K, print a string that has n characters. The string should have exactly k distinct characters and no adjacent positions.

def s(n , k):
    res =""
    for i in range(k):
        res = res+chr(ord('a')+i)
        count = 0
        for i in range(n - k):
            res = res+chr(ord('a')+count)
            count += 1
            if(count==k):
                count = 0
        return res
if __name__ == "__main__":
    n = 5
    k = 2
    print(s(n , k))