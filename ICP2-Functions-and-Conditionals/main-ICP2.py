# 1.1
def heights_loop():
  """
  function that intakes height in inches until user terminates and converts to cm
  """
  x = "Y"
  hINCH = []
  hCM = []
  while x != 'N':
    x = input("Enter a height in inches (enter N to exit)>> ")
    if x != 'N':
      hINCH.append(int(x))
      hCM.append(int(x) * 2.54)
  print("The heights in inches:", hINCH)
  print("The heights in cms:", hCM)


heights_loop()


# 1.2
def heightComp():
  """
  function that intakes height in inches until user terminates and converts to cm but with list comprehensions
  """
  x = "Y"
  hINCH = []
  while x != 'N':
    x = input("Enter a height in inches (enter N to exit)>> ")
    hINCH.append(x)
  heightsInch = [int(x) for x in hINCH if x != 'N']
  heightsCM = [x * 2.54 for x in heightsInch]
  print("Height in inches:", heightsInch)
  print("Height in cm:", heightsCM)


heightComp()


# 2.
# function that concatenates 2 strings
def fullname(firstName, lastName):
  return firstName + " " + lastName

# function that prints every 'even' indexed char
def string_alternative(myString):
  outString = ""
  for i in range(len(myString)):
    if i % 2 == 0:  # test for eve
      outString += myString[i]
  return outString

# function that asks the user for 2 strings, and then calls fullname()
def intakeNames():
  # get names
  first = input("Enter the first name of a student:")
  last = input("Enter the last name of a student:")
  # print names
  print("The full name of this student is " + fullname(first, last))


# Call the string functions
intakeNames()
print(string_alternative(input("Enter a string to get the alternative digits:")))

# 3.

def countTXT():
  #
  myDict = {}
  phrases = []
  with open("input.txt") as f:
    contents = f.read()
    # myLines
    phrases = contents.split('\n')
    phrases = set(phrases)
    for word in phrases:
      print(word)
    print(contents)
    contents = contents.replace('\n', ' ')
    words = contents.split(' ')
    print(words)
    # iterates through list of words and adds words to dict, increment by one if word is already in dict
    for word in words:
      if word in myDict:
        myDict[word] += 1
      else:
        myDict[word] = 1
  print("Word_Count:")
  with open("output.txt", 'w') as o:
    # write word counts to output file
    o.write("Word_Count:\n")
    for word in phrases:
      o.write(f"{word} \n")
    for key, value in myDict.items():
      print(f"{key}: {value}")
      o.write(f"{key}: {value}\n")


countTXT()
