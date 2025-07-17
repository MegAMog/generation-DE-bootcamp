#Menu class
from menus.utils import clear_screen

class Menu:
        def __init__(self, title:str, label:str, options:dict):
            self.title = title
            self.label = label
            self.options = options


        #Method for menu interface: prints avelaible menu options.
        def print_menu_options(self):
            clear_screen()
            print(f"\n{self.title}")

            for key, value in self.options.items():
                print(f"{key}. {value[0]}")


        #Get valid user input for menu options.
        def get_choice(self):
            while True:
                choice = input(f"\nSelect an option from {self.label} menu: ")
                if choice in self.options:
                    return choice
                else:
                    print("\nInvalid choice. Please try again.")


        #Menu interface: handles orders menu navigation and user actions.
        def call_menu(self):
            while True:
                self.print_menu_options()
                user_input = self.get_choice()

                if user_input!="0":
                    self.options[user_input][1]()
                    input("Press Enter to continue.")
                else:
                    return
