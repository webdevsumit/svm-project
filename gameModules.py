import mysql.connector
import random
import time
import matplotlib.pyplot as plt



# MySQL version should be more than 5.0.0

try:
    
    '''It will try to connect with database. If dtabas 'tdata' is not found it will give error and go to except.'''

    db = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'TDATA',
    )
except:
    
    '''first it will connect with MySQL than create a database called tdata.'''
    
    db = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
    )
    
    cur = db.cursor()
    
    cur.execute('CREATE DATABASE TDATA')
    cur.execute('USE TDATA')
    


#main game function 
def game():
    username = input('Enter your username : ')
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
    time_taken = end_time - start_time
    
    print('You have taken ',time_taken,'seconds to complete ',word_completed,' words')
    plt.plot(x_values,y_values)
    plt.show()
    
    
    cur = db.cursor()
    
    try:
        
        '''this will try to fetch data from PROFILE_DATA if table not exist it will throw error and go in except'''

        cur.execute('SELECT * FROM PROFILE_DATA')
         cur.execute('SELECT * FROM TIME_TAKEN')
    except:
        
        '''it will first create table called PROFILE_DATA'''

        cur.execute('CREATE TABLE PROFILEDATA ( USERNAME varchar(250), TIME_TAKEN varchar(250),WORD_COMPLETED int )')
        
        cur.execute('CREATE TABLE TIME_TAKEN ( USERNAME varchar(250), X_VALUE int,Y_VALUE int )')
        
    #Out of  try and except 
    cur.execute("INSERT INTO PROFILE_DATA(%s,%s,%d)"%(username, str(time_taken),word_completed))
    db.commit()
    
    
    for i in range(len(x_values)):
        cur.execute("INSERT INTO TIME_TAKEN(%s,%s,%d)"%(username, x_values[i],y_values[i]))
        db.commit()
        


#profile module is here.
def profile():
    username = input("Enter your username : ")
    
    cur = db.cursor()
    result = cur.execute("SELECT * FROM PROFILE_DATA WHERE USERNAME='%s'"%(username))
    