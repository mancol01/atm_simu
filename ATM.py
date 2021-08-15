'''
File: ATM.py
Author: Mandla Collymore Mangena 
Description: atm simulation
'''
import time

div='-'*50
div2='_'*50
print(div)
accept= ['y','yes','Yes','Y','YES']
reject= ['n','no','No','N','No']
dbpin='1234'
chances=3


try:
    b=open('bal.txt')
    
except:
    b=open('bal.txt','w')
    b.write('20')
finally:
    b=open('bal.txt','r+')
        
    
for line in b:
    bal=line.strip()
         

bal=float(bal)


def greet():
    print(f'\n{div}\nGreetings\nWelcome to Mancol Financial House(MFH) Pvt Ltd\n{div}')
    
    
    

def tryagain():
    t=input('Try again [Yes] or [No]:\t ')
    if t in accept:
        option()
    elif t in reject:
        outro()
            
def option():
    global opt
    opt=input('Select an option:\n\tWithdraw money press [1]\n\tdeposit cash press [2]\n\tTo check balance [3]\n\t>_ ')
    atm(opt)
    return opt
    
    
def pintrial(chances):
    if chances>0:
        security(chances)
    else:
        print(f"{div}\nNo more chances, your account is suspended!\n{div}")
        outro()
    pass



def security(chances):
    print(f"Pin chances {chances}")
    pin=input(f'Please enter your pin:\n\t>_\t')
    if pin == dbpin:
        print(f"Pin accepted!")
        option()
        #atm(opt)
    else:
        print("Wrong pin!")
        chances-=1
        pintrial(chances)
        
        

def again():
    agn=input("Do you want to transact again? [y] or [n]")
    if agn in accept:
        option()
    if agn in reject:
        outro()
        
        

def withdraw(*args):
    global bal
    if bal <= float(10.00):
        print(f"Insufficent balance, you have ${bal} remaining")
    elif bal >float(10.00):
        amt=input('Enter the amount you want to withdraw:\n\t>_ ')
        amt=float(amt)
        if (bal-amt)<10:
            print("You can't withdraw amount greater than your balance\n")
            again()
        else:
            bal-=amt
            print("Successfully withdrawn :-)\nYour current balance is ${0}".format(bal))
            b.seek(0)
            b.truncate()
            print(bal)
            b.write(str(bal))
            again()
    
    


def deposit(*args):
    global bal
    print(div)
    print('\n\tMaximum deposit per day is $500.00\n')
    print(div)
    dep=input('Enter the amount you want to deposit:\n')
    dep=float(dep)
    if dep>float(500.00):
        print(f"You can't deposit ${dep}, it's over your daily limit")
        again()
    else:
            bal+=dep
            print("Successfully deposited :-)\nYour current balance is ${0}".format(bal))
            b.seek(0)
            b.truncate()
            print(bal)
            b.write(str(bal))
            again()


def balance(*args):
    global bal
    if bal>=float(15):
        time.sleep(1)
        print("Your account is very sufficient :-)\nYour current balance is ${0}".format(bal))
        time.sleep(2)
        again()
    elif bal<15 and bal>10:
        time.sleep(1)
        print("Your account is sufficient :-|\nYour current balance is ${0}".format(bal))
        time.sleep(2)
        again()
    elif bal<=10:
        time.sleep(1)
        print("Your account is insufficient :-(\nYour current balance is ${0}".format(bal))
        time.sleep(2)
        again()
    


def outro():
    print(f"Thank you for doing business with us\nGoodbye!\n{div}")
    time.sleep(1)
    return exit()



def atm(opt):
    print('my option:',opt)
    
    if opt=='1':
        withdraw(bal)
    elif opt=='2':
        deposit()
    elif opt=='3':
        balance()
    else:
        print("invalid input!")
        tryagain()
        
greet()
security(chances)


