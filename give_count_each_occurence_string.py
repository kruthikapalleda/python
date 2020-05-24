def occurence_string(s):
    my_dict = {}

    for i in range (0,len(s),1):
     if s[i] in my_dict.keys():
         my_dict[s[i]] = my_dict[s[i]] + 1
     else:
         my_dict[s[i]] = 1
    print(my_dict)

     #for k , v in my_dict.items():
       #  if (v >= 1):                 
        #  print("Occurence of each element is : ", my_dict)
    print(s)

if __name__ == '__main__':
    s ="aaaaaaaaaaaaAAAAAAAAAAAbbbbccce"
    occurence_string(s)
