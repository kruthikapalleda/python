def grouping_numbers(l):
    positive_group = []
    negative_group = []
    zero_group = []

    for i in range (0,len(l),1):
        if l[i] > 0:
            positive_group.append(l[i])
            #print("Positive numbers are :", positive_group)
        elif l[i] < 0:
            negative_group.append(l[i])
            #print("Negative numbers are :", negative_group)
        elif l[i] == 0:
            zero_group.append(l[i])
            #print("Zero number are :", zero_group)
    print(positive_group)
    print(negative_group)
    print(zero_group)

if __name__ == '__main__':
    l= [10,20,-1,0,-100,26]
    grouping_numbers(l)
