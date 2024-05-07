def majority():
    list_number = [1,4,5,5,5,1,5]
    list_number.sort()
    major = len(list_number)//2
    countmajor = 0
    for i in list_number :
        if i == list_number[major] :
            countmajor +=1

    if countmajor >= major:
        print("'Majority'")
    else:
        print("No Majority Element")


majority()