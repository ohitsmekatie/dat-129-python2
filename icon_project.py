# get 100 numbers from a user that will eventually build a 10x10 icon  


def get_input(): 
    ''' a function that explains the program, asks for 100 characters in groups of 10, then returns 1 list'''

    print(''' Welcome to the icon printing program. You will enter 100 characters, in groups of 10, that represent your icon and then it will print out a beautiful terminal based picture. Please only enter 1's and 0's. A 1 represents a space you want filled in and a 0 represents an empty space.\n\n''') 

    #create an empty list to add input to
    icon_list = []
    # set number to 0 so i can incrememt for the while loop
    num = 0
    # while loop that, while number is not 10 continues to ask a user for 10 numbers
    while num != 10:
        string = input("Please entier ten 1's and 0's with no spaces: ")
        # for char in string:
        #     if char != "1" and char != "0":
        #         string = input("Sorry! You entered numbers that weren't a 1 or 0. Please enter ten 1's and 0's with no spaces: ")
        #         # reset number to 0 and make them start again
        #         num = 0
        num += 1
        icon_list.append(string)
        string = ""
    #print(icon_list)
    return icon_list 


def transform_list(a_list):
    ''' a function that takes in a list and transform it to a new list of symbols so it can be printed'''
    
    # empty list to add symbols to 
    transformed_list = []
    # for loop that iterations over each set of strings in the list 
    for item in a_list:
        # nested for loop to iterate over each character in the string and checks if it's a 1 or 0 
        for char in item:
            if char == "1":
                transformed_list.append("x")
            if char == "0":
                transformed_list.append(" ")
            if char != "1" and char != "0":
                # me lazily handling a non 1 or 0 for right now 
                transformed_list.append("ERROR")
    return(transformed_list)

    
def visualize_list(a_transformed_list):
    ''' a function that takes a transformed symbol list and prints it, 10 characters at a time to form the user's icon '''

    for item in a_transformed_list[0:9]:
        print(item, end="")
    print("\t")
    for item in a_transformed_list[10:19]:
        print(item, end="")
    print("\t")
    for item in a_transformed_list[20:29]:
        print(item, end="")
    print("\t")
    for item in a_transformed_list[30:39]:
        print(item, end="")
    print("\t")
    for item in a_transformed_list[40:49]:
        print(item, end="")
    print("\t")
    for item in a_transformed_list[50:59]:
        print(item, end="")
    print("\t")
    for item in a_transformed_list[60:69]:
        print(item, end="")
    print("\t")
    for item in a_transformed_list[70:79]:
        print(item, end="")
    print("\t")
    for item in a_transformed_list[80:89]:
        print(item, end="")
    print("\t")
    for item in a_transformed_list[90:99]:
        print(item, end="")
    print("\t")

  
def main():
    ''' main function to call all other functions '''

    icon_list = get_input() 
    transformed_list = transform_list(icon_list)
    visualize_list(transformed_list)


if __name__ == "__main__":
    main()

