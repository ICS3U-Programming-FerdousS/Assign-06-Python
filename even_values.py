# Created by: Ferdous Sediqi
# Created on: May. 31. 2022
# created by: Ferdous Sediqi
# This program asks the user for list of integer
# then append it to a list then using a seprate function we find
# even values inside the list.


# function to find the even value
def even_values(list_of_int):
    list_of_even_value = []
    #  for each loop to find the even numbers from the list
    for a_number in list_of_int:
        if (a_number % 2 == 0):
            list_of_even_value.append(a_number)
    print("You entered ", list_of_int)
    return list_of_even_value


def main():
    # declare the list
    list_of_int = []

    # using while loop to ask for numbers
    while True:
        # Ask user to input their number
        user_num = input("Enter the number into the list: ")

        # cast input to int
        try:
            # Casting to int
            user_num_as_int = int(user_num)
            list_of_int.append(user_num_as_int)
        except Exception:
            # If the user enters a invalid input
            print("Invalid input. Input was not an integer.")
            print("")

        # ask user if they want to enter another number
        next_number = input("To continue press y. To quit enter any key: ")

        # check for user answer        
        if next_number != "y":
            break

    # call the function and display the even numbers
    display_even = even_values(list_of_int)
    print("The even values of list are:", display_even)


if __name__ == "__main__":
    main()
