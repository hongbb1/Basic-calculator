#setting up our functions for the calculator: 
#key: i=carried value, x=outcome

from fractions import Fraction

def addition(A): 
    z=float(int(A))
    x=i+z 
    return x 
#function for addition 
  
def subtraction(S):
    z=float(int(S))
    x=i-z 
    return x 
#function for subtraction 
 
def multiplication(M):
    z=float(int(M))
    x=i*z 
    return x 
#function for multiplication 
 
def division(D):
    z=float(int(D))
    x=i/z 
    return x 
#function for division 
  
def exponentiation(E):
    z=float(int(E))
    x=i**z 
    return x 
#function for exponentiation 
 
 
#Using the functions when certain conditions are met
def calculate(n):
    global i

    if s=="+": 
        i=addition(n) 
        print (i) 
    #if there’s a “+” sign we use the addition function 
         
    elif s=="-":
        i=subtraction(n) 
        print (i) 
    #if there’s a “-” sign we use the subtraction function
        
    elif s=="*": 
        i=multiplication(n) 
        print (i) 
     #if there’s a problem “*” sign we use the multiplication function

    elif s=="first ^":
        i=exponentiation(t)
        print (i)
    #exception for the first exponential
    
    elif s=="^": 
        i=exponentiation(n) 
        print (i) 
      #if there’s a “^” sign we use the exponential function 
           
    elif s=="/": 
        try: 
            division(n) 
        except: 
            print ("can not divide by zero") 
        else: 
            i=division(n) 
            print (i) 
     #if there’s a “/” sign, we first test if the number can be divided, if it can’t be divided we know the user input is 0 and we tell them that we “can not divide by zero” 
     #Otherwise we use the division function and carry on with the calculation 
 
    elif s=="%": 
        i=modulus(n) 
        print (i) 
      #if there’s a “%” sign we use the modulus function 
   
    else: 
        print ("symbol not in database\n") 
     #if there’s a none number in the input that’s not a symbol we have registered or a mistype we tell the user the symbol is not in our database

        
#main function
w="first ^"
i=0
h=input("number:")
#prompting user for number
try:
    float(h)
except:
    print("use arabic numbers!")
    exit("restart programme")
else:
    i=float(h)
#testing if the input is a number if not let them know
      
o=i
n=1
#saving variables n and o as i for other codes

#loop function accepting calculation from user
for k in range(1000):
    s=input("symbol:")
        
    if s=="^":
        t=float(input("number:"))
        s=w
        i=o
        calculate(n**t)
    
    elif s=="stop":
        break
    
    elif s=="=":
        break

    elif s=="round off":
        print(i//1)

    elif s=="fraction":
        print(o,"/",n)
        print(Fraction.from_float(i))
        
    else:
        m=input("number/bracket:")
        if m=="(":
            i=float(input("number:"))
            v=s
            while s!=")":
                s=input("symbol:")
                if s==")":
                    s=v
                    i=p
                    calculate(b)
                else:
                    j=float(input("number:"))
                    calculate(j)
                    b=i
        else:
            try:
                float(m)
            except:
                print("use arabic numbers!\n")
                continue
            else:
                n=float(m)
                o=i
                calculate(n)
                p=i
                w=s


print("The result is:",i)
