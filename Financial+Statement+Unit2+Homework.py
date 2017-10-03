
# coding: utf-8

# In[3]:

#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]


# In[4]:

import numpy as np


# In[12]:

#Revenue ARRAY
revenue=np.array(revenue)
print(revenue)


# In[27]:

#Expenses ARRAY
expenses=np.array(expenses)
print(expenses)


# In[31]:

#Monthly Profit
monthly_profit=revenue-expenses
print(monthly_profit)


# In[32]:

#Tax to be paid
tax=np.round(np.array(monthly_profit*0.3),2)
print(tax)


# In[35]:

#Profit after tax cut
profit_tax_cut=np.array(monthly_profit-tax)
print(profit_tax_cut)



# In[46]:

#Profit after tax cut / Revenue
profit_tax_cut_revenue=np.array(profit_tax_cut/revenue)
print(np.round(profit_tax_cut_revenue*100,2))


# In[47]:

#Mean of Profit after tax cut
mean_pat=np.mean(profit_tax_cut)
print(mean_pat)

# In[49]:

#Good Months (Monthly profit more than mean profit)
good_months = np.array(profit_tax_cut > mean_pat)
print(good_months)

# In[51]:

#Bad Months (Monthly profit less than mean profit)
bad_months = np.array(profit_tax_cut < mean_pat)
print(bad_months)

# In[61]:

#Best Month
best_month = np.array(profit_tax_cut == np.max(profit_tax_cut))
print(best_month)


# In[62]:

#Worst month
worst_month = np.array(profit_tax_cut == np.min(profit_tax_cut))
print(worst_month)

