class Employee:
  #Declare an Employee class with properties such as id, name, dept, salary, employment status
    def __init__(self, iden, n, dept, sal):
        self.id = iden
        self.name = n
        self.department = dept
        self.salary = sal
        self.balance = 0
        self.isEmployed = True

    def pay(self):
      #pays employee their salary/adds salary to their balance
        self.balance += self.salary

    def fire(self):
      #fire employee, employement status = not employed
        self.isEmployed = False

class Full_time(Employee):
  #child class of Employee for Full-time
    def __init__(self, iden, n, dept, sal):
        Employee.__init__(self, iden, n, dept, sal)

    def give_raise(self, amt=1.1):
      #default raise for full time is a 10% increase
      #Increase salary by amt
        self.salary *= amt

class Part_time(Employee):
  #child class of Employee for Part-time
    def __init__(self, iden, n, dept, sal):
      Employee.__init__(self, iden, n, dept, sal)

    def give_raise(self, amt=1.05):
      #default raise for part time is a 5% increase
      #increase salary by amt
      self.salary *= amt


def actionCommand(command, empDict):
  #Takes in one line of the text file as a list and the employee dictionary
  action = command[0]
  if action == 'NEW':
    #creates a new employee and adds to the employee dictionary
    #initialize what each element in the command list is
    iden = command[1]
    name = command[2] + ' ' + command[3]
    dept = command[4]
    sal = int(command[-2])
    #salary needs to be an int since we'll be calculating balances/avg salaries
    employment = command[-1]

    if employment == 'F':
      #employment is full-time, creates an instance of fulltime to add to employee dictionary
      empDict[iden] = Full_time(iden, name, dept, sal)
  
    elif employment == 'P':
      #employment is part-time, creates an instance of parttime to add to employee dictionary
      empDict[iden] = Part_time(iden, name, dept, sal)

  elif action == 'PAY':
    #iterates through employee dictionary and pays each employee
    for emp in empDict:
      empDict[emp].pay()
      #print(empDict[emp].name, "was paid")

  elif action == "RAISE":
    #Gives given employee a raise
    iden = command[1] #The id number is the dictionary key for easy access
    if len(command) == 3:
      raiseAmt = int(command[-1])
      empDict[iden].give_raise(raiseAmt)
    else:
      empDict[iden].give_raise()

  elif action == "FIRE":
    #Fires employee and sets their employement status to False
    iden = command[1] #The id number is the dictionary key for easy access
    #print(empDict[iden].name, "was fired")
    empDict[iden].fire()

  return empDict #Need to return the employee dictionary to update it

def getAvg(empDict, classType):
  """
  Input: empDict (employee dictionary to get the salaries), classType is our conditional
  Output: avg salary of the list of salaries filtered by the classType
  """
  empSalaries = [empDict[x].salary for x in empDict if type(empDict[x]) == classType]
  return "{:.2f}".format(sum(empSalaries)/len(empSalaries))


def outPutInfo(empDict, fout):
  """
  Input: empDict to get the dictionary of employees, fout is our output file
  Output: Outputs to output text file, calls getAvg function to get avg salaries for each of the subclass types, and iterates through the dictionary to output each employee and their info
  """
  fired = 0
  avgFSal = getAvg(empDict, Full_time)
  avgPSal = getAvg(empDict, Part_time)

  for emp in empDict:
    name = empDict[emp].name
    iden = empDict[emp].id
    dept = empDict[emp].department
    sal = "{:.2f}".format(empDict[emp].salary)
    bal = "{:.2f}".format(empDict[emp].balance)
    empStatus = empDict[emp].isEmployed

    if (type(empDict[emp]) == Full_time):
      FP = 'Full-Time'
    else:
      FP = 'Part-Time'

    fout.write(f"{name}, {iden}, {dept}:\n")
    fout.write(f'Current salary: ${sal}\n')
    if empStatus == False:
      fout.write("Not employed with the company.\n")
      fired += 1
    fout.write(f'Pay earned to date: ${bal}\n')
    fout.write(FP+'\n')
    fout.write('\n')
    
  fout.write(f'Total number of employees: {len(empDict)-fired}\n')
  fout.write(f'Average Salary paid to all Full-time employees: ${avgFSal}\n')
  fout.write(f'Average Salary paid to all Part-time employees: ${avgPSal}\n')

with open('output.txt', 'w') as fout:
  with open('input.txt', 'r') as fin:
    empDict = {}
    header = fin.readline() #read in the header
    contents = fin.read() #the rest are commands we need
    lines = contents.split('\n') #split up the commands by newline
    for command in lines: 
      info = command.split(' ') #Split the command by spaces to get the info
      empDict = actionCommand(info, empDict) #Call the actionCommand function to do an action with each of the command line//also updates the empDict within the function

    outPutInfo(empDict, fout) #Output the information to the output file
    

import requests
from bs4 import BeautifulSoup

#get link we're gonna parse through
html = requests.get("https://en.wikipedia.org/wiki/Machine_learning")
#get the HTML 'soup'
ML = BeautifulSoup(html.content, "html.parser")
#Get the title of the wiki
print(ML.title.string, '\n')
#for loop through all of the img tags
for img in ML.find_all('img'):
  #print src for each img
  print(img.get('src'))
  