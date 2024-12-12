# №1
import pandas as pd
df = pd.read_csv('./NISPUF17.csv', sep=',')
def proportion_of_education(dataframe):
  len_of_df = len(df)
  less_than_12 = round(float(df['EDUC1'].where (df['EDUC1'] = 1).count() / len_of_df), 2)
  e12 = round(float(df['EDUC1'].where (df['EDUC1'] = 2).count() / len_of_df), 2)
  more_that_12 = round(float(df['EDUC1'].where (df['EDUC1'] = 3).count() / len_of_df), 2)
  college = round(float(df['EDUC1'].where (df['EDUC1'] = 4).count() / len_of_df), 2)

  pror = {"less than high school":less_than_12,
  "high school":e12,
  "more than high school but not college":more_than_12,
  "college":college}
  print(pror)
proportion_of_education(df)

# №2
import pandas as pd
file = '../files/NISPUF17.csv'
df = pd.read_csv(file, sep=',')
ba = df.groupby('cbf_01')['P_NUMFLU'].mean()
ba_tuple = (round(float(ba[1]), 1), (round(float(ba[2]), 1))
print(ba_tuple)

# №3
import pandas as pd
def chickenpox_by_sex():
    df = pd.read_csv('random/NISPUF17.csv')

    got_vac=df[df['P_NUMVRC']>0] 
    ms=got_vac[got_vac['SEX']==1]
    mnocpox=len(ms[ms['HAD_CPOX']==2])
    menratio=len(ms[ms['HAD_CPOX']==1])/mnocpox
  
    ws=got_vac[got_vac['SEX']==2]
    wnocpox=len(ws[ws['HAD_CPOX']==2])  
    wratio=len(ws[ws['HAD_CPOX']==1])/wnocpox
    sootn={'male':menratio,'female':wratio}
    return sootn
print(chickenpox_by_sex())
