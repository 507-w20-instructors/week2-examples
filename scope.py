# scope.py


#################
## EXAMPLE 1
#################
var1 = 66 # global scope

def func1():
    print("inside function", var1) # global name is valid

func1()
print("outside function", var1)


#################
## EXAMPLE 2
#################
var2 = 77 # global scope

def func2():
    var2 = 88 # local name overrides global
    print("inside function", var2) 

func2()
print("outside function", var2) 


#################
## EXAMPLE 3
#################

def func3():
    var3 = 99 # local name overrides global
    print("inside function", var3) 

func3()
#print("outside function", var3) 


#################
## EXAMPLE 4
#################

def func4(param1):
    print("inside function 1", param1) 
    param1 = 222
    print("inside function 1", param1) 

var4  = 111
func4(var4)
print("outside function", var4) 



#################
## EXAMPLE 5
#################

def func5(var5):
    print("inside function A", var5) 
    var5 = 222
    print("inside function B", var5) 
var5  = 111
func5(var5)
print("outside function", var5) 



#################
## EXAMPLE 6
#################
def func6(var6):
    var6 += " world"
    print(var6, "from func6") 
var6  = "hello"
func6(var6)
print(var6, "from indent level 0") 