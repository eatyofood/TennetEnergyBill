import pandas as pd
import os
from datetime import datetime
import pretty_errors


print('...............................................................')
print("               _   _ _ _ _                                ")
print(" _____ _____  | | | (_) | | __ _ _ __ _   _   _____ _____ ")
print("|_____|_____| | |_| | | | |/ _` | '__| | | |s|_____|_____|")
print("|_____|_____| |  _  | | | | (_| | |  | |_| | |_____|_____|")
print("              |_| |_|_|_|_|\__,_|_|   \__, |              ")
print("                                      |___/               ")
print("...............[ Electric Bill Calculator ]...................")
print('==========================================================')

# Tennet Refrence Sheets
rpath = 'refrence_data.csv' 

   
def add_tennets():
    done = False
    tenli= []

    while done == False:
        ten = str(input('Enter tennet name:'))

        if 'done' in ten.lower():
            print('Cool! moving on')
            done = True
        else:
           tenli.append(ten) 
           tdf = pd.DataFrame(tenli,columns=['TENNETS:'])
        print(tdf)


    return tdf

# First Run Though
if not os.path.exists(rpath):
    print('there is no tennet list ...') 
    print('   1) enter the names of the tennets. ')
    print('   2) type "done" & press enter when you are done')
    tdf = add_tennets()
    tdf.to_csv(rpath)

print('')
print('====================================================')
print('1) To Add Or Remove Tenants: ')
print('        - add or remove rows in spreadsheet labeled :"refrence_data.csv"')

total_bill = None
meter_used = None

# Define Variables For Calculator
while (type(total_bill) != float) and (type(meter_used) != float):
    
    try:
        total_bill = float(input('ENTER TOTAL BILL AMMOUNT:...........:'))
        meter_used = float(input('ENTER TOTAL METER USED..............:'))
        print('===========================================================')
    except BaseException as b:
        print(b)
        print('\n\nsomething broke but i still love you ...')


#Price To Write Calculation
ppw = total_bill / meter_used
print('Price Per Watt:',ppw)
print('============================================================')
print('')
print('')


tdf = pd.read_csv(rpath)



tennets = tdf['TENNETS:']

print(f'tennets: {tennets}')





puli = []
for t in tennets:
    tdic = {}
    print('---------------------------------------------')

    print('TENNET:',t)
    print(f'how much power did {t} use?')
    pu = int(input('POWER_USED:'))
    
    # Tennet Info 
    tdic['tennet'] = t 
    tdic['usage']  = pu
    # bill ammount
    amt            = pu * ppw
    tdic['bill']   = amt
    print(f'{t} used: {pu} watts , you should bill them ${amt}')
    print('++++++++++++++++++++++++++++++++++++++++++++')

    puli.append(tdic)


today = str(datetime.now().date())

df = pd.DataFrame(puli)#.set_index('TENNETS:')
df['price_per_watt'] = ppw
df['date'] = today 

print(df)

bill_name = today + '.csv'
df.to_csv(bill_name)


print('\n\n\n==yeet!==\n\n')


