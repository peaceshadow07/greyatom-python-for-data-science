# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include='object')
numerical_var = bank.select_dtypes(include='number')
print(categorical_var,'\n',numerical_var)
# code starts here






# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'],axis=1)

print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
print(bank_mode)
banks.fillna(bank_mode, inplace=True,)
print(banks)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,values='LoanAmount',index=['Gender','Married','Self_Employed'],aggfunc='mean')

print(avg_loan_amount)

# code ends here



# --------------
# code starts here
loan_approved = banks[banks.Loan_Status=='Y']
loan_approved_se = loan_approved[loan_approved.Self_Employed=='Yes']
loan_approved_nse = loan_approved[loan_approved.Self_Employed=='No']
# print(loan_approved_se)
# print(loan_approved_nse)

percentage_se = (loan_approved_se['Self_Employed'].count()/614)*100
percentage_nse = (loan_approved_nse['Self_Employed'].count()/614)*100
print(percentage_se,'\n',percentage_nse)
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)
big_loan_term = loan_term[loan_term>=25].count()
print(big_loan_term)





# code ends here


# --------------
# code starts here

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])

print(mean_values)

# code ends here


