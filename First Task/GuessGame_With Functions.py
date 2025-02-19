def get_player_name():
    while True:
        player_name = input("Please enter your full name (First Name Last Name): ")
        # Check if the input is a valid full name (only characters and one whitespace between names)
        if player_name.replace(" ", "").isalpha() and player_name.count(" ") == 1:
            return player_name
        else:
            print("Invalid input! Please enter a valid name with only one space and no numbers.")


def get_player_birthdate():
    while True:
        player_birthdate = input("Please enter your birthdate (yyyymmdd): ")
        # Validate if the input matches the correct format and range
        if len(player_birthdate) == 8 and player_birthdate.isdigit():
            year = int(player_birthdate[:4])
            month = int(player_birthdate[4:6])
            day = int(player_birthdate[6:])
            # Check if the year is after 1900, valid month, and valid day (simplified validation)
            if year > 1900 and 1 <= month <= 12 and 1 <= day <= 31:
                return player_birthdate
            else:
                print("Invalid birthdate! Please check the year, month, or day.")
        else:
            print("Invalid format! Please enter your birthdate in yyyymmdd format.")


from datetime import datetime

def calculate_age(player_birthdate):
    current_year = 2022
    year = int(player_birthdate[:4])
    month = int(player_birthdate[4:6])
    day = int(player_birthdate[6:])
    
    birthdate = datetime(year, month, day)
    age = current_year - birthdate.year - ((datetime(current_year, month, day) < birthdate) and 1)
    return age


def check_age():
    while True:
        player_birthdate = get_player_birthdate()
        player_age = calculate_age(player_birthdate)
        if player_age >= 18:
            return player_birthdate, player_age
        else:
            print(f"Sorry, you're under 18 years old! Your age is {player_age}. Please enter valid birthdate again.")


import random

def generate_lucky_list():
    return random.sample(range(101), 9)  # Generates 9 unique random integers between 0 and 100


def generate_lucky_number(lucky_list):
    lucky_number = random.randint(0, 100)
    lucky_list.append(lucky_number)
    return lucky_number


def get_player_input(lucky_list):
    print("Here is the lucky list: ", lucky_list)
    while True:
        try:
            player_input = int(input("Choose the lucky number from the list: "))
            if player_input in lucky_list:
                return player_input
            else:
                print("Invalid choice! Pick a number from the list.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def generate_shorter_lucky_list(lucky_list, lucky_number, player_input, shorter_lucky_list=None):
    # If this is the first wrong guess, create the shorter lucky list
    if shorter_lucky_list is None:
        shorter_lucky_list = [num for num in lucky_list if lucky_number - 10 <= num <= lucky_number + 10]
    
    # If player's guess is in the list, remove it
    if player_input in shorter_lucky_list:
        shorter_lucky_list.remove(player_input)
    
    return shorter_lucky_list


def ask_new_guess(shorter_lucky_list, tries_count):
    print(f"This is try#{tries_count} and new list is: {shorter_lucky_list}, choose the lucky number?")
    player_input = int(input())
    return player_input


def handle_correct_guess(tries_count):
    print(f"Congrats, game is over! And you got the lucky number on try#{tries_count} :)")
    play_again = input("Do you like to play again? (y: Yes, n: NO): ").lower()
    return play_again == 'y'  # Returns True if the player wants to restart

#todo - error is here
def update_shorter_lucky_list(lucky_list, shorter_lucky_list, lucky_number, player_input):
    # If this is the first wrong guess, create a shorter lucky list
    if shorter_lucky_list is None:
        shorter_lucky_list = [num for num in lucky_list if lucky_number - 40 <= num <= lucky_number + 40]
        return shorter_lucky_list
    
    # If the wrong guess is in the shorter list, remove it
    if player_input in shorter_lucky_list:
        shorter_lucky_list.remove(player_input)
        return shorter_lucky_list



def main():
    player_name = get_player_name()
    player_birthdate, player_age = check_age()
    
    while True:  # Game restart loop
        lucky_list = generate_lucky_list()
        lucky_number = generate_lucky_number(lucky_list)
        tries_count = 1
        shorter_lucky_list = None  # Initialize as None
        player_input = get_player_input(lucky_list)


        while True:

            if player_input == lucky_number:
                if handle_correct_guess(tries_count):  
                    break  # Restart game loop
                else:
                    print("Thanks for playing!")
                    return  # Exit game

            # If wrong guess, generate or update the shorter lucky list
            shorter_lucky_list = update_shorter_lucky_list(lucky_list, shorter_lucky_list, lucky_number, player_input)

                    # If only 2 numbers are left, game over
            if len(shorter_lucky_list) <= 2:
                        print("Game over! No more valid guesses left.")
                        return  # Exit game
                    
            new_Input = ask_new_guess(shorter_lucky_list, tries_count)

            player_input = new_Input
            tries_count += 1  # Increment attempt count

            continue    



if __name__ == "__main__":
    main()
        