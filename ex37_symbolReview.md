# Keywords
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

## break

- break statement in Python is used to bring the control out of the loop when some external condition is triggered. break statement is put inside the loop body (generally after if condition).  It terminates the current loop, i.e., the loop in which it appears, and resumes execution at the next statement immediately after the end of that loop. If the break statement is inside a nested loop, the break will terminate the innermost loop.

### Example 

    ```python

    for i in range(10):
        print(i)
        if i == 2:
            break

    ```

## try / except / else / finally

- Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program.

- Some of the common Exception Errors are : 
    - IOError: if the file can’t be opened
    - KeyboardInterrupt: when an unrequired key is pressed by the user
    - ValueError: when built-in function receives a wrong argument
    - EOFError: if End-Of-File is hit without reading any data
    - ImportError: if it is unable to find the module

- Try and Except statement is used to handle these errors within our code in Python. The try block is used to check some code for errors i.e the code inside the try block will execute when there is no error in the program. Whereas the code inside the except block will execute whenever the program encounters some error in the preceding try block.

- How try() works? 
    - First, the try clause is executed i.e. the code between try and except clause.
    - If there is no exception, then only the try clause will run, except the clause is finished.
    - If any exception occurs, the try clause will be skipped and except clause will run.
    - If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops.
    - A try statement can have more than one except clause

    ```python
    # Python code to illustrate
    # working of try()
    def divide(x, y):
        try:
            # Floor Division : Gives only Fractional Part as Answer
            result = x // y
            print("Yeah ! Your answer is :", result)
        except ZeroDivisionError:
            print("Sorry ! You are dividing by zero ")
    
    # Look at parameters and note the working of Program
    divide(3, 2)
    ```

- In python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.

    ```python
    # Program to depict else clause with try-except
    
    # Function which returns a/b
    def AbyB(a , b):
        try:
            c = ((a+b) // (a-b))
        except ZeroDivisionError:
            print ("a/b result in 0")
        else:
            print (c)
    
    # Driver program to test above function
    AbyB(2.0, 3.0)
    AbyB(3.0, 3.0)
    ```
- Python provides a keyword finally, which is always executed after the try and except blocks. The final block always executes after normal termination of try block or after try block terminates due to some exceptions.

    ```python
    # Python program to demonstrate finally
        
    # No exception Exception raised in try block
    try:
        k = 5//0 # raises divide by zero exception.
        print(k)
        
    # handles zerodivision exception    
    except ZeroDivisionError:   
        print("Can't divide by zero")
            
    finally:
        # this block is always executed 
        # regardless of exception generation.
        print('This is always executed') 
    ```

## import

- Import in python is similar to #include header_file in C/C++. Python modules can get access to code from another module by importing the file/function using import. The import statement is the most common way of invoking the import machinery, but it is not the only way.

- When the import is used, it searches for the module initially in the local scope by calling `__import__()` function. The value returned by the function is then reflected in the output of the initial code. 

    ```python
    import math
    pie = math.pi
    print("The value of pi is : ",pie)
    ```

- In the above code module, math is imported, and its variables can be accessed by considering it to be a class and pi as its object. The value of pi is returned by `__import__()`. pi as a whole can be imported into our initial code, rather than importing the whole module.  

    ```python
    from math import pi
    
    # Note that in the above example,
    # we used math.pi. Here we have used
    # pi directly.
    print(pi)
    ```

- In the above code module, math is not imported, rather just pi has been imported as a variable. All the functions and constants can be imported using *. 

    ```python
    from math import *
    print(pi)
    print(factorial(6))
    ```

## print

- Python print() function prints the message to the screen or any other standard output device.
- Parameters: 
    - value(s): Any value, and as many as you like. Will be converted to a string before printed
    - sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
    - end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
    - file : (Optional) An object with a write method. Default :sys.stdout
    - flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False
- Return Type: It returns output to the screen.
- String literals in python’s print statement are primarily used to format or design how a specific string appears when printed using the print() function.
    - \n : This string literal is used to add a new blank line while printing a statement.
    - “” : An empty quote (“”) is used to print an empty line.

    ```python
    print("Hello world \n is best for DSA Conten.")
    ```

- The end keyword is used to specify the content that is to be printed at the end of the execution of the print() function. By default, it is set to “\n”, which leads to the change of line after the execution of print() statement.

    ```python
    # This line will automatically add a new line before the
    # next print statement
    print ("This is a print statement.")
    
    # This print() function ends with "**" as set in the end argument.
    print ("This print ends with ** end character so there will be no new line.", end= "**")
    print("This is the same line.")
    ```
