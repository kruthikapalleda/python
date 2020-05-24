import random
def my_random(n):
    otp =""
    for i in range(0,n,1):
        value= random.randint(0,9)
        otp = otp + str(value)

    return otp

def another_otp():
    value = random.randint(10000, 99999)
    return value

if __name__ == '__main__':
    n = 5
    res_otp = my_random(n)
    print(res_otp)

    res2_otp = another_otp();
    print(res2_otp)