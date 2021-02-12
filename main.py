''' In terminal or in CMD run some commands
    pip install Ipython
    pip install mysql-connector-python
    pip install matplotlib
'''
from gameModules import *

print()
print('************Welcome to the most famous game in the world***********')
print('********************************TYPER******************************')
print()


#from gameModules import *
import IPython.display

start_game = True

while start_game:
    print()
    print('Choose number to select :)')
    print('1. for Easy Game.')
    print('2. for Normal Game')
    print('3. for Hard Game')
    print('4. for Profile.')
    print('5. for Quit Game.')
    print()
    
    choice = input('Enter choice : ')
    print()
    
    if choice=='1':
        game()

    elif choice=='2':
        normalGame()

    elif choice=='3':
        hardGame()
        
    elif choice=='4':
        profile()
        
    elif choice=='5':
        start_game = False
    
    else:
        print('Warning : please make a correct choice.')
    
    IPython.display.clear_output()