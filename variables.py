#Variables are containers for storing data values.

x = 5
print(x)

#Variables do not need to be declared with any particular type.
y = 6
y = "Salt"
print(y)

#If you want to specify the data type of a variable, this can be done with casting.
z = str(3)
a = int(7)
print(z)
print(a)

#You can get the data type of a variable with the type() function.
print(type(x))

#String variables can be declared either by using single or double quotes.
name = "Python"
#is same as
name = 'Python'

#Variable names are case-sensitive.
 # c = 10
 # C = "Sally"


#Many Values to Multiple Variables
e, f, g = "elephant", "frog", "girl"
print(e)
print(f)
print(g)

#One Value to Multiple Variables
x = y = z = "Orange"

#unpack a collection
fruits = ["apple", "mango", "grapes"]
h, i , j = fruits
print(h)
print(i)
print(j)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)