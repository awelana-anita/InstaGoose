import random
class Profile :
   def __init__ (self, uniqueId, userName, userInfo) :
        
       self.uniqueId = uniqueId # This is a unique identifier given by the system randomly 
       self.userName = userName #The user choses his username
       self.userInfo = userInfo # The user chooses the information he will like to display
       self.privacyLevel = "Only Followers" #This property is assigned when the instance of the class is created and not selected by the user.
   def __str__(self) :
    return "ID :" + str(self.uniqueId) + ", Username : " + self.userName+ ", Info : " + str(self.userInfo)
        
   def getUniqueId(self) :
    return self.uniqueId

   def getUserName(self) :
    return self.userName

   def getUserInfo(self) :
    return self.userInfo

def findPerson (listOfProfiles , targetIdentifier) :
    for profile in listOfProfiles :
        if profile.getUniqueId == targetIdentifier:
           return profile
    else : 
        return None
# This function above is used to find a profile in the lists of profiles using the unique id each user has. If the unique Id is found the function returns the profile but if it is not teh function returns nothing.


def main () :
    profiles = []  
    # this is a list to contain all the profiles ever created.
    command = " "
    while command != "quit" :
        print(" Welcome to InstaGoose!\n Would you like to perform any of the following commands?")
        print("_________________________________________________")
        print("Add, if you would like to Add a New Profile.")
        print("View, if you would like to View an already existing profile.")
        print("Quit, if you would like to Quit.")
        print("_________________________________________________")

        command = input("Enter a command : ").lower()

        if command == "add" :
            # This is to create a new profile by collecting information.
           uniqueId = random.randint(100000,999999)
           userName = input("Enter a username: ")
           userInfo = input("Enter what you would like people to know about you: ")

           profile = Profile(uniqueId, userName, userInfo)
           
           profiles.append(profile)
           print("Congrats on creating a profile with ID:")
           print(profile)
        
        elif command == "view" :
           search = input("Enter your ID: ")
           profile = findPerson(profiles, int(search))
           
           for profile in profiles:
                if profile :
                   print("Your profile exists")
                   print(profile)
                else :
                    print("A profile with ID :" + search + " cannot be found")
        
        elif command == "quit" :
             print ("You have quit InstaGoose.We look forward to your return next time")
             break

    else :
        print ("The command you entered does not exist. Please select either add, view or quit")   
       
if __name__ == "__main__" :
    main()
