#19/08/2020
#Alex Thom
Name_Array = []
Price_Array = []

Group_name = input("Please insert the name of your group - ")

Number_of_pupils = int(input("Please insert the number of people in your group - "))

while Number_of_pupils != int:
  print ("ERROR - Please enter a number between 4 and 10")
  Number_of_pupils = int(input("Please insert the number of people in your group - "))

while Number_of_pupils <4 or Number_of_pupils >10:

  print ("ERROR - Please enter a number between 4 and 10")

  Number_of_pupils = int(input("Please insert the number of people in your group - "))

for counter in range(Number_of_pupils):

  Name = input("Please enter a name of a person in your group - ")

  Photo = input("Would this person like their photo taken? Please enter yes or no - ")

  while Photo != 'No' and Photo != 'no' and Photo != 'Yes' and Photo != 'yes':
    print ("Please enter yes or no ")
    Photo = input("Would this person like their photo taken? Please enter yes or no - ")

  if Photo == "No" or Photo == "no":
    price = 3.00

  if Photo == "Yes" or Photo == "yes":
    price = 4.99

  Name_Array.append(Name)
  Price_Array.append(price)


print ("Group Name:",Group_name)
print ("Number in group:",Number_of_pupils)
print ()

for counter in range(Number_of_pupils):
  print (Name_Array[counter],Price_Array[counter])


  






 