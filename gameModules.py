import mysql.connector
import random
import time
import matplotlib.pyplot as plt



# MySQL version should be more than 5.0.0

try:
    
    '''It will try to connect with database. If dtabas 'tdata' is not found it will give error and go to except.'''
    
    
    #this database query is for you.
#    db = mysql.connector.connect(
#        host = '127.0.0.1',
#        user = 'root',
#        password = '',
#        database = 'TDATA',
#    )



    #this database is for me .

    db = mysql.connector.connect(
        host = 'sql12.freemysqlhosting.net',
        database = 'sql12392475',
        user = 'sql12392475',
        password = 'pl3GWrnplM',
        #port = '3306',
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
    print('This level is not case sensitive.')
    print()
    username = input('Enter your username : ')
    print()
    
    game = True
    
    life = 5
    word_completed = 0
    start_time = time.time()
    temp_end_time = start_time
    
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
            y_values.append(time.time()-temp_end_time)
            temp_end_time = time.time()
        else:
            print('failed to complete task.')
            life -= 1
            
        print()
        
        if life <= 0:
            game= False

    end_time = time.time()
    time_taken = end_time - start_time
    
    print('You have taken ',time_taken,'seconds to complete ',word_completed,' letters')
    plt.plot(x_values,y_values)
    plt.scatter(x_values,y_values)
    plt.xlabel('letters')
    plt.ylabel('time(in seconds).')
    plt.title('Time taken along with letters')
    plt.legend()
    plt.show()
    
    
    cur = db.cursor()
    
    try:
        
        '''this will try to fetch data from PROFILE_DATA if table not exist it will throw error and go in except'''

        cur.execute('SELECT * FROM PROFILE_DATA')
        cur.fetchall()
        cur.execute('SELECT * FROM TIME_TAKEN')
        cur.fetchall()
    except:
        
        '''it will first create table called PROFILE_DATA'''

        cur.execute('CREATE TABLE PROFILE_DATA ( USERNAME varchar(250), TIME_TAKEN decimal(25,6),WORD_COMPLETED int )')
        
        cur.execute('CREATE TABLE TIME_TAKEN ( USERNAME varchar(250), X_VALUE varchar(250),Y_VALUE decimal(25,6) )')
        
    #Out of  try and except 
    cur.execute("INSERT INTO PROFILE_DATA VALUES('%s','%s',%d)"%(username, time_taken,word_completed))
    db.commit()
    print()
    print()
    input('Press any button to continue.')
    
    
    for i in range(len(x_values)):
        cur.execute("INSERT INTO TIME_TAKEN VALUES('%s','%s',%s)"%(username, x_values[i],y_values[i]))
        db.commit()
        
def normalGame():
    print('This level is case sensitive.')
    print()
    username = input('Enter your username : ')
    print()
    
    game = True
    
    life = 5
    word_completed = 0
    start_time = time.time()
    temp_end_time = start_time
    
    x_values = []
    y_values = []
    
    while game:
        
        task = chr(random.randint(65,122))
        print(task)
        ans = input(':')
        
        print()
        if ans==task:
            print('you did it.')
            word_completed +=1
            
            x_values.append(task)
            y_values.append(time.time()-temp_end_time)
            temp_end_time = time.time()
        else:
            print('failed to complete task.')
            life -= 1
            
        print()
        
        if life <= 0:
            game= False

    end_time = time.time()
    time_taken = end_time - start_time
    
    print('You have taken ',time_taken,'seconds to complete ',word_completed,' letters')
    plt.plot(x_values,y_values)
    plt.scatter(x_values,y_values)
    plt.xlabel('letters')
    plt.ylabel('time(in seconds).')
    plt.title('Time taken along with letters')
    plt.legend()
    plt.show()
    
    
    cur = db.cursor()
    
    try:
        
        '''this will try to fetch data from PROFILE_DATA if table not exist it will throw error and go in except'''

        cur.execute('SELECT * FROM PROFILE_DATA')
        cur.fetchall()
        cur.execute('SELECT * FROM TIME_TAKEN')
        cur.fetchall()
    except:
        
        '''it will first create table called PROFILE_DATA'''

        cur.execute('CREATE TABLE PROFILE_DATA ( USERNAME varchar(250), TIME_TAKEN decimal(25,6),WORD_COMPLETED int )')
        
        cur.execute('CREATE TABLE TIME_TAKEN ( USERNAME varchar(250), X_VALUE varchar(250),Y_VALUE decimal(25,6) )')
        
    #Out of  try and except 
    cur.execute("INSERT INTO PROFILE_DATA VALUES('%s','%s',%d)"%(username, time_taken,word_completed))
    db.commit()
    print()
    print()
    input('Press any button to continue.')
    
    
    for i in range(len(x_values)):
        cur.execute("INSERT INTO TIME_TAKEN VALUES('%s','%s',%s)"%(username, x_values[i],y_values[i]))
        db.commit()
        


def hardGame():
    print('This level is case sensitive.')
    username = input('Enter your username : ')
    print()
    
    game = True
    
    life = 5
    word_completed = 0
    start_time = time.time()
    temp_end_time = start_time
    
    x_values = []
    y_values = []
    
    while game:
        
        task = chr(random.randint(65,90))
        for i in range(random.randint(3,9)):
            task += chr(random.randint(65,122))

        print(task)
        ans = input(':')
        
        print()
        if ans==task:
            print('you did it.')
            word_completed +=1
            
            x_values.append(task)
            y_values.append(time.time()-temp_end_time)
            temp_end_time = time.time()
        else:
            print('failed to complete task.')
            life -= 1
            
        print()
        
        if life <= 0:
            game= False

    end_time = time.time()
    time_taken = end_time - start_time
    
    print('You have taken ',time_taken,'seconds to complete ',word_completed,' letters')
    plt.plot(x_values,y_values)
    plt.scatter(x_values,y_values)
    plt.xlabel('letters')
    plt.ylabel('time(in seconds).')
    plt.title('Time taken along with letters')
    plt.legend()
    plt.show()
    
    
    cur = db.cursor()
    
    try:
        
        '''this will try to fetch data from PROFILE_DATA if table not exist it will throw error and go in except'''

        cur.execute('SELECT * FROM PROFILE_DATA')
        cur.fetchall()
        cur.execute('SELECT * FROM TIME_TAKEN')
        cur.fetchall()
    except:
        
        '''it will first create table called PROFILE_DATA'''

        cur.execute('CREATE TABLE PROFILE_DATA ( USERNAME varchar(250), TIME_TAKEN decimal(25,6),WORD_COMPLETED int )')
        
        cur.execute('CREATE TABLE TIME_TAKEN ( USERNAME varchar(250), X_VALUE varchar(250),Y_VALUE decimal(25,6) )')
        
    #Out of  try and except 
    cur.execute("INSERT INTO PROFILE_DATA VALUES('%s','%s',%d)"%(username, time_taken,word_completed))
    db.commit()
    print()
    print()
    input('Press any button to continue.')
    
    
    for i in range(len(x_values)):
        cur.execute("INSERT INTO TIME_TAKEN VALUES('%s','%s',%s)"%(username, x_values[i],y_values[i]))
        db.commit()
        

#profile module is here.
def profile():
    username = input("Enter your username : ")
    
    try:
        
        cur = db.cursor()
        cur.execute("SELECT * FROM PROFILE_DATA WHERE USERNAME='%s'"%(username))
        
        response = cur.fetchall()
        print()
        print('Username : ',username)
        print()

        x_values = []
        y_values = []
        for res in response:
            x_values.append(res[1])
            y_values.append(res[2])
            
        plt.scatter(y_values,x_values)
        plt.ylabel('Time taken')
        plt.xlabel('Number of letters')
        plt.title('Time taken to complete all letters (previous data.)')
        plt.show()
 
        cur.execute("SELECT * FROM TIME_TAKEN WHERE USERNAME='%s'"%(username))
        
        response2 = cur.fetchall()
        print()
        x_values2 = []
        y_values2 = []
        for res in response2:
            x_values2.append(res[1])
            y_values2.append(res[2])

        print()
        print('To see detailed data.')
        last_values_to_see = int(input('Number of last values to see : '))
        print()

        filtered_x_values = []
        filtered_y_values = []
        if (len(x_values2) >= last_values_to_see+1):
            for i in range(len(x_values2) - last_values_to_see,len(x_values2)):
                filtered_x_values.append(x_values2[i])
                filtered_y_values.append(y_values2[i])

        else:
            filtered_x_values = x_values2
            filtered_y_values = y_values2

        print('Lines are there to detect last position.')
        print()

        plt.plot(filtered_x_values,filtered_y_values)
        plt.scatter(filtered_x_values,filtered_y_values)
        plt.xlabel('letter')
        plt.ylabel('Time taken')
        plt.title('Time taken by individual letter.')
        plt.show()
        
    except:
        print('Table not found in database.')

    input('Press any key to continue.')
    