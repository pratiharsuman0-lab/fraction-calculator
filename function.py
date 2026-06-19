'''add_lambda = lambda x,y: x+y
print(add_lambda(6,4))'''

'''def add(x,y):
    return x+y
s=add(5,8)
print(s)'''

'''def even_number():
    s=list()
    for i in range(10,21):
        if i%2==0:
            s.append(i)
    return s 

suman=even_number()  
print(suman)    ''' 


'''def calculator(*args):
  u=sum(args)
  return u
def average(*args):
 return sum(args)/len(args)
calculator()
print(calculator(10,20,30,58))
print(average(14,15,18))'''

'''def max_number(*args):
    maximum=max(args)
    add=sum(args) 
    return maximum,add
s =max_number(10,25,25)
print(type(s))
p=max_number(10,58,36)  
print(p) '''

"""def my_sum(*args):
    total=0
    for i in args:
        total=total + i
    return total

s=my_sum(*range(10,20))
print (s)
"""
'''def factorial_num(num):
    sol=num*factorial_num(num-1)
    return sol

print(factorial_num(5))'''

'''def factorial_num(n):
    # Check if the number 'n' is 0
    if n == 0:
        # If 'n' is 0, return 1 (factorial of 0 is 1)
        return 1
    else:
        # If 'n' is not 0, recursively call the 'factorial' function with (n-1) and multiply it with 'n'
        return n * factorial_num(n - 1)

# Ask the user to input a number to compute its factorial and store it in variable 'n'
n = int(input("Input a number to compute the factorial: "))

# Print the factorial of the number entered by the user by calling the 'factorial' function
print(factorial_num(n))'''


'''def reverse_str(text):
    if len(text)==0:
      return 'invalid '
    else:
       return  text[::-1]

print(reverse_str('suman2005p'))'''

def sum_number(*args):
  if args==str:
     for item in args:
      if  isinstance(args, (int, float)):
       return 'ind'
      else:
        print('pagal')   
     
  else:
      return sum(args)
    
print(sum_number('suman'))    