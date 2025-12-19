#Special Pythagorean Triplet ,Problem 9
#A Pythagorean triplet is a set of three natural numbers, 𝑎 < 𝑏 < 𝑐 , for which,
#For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2 .
#There exists exactly one Pythagorean triplet for which 𝑎 + 𝑏 + 𝑐 = 1000 .
#Find the product 𝑎 𝑏 𝑐
import math
side1=1
side2=1
while True :
  The_hypotenuse_of_a_triangle=math.sqrt((side1**2) + (side2**2))
  if The_hypotenuse_of_a_triangle== int(The_hypotenuse_of_a_triangle):
    the_sum=(The_hypotenuse_of_a_triangle+side1+side2)
    if the_sum==1000:
      print (int((side1*side2*The_hypotenuse_of_a_triangle)))
      break
    side1+=1
  else:
    side1+=1
    if side1==1000:
      side2+=1
      side1=1
