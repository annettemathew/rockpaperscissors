#Question 2
# Write a class called Rock_paper_scissors that implements the logic of
# the game Rock-paper-scissors. For this game the user plays against the computer
# for a certain number of rounds. Your class should have fields for how many rounds
# there will be, the current round number, and the number of wins each player has.
# There should be methods for getting the computer’s choice, finding the winner of a round,
# and checking to see if someone has won the (entire) game. You may want more methods.

from random import randint
exit_flag = False
class Rock_paper_scissors:
    def __init__(self, choice):
        self.choice = choice
        self.list = ['r', 'p', 's']
    def generate_comp_response(self):
        rand_int = randint(0, 2)
        print("Computer generated: ", self.list[rand_int])
        return self.list[rand_int]
    def check_win(self, choice, c_choice):
        if(choice == c_choice):
            print("Draw")
            return
        if(choice == 'r'):
            if(c_choice == 'p'):
                print('Computer won')
            else: #computer picked scissors
                print('User won')
        elif(choice == 'p'):
            if(c_choice == 'r'):
                print('User won')
            else: #computer picked scissors
                print('Computer won')
        else: #user picked scissors
            if(c_choice == 'r'):
                print('Computer won')
            else: #Computer picked paper
                print('User won')
print("Hi! Welcome to Rock Paper Scissors!")
while(exit_flag == False):
    user_choice = input("Please enter r, p, s, or x(to exit): ")
    user_choice = user_choice.lower()
    if(user_choice == 'x'):
        exit(0)
    elif(user_choice != 'r' and user_choice != 'p' and user_choice != 's'):
        print("Error: incorrect input")
        exit(-1)
    Rps = Rock_paper_scissors(user_choice)
    comp_choice = Rps.generate_comp_response()
    Rps.check_win(user_choice, comp_choice)