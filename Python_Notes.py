#*************************************************************************
#String formatting

#Python 3
age = 24
print("My age is {0} years".foramt(age))
print("My age is {0:12.50f} years".foramt(age)) #string formatting is python 3

#Python 2
print("My age is %d years" % age)

#*************************************************************************
#If, elif, else processing
if 15 < age < 66: #Python supports ineqality on both sides
    print("Have a good day at work")

# any non-zero, non-empty value evaluates as true in if-statements
x = "false"
if x:
    print("It's true")

if not(age < 18): #not() is a keyword that inverse the logic
    print("You are old enough to vote")


#*************************************************************************
#For loops
for i in range(1, 20): # range does not include the last number
     print(i)
x = range(0, 100, 5) # 3rd argument is step

for item in shopping_list:
    if item == 'spam':
        continue        #continue bypass the block of code and move on to next iteration
        break           #break stops the loop

#*************************************************************************
#Augmented Assignment
greeting = 'Good '
greeting += "morning" #Concatinates the string
# greeting = "Good morning"
x = 23
x += 1  #x+1
x -= 4  #x-4
x *= 5  #x*5
x **= 2 #x**2 square

#*************************************************************************
#list
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd #appends a sequence
numbers.sort()  #sorts a sequence, does not return the list
numbers_in_order = sorted(numbers) #sorted function sorts a sequence, return the sequence

list_1 = []
list_2 = list() #Both options constructs a list
list("ABCDE") #creates a list from each character of the string ['A', 'B', 'C', 'D', 'E']

#*************************************************************************
#iterator, this is what for loop creates behind the scence
string = "1234567890"
my_iterator = iter(string)  #creates an iterator
next(my_iterator) #iterates to the next item in the string, ex: 2

#*************************************************************************
#range
print(range(10)) #range with a single parameter give a range starting from 0
# range(10) = range(0,10)
even = list(range(0,10,2)) #this creates a list [0,2,4,6,8]

#range consume small amount of memory, but creating a list from the range will take a lot more memory in Python3
even = range(0,10)
print(even.index(3)) #index works for range

sevens = range(7, 1000000, 7)
if x in sevens:
    print("is divisible by seven") # xxx in xxx works for range as well

sevens[::2] #[::2] the 2 columns default start/stop, with a step of 2
range(0, 5, 2) == range(0, 6, 2) #range eqaulity depends on the sequence values, not how it is presented
range(0, 100)[::-2] == range(99, 0, -2) #slicing step of -2 steps backward from the appends

#*************************************************************************
#tuples
#tuples are immutable, meaning the content cannot be changed
t = 'a', 'b', 'c' #This creates a tuple, () is used to differentiate between list and tuple
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975 #Tuple can contain different data types, list cannot

 #tuple supports indexing and slicing
welcome = welcome[0], "Alex Shao", welcome[2] #This gets around the immutable property

title, artist, year = welcome #extract content of the tuple, called UNPACKING
#UNPACKING works with list as well

#*************************************************************************
#Binary & Hex
x = 0x20 #0x indicates a hex number
x = 0b00101010 #0b indicates a binary number

#*************************************************************************
#Dictionary
