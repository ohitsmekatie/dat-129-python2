# https://technologyrediscovery.net/python/mod-icons.html


def get_input(): 
    ''' a function that explains the program, asks for 100 characters in groups of 10, then returns 1 list'''

    print(''' Welcome to the icon printing program. You will enter 100 characters, in groups of 10, that represent an icon and then it will print out a beautiful terminal based picture for you. 
    
    Please only enter 1's and 0's. A 1 represents a space you want filled in and a 0 represents an empty space.\n\n''') 

    #create an empty list to add input to
    icon_list = []
    # set number to 0 so i can incrememt for the while loop
    counter = 0
    # while loop that, while number is not 10 continues to ask a user for 10 numbers
    while counter != 10:
        string = input("Please enter ten 1's and 0's with no spaces: ")
        # make sure there aren't any letters 
        while any(char.isalpha() for char in string) is True:
            print("Input can only contain 1's and 0's and no letters!")
            string = input("Please enter ten 1's and 0's with no spaces: ")
        # check the length of the string to make sure it's 10
        if len(string) != 10:
            print("Sorry, it needs to be ten numbers!")
            # substract from number so the user still has to enter something 10 times
        if len(string) == 10:
            counter += 1
            icon_list.append(string)
            string = ""
    #formatting 
    print("\n\n")
    return icon_list 


def transform_list(a_list):
    ''' a function that takes in a list and transforms it to a new list of symbols so it can be printed'''
    
    # empty list to add symbols to 
    transformed_list = []
    # for loop that iterations over each set of strings in the list 
    for item in a_list:
        # nested for loop to iterate over each character in the string and checks if it's a 1 or 0 
        for char in item:
            if char == "1":
                transformed_list.append(" x ")
            if char == "0":
                transformed_list.append("   ")
            if char != "1" and char != "0":
                # fall back bc i didn't handle non 1's and 0's in the user input function 
                transformed_list.append("ERROR")
    return(transformed_list)


def invert_list(a_list):
    ''' a function that takes in a list and transform it to a new list of symbols so it can be printed, but inverted from the original icon'''
    
    # empty list to add symbols to 
    inverted_list = []
    # for loop that iterations over each set of strings in the list 
    for item in a_list:
        # nested for loop to iterate over each character in the string and checks if it's a 1 or 0 
        for char in item:
            if char == "1":
                inverted_list.append("  ")
            if char == "0":
                inverted_list.append(" x ")
            if char != "1" and char != "0":
                # me lazily handling a non 1 or 0 for right now 
                inverted_list.append("ERROR")
    return(inverted_list)


def visualize_list(a_list):
    ''' a function that takes a transformed symbol list and prints it, 10 characters at a time to form the user's icon '''

    counter = 0
    for item in a_list:
         print(item, end="")
         counter += 1
         if counter % 10 == 0:
            print("\t")

# stubbing out the scale function if i do want to implement this later
#  def scale_list(a_list):
#     scale_size = int(input("How much would you like to scale the icon: "))
#     for row in a_list:
#         for vert_rep in range(0,scale_size):
#             for char in row:
#                 for horz_rep in range(0,scale_size)

  
def main():
    ''' main function to call all other functions '''

    # my_icon = ["1","1","1","1","1","1","1","1","1","1","1","1","0","0","1","1","0","0","1","1","1","1","0","0","1","1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","0","1","0","1","0","1","1","1","0","1","0","1","0","1","0","1","1","1","0","1","0","1","0","1","0","1","1","1","0","1","0","1","0","1","0","1","1","1","0","1","0","1","0","1","0","1","1","1","0","1","0","1","0","1","0","1","1"]
    icon_list = get_input() 
    transformed_list = transform_list(icon_list)
    inverted_list = invert_list(icon_list)
    print("Your icon:\n")
    visualize_list(transformed_list)
    print("\nYour inverted icon:\n")
    visualize_list(inverted_list)

    # my_icon = transform_list(my_icon)
    # visualize_list(my_icon)

if __name__ == "__main__":
    main()

