#importing libraries
import mysql.connector 
import PySimpleGUI as sg
import time as dt


#making connection
mydb = mysql.connector.connect(host="localhost",user="root",passwd="dadapython",database="school")
cursor=mydb.cursor()
currentstdid=0
ctecid=0


#generatins student's id
def getstdid():
  cursor=mydb.cursor()
  exe='select max(id) from c6 '
  cursor.execute(exe)
  d = cursor.fetchall()

  return int(d[0][0])+1


#generatins Teacher's id
def gettecid():
  cursor=mydb.cursor()
  exe='select max(id) from teacher '
  cursor.execute(exe)
  d = cursor.fetchall()

  return int(d[0][0])+1




#Getting Date
dt=dt.strftime("%d/%m/%Y")
#Theme
sg.LOOK_AND_FEEL_TABLE['Theme'] = {'BACKGROUND': '#edc464',
                                        'TEXT': '#4f3510',
                                        'INPUT': '#ffffff',
                                        'TEXT_INPUT': '#4f3510',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('white', '#4f3510'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 3, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }

sg.theme('Theme')

    



#login window
def login():
    user='1'
    passw= '1'

    layout = [ [sg.Text('Welcome to School Management System')],
               [sg.Text('Please Login To Continue')],
               [sg.Text('Username',size=(10,1)),sg.Input(key='user')],
               [sg.Text('Password',size=(10,1)),sg.Input(key='pass')],
               [sg.Button('Login')],
               [sg.Text(size=(40,2),key = 'warn')]
              ]
    window = sg.Window('Holy Cross Sr. Sec.,Kapa',layout)
    while True :
        event,values = window.read()
       
        user = values['user']
        passw = values['pass']

        if event == 'Login':
                if user == 'admin' and passw == 'admin':
                      window.close()
                      admin()
                elif user == 'teacher' and passw == 'teacher' :
                      window.close()
                      teacher()
                elif user == 'student' and passw == 'student' :
                      window.close()
                      student()
                else :
                      print('Unknown User \nPlease register yourself')
                      window['warn'].update('Unknown User \nPlease register yourself')
        elif event == sg.WIN_CLOSED:
            window.close()


#admin login
def admin() :
    
    print ('Welcome admin')
    layout =[
        [sg.Button('Add Student',size=(20,1)),sg.Button('Remove Student',size=(20,1))],
        [sg.Button('Add Teacher',size=(20,1)),sg.Button('Remove Teacher',size=(20,1))],
        [sg.Button('Pay Salary',size=(20,1)),sg.Button('Student Fees',size=(20,1))],
        [sg.Button('Student Profile',size=(20,1)),sg.Button('Teacher Profile',size=(20,1))],
        [sg.Button('Logout',size=(10,1))]
            ]
    window = sg.Window('Holy Cross Sr. Sec.,Kapa',layout)
    while True :
        event,values = window.read()

        if event == 'Add Student' :
            window.close()
            addstd()
        elif event == 'Remove Student' :
            window.close()
            rmvstd()
        elif event == 'Remove Teacher' :
            window.close()
            rmvtec()
        elif event == 'Add Teacher' :
            window.close()
            addtec()
        elif event == 'Pay Salary' :
            window.close()
            tecsal()
        elif event == 'Student Fees' :
            window.close()
            stdfeeadm()
        elif event == 'Student Profile':
            window.close()
            stdproadm()
        elif event == 'Teacher Profile':
            window.close()
            tecpro()
        elif event == 'Logout' or event == sg.WIN_CLOSED :
            window.close()
            login()





#teacher Login
def teacher():
    print('Teacher Logined')
    layout =[[sg.Button('Student Profile',size=(20,1)),sg.Button('Give Homework',size=(20,1))],
             [sg.Button('Logout',size=(10,1))]
            ]
    window = sg.Window('Holy Cross Sr. Sec.,Kapa',layout)
    while True :
        event,values=window.read()

        if event == 'Student Profile':
            window.close()
            stdprotec()
        elif event == 'Give Homework':
            window.close()
            givehw()
        elif event == 'Logout' or event == sg.WIN_CLOSED :
            window.close()
            login()


#Student Login
def student():
    print('Student Logined')
    layout = [[sg.Button('Pay Fees',size=(20,1)),sg.Button('Check Homework',size=(20,1))],
              [sg.Button('Logout',size=(10,1))]   

            ]
    window = sg.Window('Holy Cross Sr. Sec.,Kapa',layout)
    while True :
        event,values = window.read()

        if event == 'Pay Fees':
            window.close()
            stdfeestd()
        elif event == 'Check Homework':
            window.close()
            seehw()
        elif event == 'Logout' or event == sg.WIN_CLOSED :
            window.close()
            login()




#addstudent
def addstd():
    newstdid=getstdid()
    print('Adding Student')
    layout = [[sg.Text('Student ID',size=(15,1)),sg.Text('%s'%newstdid,key='sid',size=(15,1))],
              [sg.Text('Name',size=(15,1)),sg.Input(key='sname')],
              [sg.Text('Roll No.',size=(15,1)),sg.Input(key='rollno')],
              [sg.Text('DOB(yyyy/mm/dd)',size=(15,1)),sg.Input(key='dob'),sg.CalendarButton('Calendar',format=('%Y-%m-%d'))],
              [sg.Text('Fees',size=(15,1)),sg.Input(key='fees')],
              [sg.Text('Marks',size=(15,1)),sg.Input(key='marks')],
              [sg.Button('Add',size=(10,1)),sg.Button('Quit',size=(10,1))]

    ]
    window = sg.Window('Add Student',layout)
    while True :
        event,values = window.read()
        window['sid'].update(newstdid)

        if event == 'Add' :
          try:
            sid = newstdid
            sname = values['sname']
            rollno = values['rollno']
            dob = values['dob']
            fees = values['fees']
            marks = values['marks']
            temp = (sid,sname,rollno,dob,fees,marks)
            cursor=mydb.cursor()
            s='insert into c6 (id,name,roll,dob,fees,marks) values(%s,%s,%s,%s,%s,%s)'
            cursor.execute(s,temp)
            mydb.commit()
            sg.popup('Student added successfully')
            window.close()
            addstd()
          except Exception :
            sg.popup('Wrong input')
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            admin()


#add Teacher
def addtec():
    newtecid=gettecid()
    print('Adding Teacher')
    layout = [[sg.Text('Teacher ID',size=(15,1)),sg.Text('%s'%newtecid,key='Tid',size=(15,1))],
              [sg.Text('Name',size=(15,1)),sg.Input(key='Tname')],
              [sg.Text('Subject',size=(15,1)),sg.Input(key='subject')],
              [sg.Text('salary',size=(15,1)),sg.Input(key='salary')],
              [sg.Button('Add',size=(10,1)),sg.Button('Quit',size=(10,1))]
    ]
    window = sg.Window('Add Teacher',layout)
    while True :
        event,values = window.read()
        window['Tid'].update(newtecid)

        if event == 'Add' :
          try:
            tid = newtecid
            tname = values['Tname']
            Sub= values['subject']
            salary= values['salary']
            temp = (tid,tname,Sub,salary)
            cursor=mydb.cursor()
            s='insert into teacher(id,name,subject,salary) values(%s,%s,%s,%s)'
            cursor.execute(s,temp)
            mydb.commit()
            sg.popup('Teacher added successfully')
            window.close()
            addtecj()
          except Exception:
            sg.popup('Wrong input')
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            admin()
               


#Remove Student
def rmvstd():
    print('Removing Student')
    layout = [[sg.Text('Student ID',size=(15,1)),sg.Input(key='sid')],
              [sg.Button('Remove',size=(10,1)),sg.Button('Quit',size=(10,1))]
    ]
    window = sg.Window('Remove Student',layout)
    while True :
        event,values = window.read()

        if event == 'Remove' :
          try:
            sid = values['sid']
            cursor=mydb.cursor()
            temp=(sid,)
            s='Delete from c6 where id = %s'
            cursor.execute(s,temp)
            mydb.commit()
            sg.popup("HCKP",'Student with id %s was removed successfully'%sid)
          except Exception:
            sg.popup('Wrong input')
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            admin()



#Remove Teacher
def rmvtec():
    print('Removing Teacher')
    layout = [[sg.Text('Teacher ID',size=(15,1)),sg.Input(key='tid')],
              [sg.Button('Remove',size=(10,1)),sg.Button('Quit',size=(10,1))]
    ]
    window = sg.Window('Remove Teacher',layout)
    while True :
        event,values = window.read()

        if event == 'Remove' :
            tid = values['tid']
            cursor=mydb.cursor()
            temp=(tid,)
            s='Delete from teacher where id = %s'
            cursor.execute(s,temp)
            mydb.commit()
            sg.popup("HCKP",'Teacher with id %s was removed successfully'%tid)
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            admin()

#Profile of Student By Teacher
def stdprotec():
    print('See Student Profile')
    layout = [[sg.Text('Student ID',size=(15,1)),sg.Input(key='sid')],
              [sg.Button('See Profile',size=(15,1)),sg.Button('Quit',size=(15,1))],
              [sg.Text('Name',size=(10,1)),sg.Text('Roll no.',size=(10,1)),sg.Text('DOB',size=(8,1)),sg.Text('Fees',size=(6,1)),sg.Text('Marks',size=(4,1))],
              [sg.Text(key='name',size=(10,1)),sg.Text(key='rollno',size=(10,1)),sg.Text(key='dob',size=(8,1)),sg.Text(key='fees',size=(6,1)),sg.Text(key='marks',size=(4,1))],
    ]
    window = sg.Window('Student Profile',layout)
    while True :
        event,values = window.read()

        if event == 'See Profile' :
          try:
            sid = values['sid']
            cursor=mydb.cursor()
            temp=(sid,)
            s='select * from c6 where id = %s'
            cursor.execute(s,temp)
            d = cursor.fetchall()
            for i in d :
                print(i)
                window['name'].update(i[1])
                window['rollno'].update(i[2])
                window['dob'].update(i[3])
                window['fees'].update(i[4])
                window['marks'].update(i[5])
          except Exception :
            sg.popup('Wrong Sid')
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            teacher()
            


#Profile of Student by Student
def stdproadm():
    print('See Student Profile')
    layout = [[sg.Text('Student ID',size=(15,1)),sg.Input(key='sid')],
              [sg.Button('See Profile',size=(15,1)),sg.Button('Quit',size=(15,1))],
              [sg.Text('Name',size=(10,1)),sg.Text('Roll no.',size=(10,1)),sg.Text('DOB',size=(8,1)),sg.Text('Fees',size=(6,1)),sg.Text('Marks',size=(4,1))],
              [sg.Text(key='name',size=(10,1)),sg.Text(key='rollno',size=(10,1)),sg.Text(key='dob',size=(8,1)),sg.Text(key='fees',size=(6,1)),sg.Text(key='marks',size=(4,1))],
    ]
    window = sg.Window('Student Profile',layout)
    while True :
        event,values = window.read()

        if event == 'See Profile' :
            sid = values['sid']
            cursor=mydb.cursor()
            temp=(sid,)
            s='select * from c6 where id = %s'
            cursor.execute(s,temp)
            d = cursor.fetchall()
            for i in d :
                print(i)
                window['name'].update(i[1])
                window['rollno'].update(i[2])
                window['dob'].update(i[3])
                window['fees'].update(i[4])
                window['marks'].update(i[5])
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            admin()
            



#Profile of Teacher
def tecpro():
    print('See Teacher Profile')
    layout = [[sg.Text('Teacher ID',size=(15,1)),sg.Input(key='sid')],
              [sg.Button('See Profile',size=(15,1)),sg.Button('Quit',size=(15,1))],
              [sg.Text('Name',size=(10,1)),sg.Text('Subject',size=(10,1)),sg.Text('Salary',size=(8,1))],
              [sg.Text(key='name',size=(10,1)),sg.Text(key='sub',size=(10,1)),sg.Text(key='Salary',size=(8,1))],
    ]
    window = sg.Window('Teacher Profile',layout)
    while True :
        event,values = window.read()

        if event == 'See Profile' :
            sid = values['sid']
            cursor=mydb.cursor()
            temp=(sid,)
            s='select * from teacher where id = %s'
            cursor.execute(s,temp)
            d = cursor.fetchall()
            for i in d :
                print(i)
                window['name'].update(i[1])
                window['sub'].update(i[2])
                window['Salary'].update(i[3])
               
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            admin()
            



#Salary Of teacher
def tecsal():
    print('Give Salary to Teacher')
    layout = [[sg.Text('Teacher ID',size=(15,1)),sg.Input(key='tid')],
              [sg.Text('Date',size=(15,1)),sg.Text(key='dt',size=(15,1))],
              [sg.Button('Give salary',size=(15,1)),sg.Button('Quit',size=(15,1))]
    ]
    window = sg.Window('Teacher salary',layout)
    while True :
        event,values = window.read()
        window['dt'].update(dt)
        if event == 'Give salary' :
            tid = values['tid']
            date = dt
            cursor=mydb.cursor()
            temp=(tid,'PAID',date)
            s='insert into salary (id,status,date) values(%s,%s,%s)'
            cursor.execute(s,temp)
            mydb.commit()
               
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            admin()







#Fees of Student by student
def stdfeestd():
    print('Pay Fees')
    layout = [[sg.Text('Your Student ID',size=(15,1)),sg.Input(key='sid')],
              [sg.Text('Date',size=(15,1)),sg.Text(key='dt',size=(15,1))],
              [sg.Button('Pay Fees',size=(15,1)),sg.Button('Quit',size=(15,1))]
    ]
    window = sg.Window('Pay Fees',layout)
    while True :
        event,values = window.read()
        window['dt'].update(dt)
        if event == 'Pay Fees' :
            sid = values['sid']
            date = values['Date']
            cursor=mydb.cursor()
            temp=(sid,'PAID',date)
            s='insert into fees (id,fees,date) values(%s,%s,%s)'
            cursor.execute(s,temp)
            mydb.commit()
               
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            student()



#Fees of Student by Admin
def stdfeeadm():
    print('Pay Fees')
    layout = [[sg.Text('Student ID',size=(15,1)),sg.Input(key='sid')],
              [sg.Text('Date',size=(15,1)),sg.Text('%s'%dt,key='dt',size=(15,1))],
              [sg.Button('Pay Fees',size=(15,1)),sg.Button('Quit',size=(15,1))]
    ]
    window = sg.Window('Pay Fees',layout)
    while True :
        event,values = window.read()
        window['dt'].update(dt)
        if event == 'Pay Fees' :
            sid = values['sid']
            date = values['d+t']
            cursor=mydb.cursor()
            temp=(sid,'PAID',date)
            s='insert into fees (id,fees,date) values(%s,%s,%s)'
            cursor.execute(s,temp)
            mydb.commit()
               
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            admin()




#see Hw
def seehw():
    print('See homework')
    layout = [[sg.Text('Class',size=(15,1)),sg.Input(key='clas')],
              [sg.Button('See Homework',size=(15,1)),sg.Button('Quit',size=(15,1))],
              [sg.Text('English',size=(10,1)),sg.Text('Hindi',size=(10,1)),sg.Text('Maths',size=(8,1)),sg.Text('Science',size=(6,1)),sg.Text('SST',size=(4,1)),sg.Text('CS',size=(4,1))],
              [sg.Text(key='eng',size=(10,1)),sg.Text(key='hindi',size=(10,1)),sg.Text(key='math',size=(8,1)),sg.Text(key='sci',size=(6,1)),sg.Text(key='sst',size=(4,1)),sg.Text(key='cs',size=(4,1))],
    ]
    window = sg.Window('Student Homework',layout)
    while True :
        event,values = window.read()

        if event == 'See Homework' :
            clas = values['clas']
            cursor=mydb.cursor()
            temp=(clas,)
            s='select * from hw where class = %s'
            cursor.execute(s,temp)
            d = cursor.fetchall()
            for i in d :
                print(i)
                window['eng'].update(i[1])
                window['hindi'].update(i[2])
                window['math'].update(i[3])
                window['sci'].update(i[4])
                window['sst'].update(i[5])
                window['cs'].update(i[6])
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            login()





#Give Homework
def givehw():
    print('Homework')
    layout = [[sg.Text('class',size=(15,1)),sg.Input(key='clas')],
              [sg.Text('English',size=(15,1)),sg.Input(key='eng')],
              [sg.Text('Hindi',size=(15,1)),sg.Input(key='hindi')],
              [sg.Text('Maths',size=(15,1)),sg.Input(key='math')],
              [sg.Text('Science',size=(15,1)),sg.Input(key='sci')],
              [sg.Text('SST',size=(15,1)),sg.Input(key='sst')],
              [sg.Text('CS',size=(15,1)),sg.Input(key='cs')],
              [sg.Button('Done',size=(15,1)),sg.Button('Quit',size=(15,1))]

    ]
    window = sg.Window('Give Homework',layout)
    while True :
        event,values = window.read()

        if event == 'Done' :
          
            eng = values['eng']
            hindi = values['hindi']
            math = values['math']
            sci = values['sci']
            sst = values['sst']
            cs = values['cs']
            clas = values['clas']
            try:
              temp = (clas,eng,hindi,math,sci,sst,cs)
              cursor=mydb.cursor()
              s='insert into hw (class,eng,hindi,maths,science,sst,cs) values(%s,%s,%s,%s,%s,%s,%s)'
              cursor.execute(s,temp)
              mydb.commit()
            except Exception:
              temp =(eng,hindi,math,sci,sst,cs,clas)
              cursor=mydb.cursor()
              s='update hw set eng=%s, hindi=%s,maths=%s,science=%s,sst=%s,cs=%s where class=%s'
              cursor.execute(s,temp)
              mydb.commit()
            finally:
              sg.popup('Homework Distributed')
            
        elif event == 'Quit' or event == sg.WIN_CLOSED :
            window.close()
            teacher()
            





# initializing 
login()

