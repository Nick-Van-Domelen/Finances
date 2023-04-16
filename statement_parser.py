import pandas as pd
import numpy as np
import sys
import os
import Categories as cat

# Read in CSV file and create pandas dataframe
df = pd.read_csv(sys.argv[1])

#strip out unnecessary columns from the dataframe
df = df.drop(['Transaction','Memo'], axis=1)

#Add column that keeps track of if a line item has been accounted for in a dictionary
df = df.assign(Accounted='NO')

for d in df.index:
    if df['Accounted'][d] == 'NO':
        print('Which Dictionary would you like to add this expense to?')
        print(df['Name'][d],df['Amount'][d])
        val = input('(1)Entertainment (2)Bills (3)Groceries\n')
        if val == '1':
            cat.Entertainment.append(df['Name'][d])
        elif val == '2':
            cat.Bills.append(df['Name'][d])
        elif val == '3':
            cat.Groceries.append(df['Name'][d])
        else:
            print("Incorrect error received, be better")
        df.at[d,'Accounted'] = 'YES'

    else:
        print("YES")

print(df.to_string())
