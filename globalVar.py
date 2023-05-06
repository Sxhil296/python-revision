# variables outisde the function
# can be used anywhere

x = "awesome"

# def myfunc():
#     print("Python is " + x)
# myfunc()


"""If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function.
 The global variable with the same name will remain as it was, 
 global and with the original value."""


def myfunc():
    #global x - to changfe the value of global variable
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)



#To create a global variable inside a function, you can use the global keyword.

def func():
    global x
    x = "amazing"
func()
print(x)