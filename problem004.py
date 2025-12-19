# Largest Palindrome Product, Problem 4
#A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009=91*99
#
#Find the largest palindrome made from the product of two
#3-digit numbers.


def prodect_numbers()->int:
  answer={num1*num2 for num1 in range(100,1000) for num2 in range(100,1000)}
  return answer
  """ product the numbers"""
def largest_palindrome_product()->int:
  list1=[]
  for answer in prodect_numbers():
    """ read the numbers"""
    if answer==int(str(answer)[::-1]):
      """ check if the numbers are palindromes or not"""
      list1.append(answer)
  return(max(list1))
  """ find the largest palindrome number"""
print(largest_palindrome_product())


