import mysql.connector
import random
import time
import matplotlib.pyplot as plt

#mydb = mysql.connector.connect(
#    host = 'sql12.freemysqlhosting.net',
#    user = 'sql12392374',
#    password = 'yTucD2kgLw',
#    port = '3306',
#    database = 'sql12392374',
#)



def game():
    username = input('Username : ')
    print()
    
    game = True
    
    life = 5
    word_completed = 0
    start_time = time.time()
    
    x_values = []
    y_values = []
    
    while game:
        
        task = chr(random.randint(65,90))
        print(task)
        ans = input(':')
        
        print()
        if ans.upper()==task:
            print('you did it.')
            word_completed +=1
            
            x_values.append(task)
            y_values.append(time.time()-start_time)
        else:
            print('failed to complete task.')
            life -= 1
            
        print()
        
        if life <= 0:
            game= False
    end_time = time.time()
    
    print('You have taken ',end_time - start_time,'seconds to complete ',word_completed,' words')
    plt.plot(x_values,y_values)
    plt.show()