import pyfiglet as pyg
from datetime import datetime



'''
-------> Birth Date PROJECT <-------

Project descraption:
This project is for one of the "Full Stack Python" Courses 
which consists of several courses and each course contains a simple project,
provided by SATR Platform



Credit to Abdullah AlOwais
Email: aalowais@outlook.sa
'''


def valDate(input): # -> Function to Validating The Date
    try:
        dateObject=datetime.strptime(input, '%d-%m-%Y')
        return True

    except ValueError:
        return False



def convertToDictionary (userInput): # -> Function to Convert User Input to Dictionary

    for i in range(0,len(userInput)-1,2): # Convert The Date From String to Date in "'%d-%m-%Y'" Format

        peopleInformation.update({userInput[i]:datetime.strptime(userInput[i+1], '%d-%m-%Y')})



def ageCalculator(birthdate): # -> Function to Calculate Age

    today = datetime.today() # Today's Date

    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    return age



def dictionaryPrint(): # Function to Display peopleInformation

    if(len(peopleInformation) >= 1):

        for name,age in peopleInformation.items():

            print(" {} is {} Years Old And She/He Was Born on {} ".format(name, ageCalculator(age),age.strftime('%A')))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    else:
        print("No One Found!\nTotal People: ",len(peopleInformation))

    print("---------------------------------------------------\n")



def dictionaryReverse(): # Function to Reverse peopleInformation

    if(len(peopleInformation) >= 1):

        for i,j in reversed(peopleInformation.items()):

            print(i)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    else:
        print("No One Found!\nTotal People: ",len(peopleInformation))
    
    print("---------------------------------------------------\n")



def dictionarySorting(): # -> Function To Sort peopleInformation

    sortedDict = sorted(peopleInformation.items(),key= lambda t:t[1])

    for i in range(len(sortedDict)):
        print(i+1,")",sortedDict[i][0],"\n")

    if(len(sortedDict) <= 1):
        print("There is No Oldest Or Youngest Person")

    else:
        print("The Oldest One is ",sortedDict[0][0])
        print ("The Youngest One is ",sortedDict[-1][0])

    print("\nTotal People: ",len(sortedDict),"\n---------------------------------------------------\n")
    


# -> Main Program Start From Here

peopleInformation={}       
userInput=[]
numOfPeople="" # To Store Number of People The User Want to Insert


print (pyg.figlet_format('Birth Date Calculator',font='slant')) # Program Header

print('''            ----------------------------------------------------------
                     >>> Welcome to Birth Date Calculator <<<
            ----------------------------------------------------------
            ''')


while(True): # Loop To Check if The User Input was a Number or no

    numOfpeople=input("How Many People Do You Want To Enter? ")

    if(numOfpeople.isdigit() and int(numOfpeople) > 0 ): 
        print('---------------------------------------------------')
        break
    
    else:
        print("---------------------------------------------------")
        print("  >>> Wrong Choice! Try Again <<<")
        print("---------------------------------------------------\n")



for i in range(0,2*int(numOfpeople),2): # Loop to Input The People Name and Age 

        userInput.append(input("Enter The Name: "))
        userInput.append(input("Enter Birth Date in This Format \"dd-mm-yyyy\" : "))
        
        if(valDate(userInput[i+1]) == True):
            convertToDictionary(userInput) # if The Date is Validated Add the Information 
        else:
            print("\n",userInput[i]," \Is Entered a Invalid date!")
            userInput.pop()

        print("---------------------------------------------------\n")



while(True): # Loop to Control The Program
    
    print("  1 -> Sort People Information\n" 
    "\n  2 -> Reverse The Input\n"+
    "\n  3 -> Print The Age And in Which Day She/He Was Born \n"+
    "\n  0 -> Exit\n")

    choice= input("\n please Enter your Choice : ")
    print("\n---------------------------------------------------")
 

    if choice in ['0','1','2','3']:

        if choice == "1":
            dictionarySorting()

        elif choice == "2":
            dictionaryReverse()

        elif choice == "3":
            dictionaryPrint()

        elif choice == "0":
            print("----------------------\n"+
                "   >> Thank You! <<   \n"+
                "     >>> Bye! <<<     \n"+
                "----------------------\n")
            break #end the program
    else:
        print("---------------------------------------------------")
        print("  >>> Wrong Choice! Try Again <<<")
        print("---------------------------------------------------\n")
                
  


