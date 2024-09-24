from numpy import array
MyArray =   array([[20,23,30,33,42,49,55],
                   [12,17,26,31,34,38,47],
                   [ 8,17,20,24,33,39,43],
                   [25,34,39,45,49,52,55],
                   [ 2, 7,11,20,25,34,50],])


for row in MyArray:
    
    intLargest = -1
    intLowest = -1

    for id,entry in enumerate(row):
        if id>0:
            interval = abs(row[id-1] - entry)
            
            print(interval)

            if interval > intLargest or intLargest == -1:
                intLargest = interval
            if interval < intLowest or intLowest == -1:
                intLowest = interval
        
    print(f"({intLowest},{intLargest})")