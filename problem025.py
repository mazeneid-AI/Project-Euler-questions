#1000-digit Fibonacci Number
#Problem 25
#
#The 12th term, F12, is the first term to contain three digits. What is the index 
#of the first term in the Fibonacci sequence to contain 1000 digits
num1,num2=1,0
index=1
while True:

  fibonacci,num1=num1+num2,num2
  num2=fibonacci
  if len(str(num2))==1000:
    break
  else:
    index+=1
print(index)
