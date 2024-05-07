def pyramid():
    hight = int(input("Please enter Height of the pyramid:"))
    time = int(input("Please enter loop time:"))

    for t in range(time):
        for i in range(hight+1) :
            if i <=  hight :
                print(" " * (hight-i),"* " * i)

pyramid()