- The I/Os in python are generally buffered, meaning they are used in chunks. This is where flush comes in as it helps users to decide if they need the written content to be buffered or not. By default, it is set to false. If it is set to true, the output will be written as a sequence of characters one after the other. This process is slow simply because it is easier to write in chunks rather than writing one character at a time. To understand the use case of the flush argument in the print() function, let’s take an example.

    ```python
    import time
    
    count_seconds = 3
    for i in reversed(range(count_seconds + 1)):
        if i > 0:
            print(i, end='>>>', flush = True)
            time.sleep(1)
        else:
            print('Start')
    ```
- The print() function can accept any number of positional arguments. To separate these positional arguments , keyword argument “sep” is used.

    ```python
    a=12
    b=12
    c=2022
    print(a,b,c,sep="-")
    ```

- Contrary to popular belief, the print() function doesn’t convert the messages into text on the screen. These are done by lower-level layers of code, that can read data(message) in bytes. The print() function is an interface over these layers, that delegates the actual printing to a stream or file-like object. By default, the print() function is bound to sys.stdout through the file argument. 

    ```python
    import io
    
    # declare a dummy file
    dummy_file = io.StringIO()
    
    # add message to the dummy file
    print('Hello Geeks!!', file=dummy_file)
    
    # get the value from dummy file
    dummy_file.getvalue()
    ```
    
    ```python
    print('Welcome to Python world.!!', file=open('Testfile.txt', 'w'))
    ```
## class

- Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

    ```python
    # python code to demonstrate example of 
    # class keyword 

    # an empty class
    class sample:
        pass

    # main code
    # printing it's type 
    print("type of class: ", type(sample))
    ```
    
    ```python
    # python code to demonstrate example of 
    # class keyword 

    # student class code in Python

    # class definition
    class Student:
        __id=0
        __name=""
        __course=""
        
        # function to set data 
        def setData(self,id,name,course):
            self.__id=id
            self.__name = name
            self.__course = course
        
        # function to get/print data
        def showData(self):
            print("Id\t:",self.__id)
            print("Name\t:", self.__name)
            print("Course\t:", self.__course)

    # main function definition
    def main():
        #Student class Object
        std=Student()
        std.setData(1,'Manju','M. Com.')
        std.showData()
        
    if __name__=="__main__":
        main()
    ```
    
## raise

- Python raise Keyword is used to raise exceptions or errors. The raise keyword raises an error and stops the control flow of the program. It is used to bring up the current exception in an exception handler so that it can be handled further up the call stack.
- In the below code, we check if an integer is even or odd. if the integer is odd an exception is raised.  a  is a variable to which we assigned a number 5, as a is odd, then if loop checks if it’s an odd integer, if it’s an odd integer then an error is raised.

    ```python
    a = 5
    
    if a % 2 != 0:
        raise Exception("The number shouldn't be an odd integer")
    ```

## continue

- Python Continue statement is a loop control statement that forces to execute the next iteration of the loop while skipping the rest of the code inside the loop for the current iteration only, i.e. when the continue statement is executed in the loop, the code inside the loop following the continue statement will be skipped for the current iteration and the next iteration of the loop will begin.

- In the following code, 'e' letter will not be printed:

    ```python
    for var in "MySampleText":
        if var == "e":
            continue
        print(var)
    ```
## is

- This keyword is used to test object identity. The “is keyword” is used to test whether two variables belong to the same object. The test will return True if the two objects are the same else it will return False even if the two objects are 100% equal.

    ```python
    # Python program to demonstrate
    # is keyword
    # output will be False and True in the second line
    
    x = ["a", "b", "c", "d"]
    
    y =  ["a", "b", "c", "d"]
    
    print(x is y)
    print(x == y)
    ```
## return

- A return statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller. The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned. A return statement is overall used to invoke a function so that the passed statements can be executed.

    ```python
    # Python program to
    # demonstrate return statement
    
    def add(a, b):
    
        # returning sum of a and b
        return a + b
    
    def is_true(a):
    
        # returning boolean of a
        return bool(a)
    
    # calling function
    res = add(2, 3)
    print("Result of add function is {}".format(res))
    
    res = is_true(2<5)
    print("\nResult of is_true function is {}".format(res))
    ```

