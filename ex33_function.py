loopNumber = 6
numbers = []
incrementer = 1

def createArray(loopNumber, incrementer) :
    
    i = 0
    
    while i < loopNumber:
        print("At the top i is %d" % i)
        numbers.append(i)

        i = i + incrementer
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

createArray(loopNumber, incrementer)

print("The numbers: ")

for i in numbers:
    print(i)