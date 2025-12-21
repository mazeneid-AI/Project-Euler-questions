# Self Powers, Problem 48
#The series, 1 1 + 2 2 + 3 3 + ⋯ + 10 10 = 10405071317 .
#Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ⋯ + 1000**1000 .
def limit_of_numbers()->int:
  number,power=1,1
  list1=[]
  while True:
    list1.append(number**power)
    number+=1
    power+=1
    if len(list1)==1000:
      break
  return list1
  """ add all the powered numbers"""
def get_the_last_10_degit()->int:
  list2=[]
  for sum_of_numbers in str(sum(limit_of_numbers())):
    """ Read the number"""
    list2.append(sum_of_numbers)
    the_location_of_numbers=len(list2)-10
    """ get the location of last 10 digit"""
  return("".join(list2[the_location_of_numbers:]))

print(get_the_last_10_degit())
