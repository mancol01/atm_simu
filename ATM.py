'''
File: ATM.py
Author: Mandla Collymore Mangena 
Description: atm simulation
'''
import time

div='-'*58
div2='_'*58
print(div)
accept= ['y','yes','Yes','Y','YES']
reject= ['n','no','No','N','No']
dbpin='1234'
chances=3

#reading from file
filBal=open('dbal2.txt')

fLis=[]
balList=[]

for line in filBal:
    dat=line.strip()
    balList.append(dat)

a=balList[0]
b=balList[1]
c=a.split('_')
d=b.split('_')


balDict=dict(zip(c,d))

###################

es=time.localtime()
timestr1 = time.strftime("%A\t%d %B %Y",es)
timestr2 = time.strftime("%H:%M:%S",es)
print("\nToday's Date:\t\t{0}".format(timestr1))
#######################################

def Welcome():
    print(f'\n[{div}]\n\tWelcome to Mancol Financial House(MFH) Pvt Ltd\n\t\tLog in time:{timestr2}\n[{div}]')
    iniT=input("\nSelect:\n\tOption [1] is you are a client:\n\tOption [2] if you are an admin:\n")
    if iniT=='1':
        print("Entering client Interface:")
        time.sleep(1)
        client()
    elif iniT=="2":
        print("Entering Adminstration Interface:")
        time.sleep(1.5)
        admin()
        
        

############
def admin():
    global username, password
    username=input('Enter your username:\n')
    password=input('Enter your password:\n')
    if password=='password' and username=="username":
        greetAdmn()
        
    return username, password
    
def client(*args):
    global account
    account=input('Enter your account number:\n')
    #account='2021-0001-100-10'
    item_ret(fDict, account)
    greetClient(title, surName)
    #print(account)
    return account
    
    
#######################################

#zto process data in the clientDB atfer generating fDict
db=open('clientDB.txt')

for line in db:
    lin=line.strip()
    fLis.append(lin)
    

lnA=fLis[0]
lnB=fLis[1]
lnC=fLis[2]


LA=lnA.split('_')
LB=lnB.split(',')


SLC=lnC.split('_')
nbl=[]

for e in SLC:
    LC=e.split(',')
    nbl.append(LC)    


listOfD=[]
for i in nbl:
    anot_CL=dict(zip(LB,i))
    listOfD.append(anot_CL)


fDict=dict(zip(LA,listOfD))

def item_ret(*args):
    global firstName, surName, regNumberID, emailAddress, cellNumber, occupation, natIDNum, DateOfBirth, accountType, RegDate, sex, title, account
    for key in fDict:
        #print(key)
        if account not in fDict:
            break
        elif key == account:
            v=fDict[key]
            nested_dict=v
            for ndkey in nested_dict:
                if ndkey=='fName':
                    firstName=nested_dict[ndkey]
                elif ndkey=='sName':
                    surName=nested_dict[ndkey]
                elif ndkey=='reg.I.D':
                    regNumberID=nested_dict[ndkey]
                    
                elif ndkey=='email-address':
                    emailAddress=nested_dict[ndkey]
                elif ndkey=='cell-number':
                    cellNumber=nested_dict[ndkey]
                elif ndkey=='occupation':
                    occupation=nested_dict[ndkey]
                elif ndkey=='nat-I.D.-or-Passport-Num':
                    natIDNum=nested_dict[ndkey]
                elif ndkey=='D.O.B':
                    DateOfBirth=nested_dict[ndkey]
                elif ndkey=='account-type':
                    accountType=nested_dict[ndkey]
                elif ndkey=='Reg-Date':
                    RegDate=nested_dict[ndkey]
                elif ndkey=='sex':
                    sex=nested_dict[ndkey]
                elif ndkey=='title':
                    title=nested_dict[ndkey]
                
                
    try:
        
        return firstName, surName, regNumberID, emailAddress, cellNumber, occupation, natIDNum, DateOfBirth, accountType, RegDate, sex, title, account
    except:
        print("account not found")
    
  

def greetClient(*args):
    #global chances
    ltrs=[]
    for i in firstName:
        ltrs.append(i)
        fc=ltrs[0]
    print(f'\n[{div}]\n\tGreetings \t{title} {fc} {surName} \n\n[{div}]')
    security(chances)
    
    


#############
#############

def pintrial(chances):
    if chances>0:
        security(chances)
    else:
        print(f"{div2}\nNo more chances, your account is suspended!\n{div2}")
        outro()
    pass


def security(chances):
    print(f"Pin chances {chances}")
    pin=input(f'Please enter your pin:\n\t>_\t')
    if pin == dbpin:
        print(f"{div}\n\tPin accepted!\n{div}")
        try:
            print(f"\aACCOUNT TYPE:  >_\t{accountType}")
        except NameError:
            print('ACCOUNT UNKOWN')
        
        print(f"ACCOUNT HOLDER:>_\t{title} {firstName} {surName}\nACCOUNT NUMBER:>_\t{account} ")
        option()
    else:
        print(f"{div}\n\tWrong pin!\n{div}")
        chances-=1
        pintrial(chances)
        
        

#getting balance from dbBal
def getBal(balDict):
    global bal
    for i in balDict:
        if account==i:
            bal=balDict[i]
    bal=float(bal)
    return bal
    

def outro():
    eso=time.localtime()
    tmOut=time.strftime("%H:%M:%S",eso)
    print(f"\n\n[{div2}]\n\tThank you {title} {surName} for doing business with us\n\n\t\t\tGoodbye!\n\t\tLog out time:{tmOut}\n[{div}]")
    time.sleep(1)
    return exit()

def again():
    agn=input("Do you want to transact again? [y] or [n]:\t")
    if agn in accept:
        option()
    elif agn in reject:
        outro()
        
        

#########features client
def withdraw(bal):
    #global bal
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
            retBal(balDict, bal)
            again()
    
    
#returning balance
def retBal(balDict, bal):
    cont1=[]
    cont2=[]
    balax = bal
    try:
        for i in balDict:
            if account==i:
                #print(i)
                balDict[account]=str(balax)
    except RuntimeError:
        print('Working')
        #print(balDict)
        
    #print(balDict)
    for i in balDict.items():
        f=list(i)
        #print(f)
        a=f[0]
        b=f[1]
        #print(a)
        #print(b)
        cont1.append(a)
        cont2.append(b)
        #print(cont1)
        #print(cont2)
        w='_'.join(cont1)
        x='_'.join(cont2)
        #print(w)
        #print(x)
        
        with open('dbal2.txt', 'w+') as file:
            file.write(f"{w}\n{x}")
            
        


def deposit(*args):
    global bal
    print(div2)
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
            retBal(balDict, bal)
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
    

#########
def tryagain():
    t=input('Try again [Yes] or [No]:\t ')
    if t in accept:
        option()
    elif t in reject:
        outro()
    else:
        time.sleep(1)
        print('\n\tOops! unrecognized input\n')
        time.sleep(1)


def atm(opt):
    getBal(balDict)
    print(f'{div}\n\tmy option:\t{opt}\n{div}')
    
    if opt=='1':
        withdraw(bal)
    elif opt=='2':
        deposit()
    elif opt=='3':
        balance()
    else:
        print("invalid input!")
        tryagain()
        

def option():
    global opt
    opt=input('Select an option:\n\tWithdraw money press [1]\n\tDeposit cash press [2]\n\tTo check balance [3]\n\t>_ ')
    atm(opt)
    return opt
    
    

'''

def Query():
    print(f"Account Holders information:\nFullname:\t{title} {firstName} {surName}")
    
    
###################

'''

Welcome()

