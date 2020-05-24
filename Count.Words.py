def myCount(s):
    flag = 1
    count = 0
    for i in range(0,len(s),1):
        if s[i]==' ' or s[i]== '\n' or s[i]== '\t':
            flag=1
        elif flag == 1:
            count = count+1
            flag = 0

    return count


if __name__ == '__main__':
 print(myCount('One two         three\n four\tfive '))




