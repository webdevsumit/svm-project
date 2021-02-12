print()
print('************Welcome to the most famous game in the world***********')
print('********************************TYPER******************************')
print()


from gameModules import *
import IPython.display

start_game = True

while start_game:
    print()
    print('Choose number to select :)')
    print('1. for New Game.')
    print('2. for Profile.')
    print('3. for Quit Game.')
    print()
    
    choice = input('Enter choice : ')
    print()
    
    if choice=='1':
        game()
        
    elif choice=='2':
        print('profile')
        
    elif choice=='3':
        start_game = False
    
    else:
        print('Warning : please make a correct choice.')
    
    IPython.display.clear_output()