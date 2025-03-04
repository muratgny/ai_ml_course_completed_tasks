import random
from datetime import datetime

class Player:
    
    def __init__(self):
        self.name = self.get_player_name()
        self.birthdate, self.age = self.check_age()

    def get_player_name(self):

        while True:
            player_name = input("Please enter your full name (First Name Last Name): ")
            if player_name.replace(" ", "").isalpha() and player_name.count(" ") == 1:
                return player_name
            else:
                print("Invalid input! Please enter a valid name with only one space and no numbers.")

    def get_player_birthdate(self):

        while True:
            player_birthdate = input("Please enter your birthdate in yyyymmdd format : ")

            if len(player_birthdate) == 8 and player_birthdate.isdigit():
                year = int(player_birthdate[:4])
                month = int(player_birthdate[4:6])
                day = int(player_birthdate[6:])
                if year > 1900 and 1 <= month <= 12 and 1 <= day <= 31:
                    return player_birthdate
                else:
                    print("Invalid birthdate! Please check the year, month, or day.")
            else:
                print("Invalid format! Please enter your birthdate in yyyymmdd format.")

    def calculate_age(self, player_birthdate):
        current_year = 2022
        year = int(player_birthdate[:4])
        month = int(player_birthdate[4:6])
        day = int(player_birthdate[6:])
        birthdate = datetime(year, month, day)

        age = current_year - birthdate.year - ((datetime(current_year, month, day) < birthdate) and 1)
        return age

    def check_age(self):
        while True:
            player_birthdate = self.get_player_birthdate()
            player_age = self.calculate_age(player_birthdate)
            if player_age >= 18:
                return player_birthdate, player_age
            else:
                print(f"Sorry, you are under 18! Your age is {player_age}. Please enter a valid birthdate again.")


class LuckyNumberGame:
    def __init__(self):
        self.lucky_list = self.generate_lucky_list()
        self.lucky_number = self.generate_lucky_number()
        self.tries_count = 1
        self.shorter_lucky_list = None

    def generate_lucky_list(self):
        return random.sample(range(101), 9)

    def generate_lucky_number(self):
        """Generates a lucky number and inserts it at a random position in the lucky list."""
        lucky_number = random.randint(0, 100)
        insert_index = random.randint(0, len(self.lucky_list))  # Get a random index
        self.lucky_list.insert(insert_index, lucky_number)  # Insert at random index
        return lucky_number

    def get_player_input(self):
        print("Here is the lucky list: ", self.lucky_list)
        while True:
            try:
                player_input = int(input("Choose the lucky number from the list: "))
                if player_input in self.lucky_list:
                    return player_input
                else:
                    print("Invalid choice! Pick a number from the list.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    def create_or_update_shorter_lucky_list(self, player_input):
        if self.shorter_lucky_list is None:
            self.shorter_lucky_list = [num for num in self.lucky_list if self.lucky_number - 40 <= num <= self.lucky_number + 40]
            return self.shorter_lucky_list

        if player_input in self.shorter_lucky_list:
            self.shorter_lucky_list.remove(player_input)
            return self.shorter_lucky_list

    def ask_new_guess(self):
        print(f"This is try#{self.tries_count} and new list is: {self.shorter_lucky_list}, choose the lucky number?")
        return int(input())

    def handle_correct_guess(self):
        print(f"Congrats, game is over! And you got the lucky number on try#{self.tries_count} :)")
        play_again = input("Do you like to play again? (y: Yes, n: NO): ").lower()
        return play_again == 'y'


def main():
    player = Player()
    print(f"Welcome, {player.name}!")

    while True:
        game = LuckyNumberGame()
        player_input = game.get_player_input()

        while True:
            if player_input == game.lucky_number:
                play_again = game.handle_correct_guess()
                
                if not play_again:
                    print("Thanks for playing!")
                    return  # Exit game
                
                break  # Restart game loop

            game.shorter_lucky_list = game.create_or_update_shorter_lucky_list(player_input)

            if len(game.shorter_lucky_list) <= 2:
                print("Game over! No more valid guesses left.")
                return  # Exit game

            player_input = game.ask_new_guess()
            game.tries_count += 1


if __name__ == "__main__":
    main()