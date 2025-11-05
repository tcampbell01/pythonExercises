def getNumber():

    number_str = input("Please enter a number: ")

    print("You chose: " + number_str)
    
    convertStringToNum(number_str)
    
def convertStringToNum(number_str):
    
    number_int = int(number_str)
    print(f"The number is now an int.  It is: {number_int}")
    
    evenOrOdd(number_int)
    

def evenOrOdd(number_int): 
    
    if number_int % 2 == 0:
        print(f"{number_int} is an even number")
    else:
        print(f"{number_int} is an odd number")
        

getNumber()








    
    