import time
import math

timeStart = time.perf_counter()

intMaxNum = 0

while intMaxNum == 0: 
    try :
        print("Input max digits for last prime:")
        intMaxNum = int( input() )
    except ValueError:
        print("Not a valid integer.")

intCurNum = 3
intPrimeNumCount = 0
intLargestPrime = 0

if (intMaxNum >= 2) :
    intPrimeNumCount+=1
    print("2")

intStrCntLen = 1

#Iterate the main number up
while intStrCntLen <= intMaxNum :
   
    #assume it's prime
    isPrime = True
    intSqrtNum = int(math.sqrt(intCurNum))

    #test up to the square root
    for intNumTester in range(3, intSqrtNum +1, 2) :
        if intCurNum%intNumTester == 0:
            isPrime = False
            break
    
    #print primes and increase current number
    if isPrime == True :
        intPrimeNumCount+=1
        intLargestPrime = intCurNum
        print(intCurNum)

    intCurNum+=2
    intStrCntLen = len(str(intCurNum)) 

print(f"Total Prime number count between 0 and {intCurNum} is {intPrimeNumCount}. Largest Prime is {intLargestPrime}.")
print(f"Took {time.perf_counter() - timeStart:.2f} seconds.")