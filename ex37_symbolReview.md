## from  

- 'from' keyword is used for importing a specific variable, class, or a function from a module.  

    ```python
    from sys import exit
    ```  

## and   

- 'and' keyword is a logical operator:

    ```python
    x = 11

    if x > 0 and x < 10 :
        print("Value of the x variable is %i. It is between 0 and 10." % x)
    else :
        print("Value of the x variable is outside of the treshold values (0-10). X is %i." %x)
    ```  
    
## as

- 'as' keyword is used to define an alias:

    ```python
    with open('ex37.txt') as data :
        list = data.read().splitlines()
        
        for i in list:
            print(i)
    ```  

## del    

- 'del' keyword is used to delete objects

    ```python
    myString = 'hello'
    
    print(myString)
    
    del myString
    ```

## not

- The Keyword 'not' is a unary type operator which means that it takes only one operand for the logical operation and returns the complementary of the boolean value of the operand.

    ```python
    a = True
    
    print(not a) # it will print False
    ```  

## while

- Python while loop is used to run a specific code until a certain condition is met. Here, A while loop evaluates the condition. If the condition evaluates to True , the code inside the while loop is executed.

    ```python
    someNumber = 3
    count = 0
    
    while someNumber > count:
        print("Count number is:", count)
        count = count + 1
    ```  

## if, elif, else

- Keywords 'if' 'else' 'elif' are used to construct loops.

    ```python
    apples = 2

    if apples is not 0:
        
        print("I have %i apples. Would you like one?" % apples)
        answer = input("> ")
        
        if answer == "yes":
            
            print("Allright, here is an apple for you...")
            
        elif answer == "no":
            
            print("No apple for you then...")
        
        else:
            
            print("I do not understand what you're trying to say.")
    ```  

## global

- In Python, the global keyword allows us to modify the variable outside of the current scope. It is used to create a global variable and make changes to the variable in a local context.

    ```python
    c = 1 # this is a global variable

    def addIntegers():
        
        # use global keyword if a variable is not defined within the function:
        global c
        
        # add 2 to c
        c = c + 2
        print(c)

    addIntegers()
    ```

## or

- The or keyword is a logical operator. Logical operators are used to combine conditional statements. The return value will be True if one of the statements return True, otherwise it will return False.

    ```python
    if 5 > 1 or 5 > 2:
    print("At least one of the statements are True")
    else:
    print("None of the statements are True")
    ```

## with

- The with statement in Python is used for resource management and exception handling. You’d most likely find it when working with file streams. 
- For example, the statement ensures that the file stream process doesn’t block other processes if an exception is raised, but terminates properly.

    ```python
    file = open('ex37.txt', 'w')

    try:
        file.write("200000")
        
    finally: 
        file.close()

    with open('ex37.txt', 'w') as file:
        file.write("30000")
    ```

## assert

- The assert keyword is used when debugging code.
- The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
- You can write a message to be written if the code returns False, check the example below.

    ```python
    x = "hello"

    #if condition returns False, AssertionError is raised:
    assert x == "goodbye", "x should be 'hello'"
    ```

## pass

- The pass statement is used as a placeholder for future code.
- When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
- Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

    ```python
    def myfunction():
    pass

    for x in [0, 1, 2]:
    pass
    ```

## yield

- yield keyword is used to create a generator function. A type of function that is memory efficient and can be used like an iterator object.  
- In layman terms, the yield keyword will turn any expression that is given with it into a generator object and return it to the caller. Therefore, you must iterate over the generator object if you wish to obtain the values stored there. we will see the yield python example.  
- Difference between return and yield Python:
    The yield keyword in Python is similar to a return statement used for returning values in Python which returns a generator object to the one who calls the function which contains yield, instead of simply returning a value. The main difference between them is, the return statement terminates the execution of the function. Whereas, the yield statement only pauses the execution of the function. Another difference is return statements are never executed. whereas, yield statements are executed when the function resumes its execution.  
- Advantages of yield:
    - Using yield keyword is highly memory efficient, since the execution happens only when the caller iterates over the object.
    - As the variables states are saved, we can pause and resume from the same point, thus saving time.
- Disadvantages of yield: 
    -Sometimes it becomes hard to understand the flow of code due to multiple times of value return from the function generator.
    - Calling of generator functions must be handled properly, else might cause errors in program.

### Example 1: Generator functions and yield Keyword in Python

- Generator functions behave and look just like normal functions, but with one defining characteristic. Instead of returning data, Python generator functions use the yield keyword. Generators’ main benefit is that they automatically create the functions ```__iter__()``` and next (). Generators offer a very tidy technique to produce data that is enormous or limitless.

    ```python
    def fun_generator():
        yield "Hello world!!"
        yield "This is my generator func."
    
    
    obj = fun_generator()
    
    print(type(obj))
    
    print(next(obj))
    print(next(obj))
    ```

- Output:

    ```
    <class 'generator'>
    Hello world!!
    This is my generator func.
    ``` 
### Example 2: Generating an Infinite Sequence

- Here, we are generating an infinite sequence of numbers with yield, yield returns the number and increments the num by + 1. 
- Note: Here we can observe that num+=1 is executed after yield but in the case of a return, no execution takes place after the return keyword.

    ```python

    def inf_sequence():
        num = 0
        while True:
            yield num
            num += 1
            
    for i in inf_sequence():
        print(i, end=" ")
    ```

- output: 

    ```
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 
    26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 
    49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 
    72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96.......
    ```  
    
### Example 3:  Demonstrating yield working with a list.

- Here, we are extracting the even number from the list.

```python
# generator to print even numbers
def print_even(test_list):
    for i in test_list:
        if i % 2 == 0:
            yield i
 
# initializing list
test_list = [1, 4, 5, 6, 7]
 
# printing initial list
print("The original list is : " + str(test_list))
 
# printing even numbers
print("The even numbers in list are : ", end=" ")
for j in print_even(test_list):
    print(j, end=" ")
```

- output:  

    ```
    The original list is : [1, 4, 5, 6, 7]
    The even numbers in list are :  4 6
    ```
### Example 4: Use of yield Keyword as Boolean

- The possible practical application is that when handling the last amount of data and searching particulars from it, yield can be used as we don’t need to look up again from start and hence would save time. There can possibly be many applications of yield depending upon the use cases. 

```python

# func to count number of given word
def print_even(test_string):
    for i in test_string:
        if i == "geeks":
            yield i
 
 
# initializing string
test_string = " The are many geeks around you, \
              geeks are known for teaching other geeks"
 
# count numbers of geeks used in string
count = 0
print("The number of geeks in string is : ", end="")
test_string = test_string.split()
 
for j in print_even(test_string):
    count = count + 1
 
print(count
```

- output: 

    ```
    The number of geeks in string is: 3
    ```




