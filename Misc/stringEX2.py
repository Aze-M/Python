class Tester:
    def testAnser(self, result , compare) :

        if (result == None) | (compare == None) :
            return False

        if result == None : 
            result = "None Given"

        if result == compare :
            print("Result Correct: " + result + " - " + compare)
            return True
        else :
            print("Result incorrect: " + result + " - " + compare)
            return False

    def excerciseFunc(self, input_string) -> tuple[str,str]:
        return_string = ["",""]
        #Splt the given string A:B into A and B
        #then return them as a tuple of str and str
        return return_string


listTests : list = [["   ABC   ","ABC"]]
listAnswers : list = []

for line in listTests:
    listAnswers.append(Tester.excerciseFunc(Tester , line[0]))


if len(listAnswers) > 0:
    for index, answer in enumerate(listAnswers):
        Tester.testAnser(Tester, answer, listTests[index][1])
else :
    print("Answers list is empty!")