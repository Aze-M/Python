import time
import math

timeStart = time.perf_counter()

intMaxNum = 0

while intMaxNum == 0: 
    try :
        print("Input max number to look for primes:")
        intMaxNum = int( input() )
    except ValueError:
        print("Not a valid integer.")

intCurNum = 3
intPrimeNumCount = 0

if (intMaxNum >= 2) :
    intPrimeNumCount+=1
    print("2")

#Iterate the main number up
while intCurNum + 2 < intMaxNum :

    #assume it's prime
    isPrime = True
    intSqrtNum = int(math.sqrt(intCurNum))

    #test up to the square root
    for intNumTester in range(3, intSqrtNum +1, 2) :
        if intCurNum%intNumTester == 0:
            isPrime = False
            break
    
    #print primes and increase current number
    if isPrime == False :
        intCurNum+=2
        continue
    else :
        intPrimeNumCount+=1
        print(intCurNum)
        intCurNum+=2


print(f"Total Prime number count between 0 and {intMaxNum} is {intPrimeNumCount}.")
print(f"Took {time.perf_counter() - timeStart:.2f} seconds.")