# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
import pandas as pd
import numpy as np
edu= pd.read_csv (r'/Users/helmichaaba/Downloads/6 - Primary Education.xlsx - Primary.csv')
edu.head()
null_cols = edu.isnull().sum()
null_cols[null_cols > 0]
stats = edu.describe().transpose()
stats['IQR'] = stats['75%'] - stats['25%']
stats
edu.dtypes
select_columns = ['ISO3', 'Countries and areas', 'Region', 'Sub-region', 'Income Group', 
                  'Total', 'Residence Rural', 'Residence Urban','Wealth quintile Poorest','Wealth quintile Richest', 
                  'Data source', 'Time period']
before = len(edu) 
edu = edu[select_columns].drop_duplicates()
after = len(edu)
print('Number of duplicate records dropped: ', str(before - after))
edu.loc[edu.isnull().any(axis=1)]
edu1=edu.dropna(subset=['Total','Residence Rural', 'Residence Urban','Wealth quintile Poorest','Wealth quintile Richest'], how='all')
edu2=edu1.drop(['Countries and areas','Sub-region'], axis=1)
edu2
edu2['Time period']=edu2['Time period'].str.replace('-[0-9]*', '', regex=True)
edu2=edu2.fillna(0)
edu2['Residence Urban'] =np.where(edu2['Residence Urban']>1, edu2['Residence Urban']/100 , edu2['Residence Urban'])
edu2['Total']=np.where(edu2['Total']> 1, ((edu2['Residence Rural']+edu2['Residence Urban'])/2) , edu2['Total'])
edu2.reset_index(drop=True, inplace=True)
edu2
edu2.to_csv(r'/Users/helmichaaba/Downloads/edu2.csv')


edu3=edu2.groupby(['Time period','Region','ISO3']).sum()
edu3
edu3= edu3.fillna(0)
edu3
edu3['Residence Urban'] =np.where(edu3['Residence Urban']>1, edu3['Residence Urban']/100 , edu3['Residence Urban'])
edu3['Total']=np.where(edu3['Total']> 1, ((edu3['Residence Rural']+edu3['Residence Urban'])/2) , edu3['Total'])
edu3
edu3.to_csv(r'/Users/helmichaaba/Downloads/edu7.csv')
