#Linear Search

#Creating a list...
Avengers=["Tony Stark","Steve Rogers","Thor Odinson","Bruce Banner","Natasha Romanoff"]

#Defining the Search Function...
def linear_search():
    for i in range(len(Avengers)):
        if user_input==Avengers[i]:
            return i

#Getting the input from user for search context...
user_input=input("Enter the name: ")
 
#Checking whether the input value is valid or not....
if linear_search() is None:
    print("Please, enter the correct name!!!")
else:
    print(" Index position of entered name is at : ",linear_search())
    