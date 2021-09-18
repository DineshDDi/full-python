print("Welcome to ICICI Bank ATM")
Restart = 'Q'
Chance = 3
Balance = 1560.45
while Chance >= 0:
    pin = int(input("Please enter your PIN:  "))
    if pin == (1004):
        while Restart not in ('NO:1', 'NO:2', 'NO:3', 'NO:4'):
            print('Press 1 for your Bank Balance \n')
            print('Press 2 to make withdrawl \n')
            print('Press 3 to Deposit in \n')
            print('Press 4 to Return Card \n')
            Option = int(input('What Would like to choose : '))
            if Option == 1:
                print('Your Account Balance is $', Balance, '\n')
                Restart = input('Go Back : ')
                if Restart in ('NO:1', 'NO:2', 'NO:3', 'NO:4'):
                    print('Thank You')
                    break
            elif Option == 2:
                Option2 = ('Q')
                withdrawl = float(input('How much you like to withdrawl? \n$100/$200/$500$2000'))
                if withdrawl in [100, 200, 500, 2000]:
                    Balance = Balance - withdrawl
                    print('\n Your Account Balance is now: ', Balance)
                    Restart = input('Go Back : ')
                    if Restart in ('NO:1', 'NO:2', 'NO:3', 'NO:4'):
                        print('Thank You')
                        break
                elif withdrawl != [100, 200, 500, 2000]:
                    print('Invaild Amount, Please re-try \n')
                    Restart = ('Q')
            elif Option == 3:
                Deposit_in = float(input('Please! enter the Deposit Amount: '))
                Balance = Balance + Deposit_in
                print('\n Your Balance is now $: ', Balance)
                Restart = input('Go Back : ')
                if Restart in ('NO:1', 'NO:2', 'NO:3', 'NO:4'):
                    print('Thank You')
                    break
            elif Option == 4:
                print('Please wait your card as been return \n')
                print('Thank You')
                break
    elif pin != ('1004'):
        print('Incorect Password')
        Chance = Chance-1
        if Chance == 0:
            print('\n NO more Chances, Please collect your Card')
            break




