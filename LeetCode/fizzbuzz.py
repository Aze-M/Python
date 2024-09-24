input = int(input())

def fizzbuzz(int_input):
    list_return = []

    for cur in range(1,int_input+1):
        answer = ""

        if cur%3 == 0:
            answer+="fizz"

        if cur%5 == 0:
            answer+="buzz"        

        if answer == "":
            answer = str(cur)

        list_return.append(answer)
        
    return list_return

print(fizzbuzz(input))