- In Python, we can return multiple values from a function. Following are different ways.  
    - Using Object: This is similar to C/C++ and Java, we can create a class (in C, struct) to hold multiple values and return an object of the class.  

        ```python
        # A Python program to return multiple 
        # values from a method using class
        class Test:
            def __init__(self):
                self.str = "myUniqueString"
                self.x = 20  
        
        # This function returns an object of Test
        def fun():
            return Test()
            
        # Driver code to test above method
        t = fun() 
        print(t.str)
        print(t.x)
        ```
        
    - Using Tuple: A Tuple is a comma separated sequence of items. It is created with or without (). Tuples are immutable. See this for details of tuple.

        ```python
        # A Python program to return multiple 
        # values from a method using tuple
        
        # This function returns a tuple
        def fun():
            str = "myUniqueString"
            x = 20
            return str, x;  # Return tuple, we could also
                            # write (str, x)
        
        # Driver code to test above method
        str, x = fun() # Assign returned tuple
        print(str)
        print(x)
        ```
    
    - Using a list: A list is like an array of items created using square brackets. They are different from arrays as they can contain items of different types. Lists are different from tuples as they are mutable. See this for details of list.

        ```python
        # A Python program to return multiple 
        # values from a method using list
        
        # This function returns a list
        def fun():
            str = "myUniqueString"
            x = 20  
            return [str, x];  
        
        # Driver code to test above method
        list = fun() 
        print(list)
        ```
    
    - Using a Dictionary: A Dictionary is similar to hash or map in other languages. See this for details of dictionary.

        ```python
        # A Python program to return multiple 
        # values from a method using dictionary
        
        # This function returns a dictionary
        def fun():
            d = dict(); 
            d['str'] = "myUniqueString"
            d['x']   = 20
            return d
        
        # Driver code to test above method
        d = fun() 
        print(d)
        ```

- In Python, functions are objects so, we can return a function from another function. This is possible because functions are treated as first class objects in Python. 

    ```python
    # Python program to illustrate functions
    # can return another function
    
    def create_adder(x):
        def adder(y):
            return x + y
    
        return adder
    
    add_15 = create_adder(15)
    
    print("The result is", add_15(10))
    
    # Returning different function
    def outer(x):
        return x * 10
    
    def my_func():
        
        # returning different function
        return outer
    
    # storing the function in res
    res = my_func()
    
    print("\nThe result is:", res(10))
    ```

## def

- Python def keyword is used to define a function, it is placed before a function name that is provided by the user to create a user-defined function. In python, a function is a logical unit of code containing a sequence of statements indented under a name given using the “def” keyword. In python def keyword is the most used keyword.
- In the case of classes, the def keyword is used for defining the methods of a class.
- def keyword is also required to define the special member function of a class like `__init__()`.
- The possible practical application is that it provides the feature of code reusability rather than writing the piece of code again and again we can define a function and write the code inside the function with the help of the def keyword. It will be more clear in the illustrated example given below. There can possibly be many applications of def depending upon the use cases. 

    ```python
    # Python3 code to demonstrate
    # def keyword
    
    # function for subtraction of 2 numbers.
    def subNumbers(x, y):
        return (x-y)
    
    # main code
    a = 90
    b = 50
    
    # finding subtraction
    result = subNumbers(a, b)
    
    # print statement
    print("subtraction of ", a, " and ", b, " is = ", result)
    ```

    ```python
    # Python program to print first 10
    # prime numbers
    
    # A function name prime is defined
    # using def
    def prime(n):
        x = 1
        count = 0
        while count < n:
            for d in range(2, x, 1):
                if x % d == 0:
                    x += 1
            else:
                print(x)
                x += 1
                count += 1
    
    # Driver Code
    n = 10
    
    # print statement
    print("First 10 prime numbers are:  ")
    prime(n)
    ```
    
    ```python
    # Python program to find the
    # factorial of a number
    
    # Function name factorial is defined
    def factorial(n):
        if n == 1:
            return n
        else:
            return n*factorial(n-1)
    
    # Main code
    num = 6
    
    # check is the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        print("The factorial of", num, "is", factorial(num))
    ```
## for
 
 - This keyword is used to create a for loop.
## lambda

- Python Lambda Functions are anonymous function means that the function is without a name. As we already know that the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 
- Syntax: lambda arguments: expression
    - This function can have any number of arguments but only one expression, which is evaluated and returned.
    - One is free to use lambda functions wherever function objects are required.
    - You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
    - It has various uses in particular fields of programming, besides other types of expressions in functions.

    ```python
    str1 = 'GeeksforGeeks'
    
    # lambda returns a function object
    rev_upper = lambda string: string.upper()[::-1]
    print(rev_upper(str1))
    ```

# Data types

## True

## False

## None

## strings

## numbers

## floats

## lists