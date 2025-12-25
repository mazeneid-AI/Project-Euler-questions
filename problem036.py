#Problem 36
#Double-base Palindromes
#
#The decimal number 585=1001001001 (binary) is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in 
#base 10  and base 2.
def double_base_palindromes()->int:
  number=0
  list1=[]
  while number<1000000:
    number+=1
    if str(number)==str(number)[::-1] and bin(number)[2:]==bin(number)[2:][::-1]:
      list1.append(number)
  return sum(list1)
print(double_base_palindromes())
      

