# Ez way to find max and min
# python is include methon to find min and max
# Max = max(array name)
# Min = min(array name)

def minimum_number():
    arr = [2,4,6,8,1,3,10,5]
    min = max(arr)
    for i in arr:
        if i < min :
            min = i
    print("Minimum number element is:%d"%min)

def maximum_number():
    arr = [2,4,6,8,1,3,10,5]
    max = min(arr)
    for i in arr:
        if i > max :
            max = i
    print("Maximum number element is:%d"%max)
            
    
        
minimum_number()
maximum_number()
