def my_print(n):

    for i in range(0,len(n),1):

      if n[i] % 32 == 0:
        print("ANIMAL")
      elif n[i] % 16 == 0:
        print("ANIM")
      elif n[i] % 8 == 0:
        print("AN")
if __name__ == '__main__':
    n = [0,-8,32,4]
    my_print(n)