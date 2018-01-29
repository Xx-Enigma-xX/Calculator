import re

from fraction import Fraction
import calculator

class Menu:
    '''
    Display a menu and respond to choices.
    '''
    def __init__(self):
        print("initialized")
        self.fractionRegex = re.compile(r'\((\d+)/(\d+)\)')
        self.signRegex = re.compile(r'[\+|\-|\*]')
        # self.calculator = calculator.Calculator()
        self.choice = {
                "1": self.new_session,
                "2": self.quit}
        ''' optional
        "3": self. list_sessions,
        "4": self.save_session,
        "5": self.load_session'''

    def display_menu(self):
        print('''

    Notebook menu
    -------------
    1. Start a new session.
    ?. List all sessions.
    2. Quit.

    ''')

    def run(self):
        ''' Display the menu and respond to choices.'''
        self.display_menu()
        userInput = input()
        # userInput = '1'
        # print(self.choice)
        self.choice[userInput]()

    def new_session(self):
        ''' a session represents the screen you see when you open
        a calculator program on linux or windows. (or a physical one!)

        this week, we will only be dealing with calculating fractions.
        you should tell the user to encase the fractions in brackets,
        then extract the fractions for calculation purposes.

        once inside a session,

        prompt the console to print the current value, initialized as 0.
        just like a regular calculator, usage will be as follows.

        user types (15/4)+(12/13)
        user types enter
        program calculates, saves into a last_result variable.
        program prints the last_result variable.
        program prompts to continue or exit
        if continued, program displays and types ANS
        (representing the last_result variable.)
        program proceeds.

        the calculation will require you to recognize a fraction from
        user input, then call the add()/subtract()/multiply()/divide()
        functions from the Calculator class.

        '''
        userInput = input('Enter your mathematical expression: ')
        # userInput = '(15/4)+(12/13)'
        fractions = self.fractionRegex.findall(userInput)
        # print(fractions)
        fraction1 = Fraction(fractions[0][0], fractions[0][1])
        fraction2 = Fraction(fractions[1][0], fractions[1][1])
        self.calculator = calculator.Calculator(fraction1, fraction2)
        sign = self.signRegex.findall(userInput)
        # print(sign)
        if sign == None:
            result = self.calculator.divide()
            print("(%s/%s)" % (result.numerator, result.denominator))
        elif sign[0] == "+":
            result = self.calculator.add()
            print("(%s/%s)" % (result.numerator, result.denominator))
        elif sign[0] == "-":
            result = self.calculator.subtract()
            print("(%s/%s)" % (result.numerator, result.denominator))
        elif sign[0] == "*":
            result = self.calculator.multiply()
            print("(%s/%s)" % (result.numerator, result.denominator))
        else:
            print("Incorrect input.")

    def quit():
        sys.exit(0)

'''
save/load/list sessions will require you to add an extra layer of data
that saves a session to a session_id and is able to list and load past sessions.

this is an optional exercise, will be done in class together if not complete.

good luck!

'''

menu = Menu()
menu.run()
