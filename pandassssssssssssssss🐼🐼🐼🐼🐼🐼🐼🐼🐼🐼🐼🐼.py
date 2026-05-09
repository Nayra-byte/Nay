import pandas as pd
import numpy as np
exam_data={'name':['ANA','DIA','IRA','SIA','DANA','SAM','HANNAH','NYSA','AMAIRA','INAARA'],'score':[12.4,23.3,32.3,np.nan,122,12,33,np.nan,12.2,21.2],'attempts':[1,2,3,3,2,1,1,2,2,2],'qualify':['yes','no','yes','no','yes','no','yes','no','yes','no']}
labels=['a','b','c','d','e','f','g','h','i','j']
df=pd.DataFrame(exam_data , index=labels)
print('SUMMARY OF THE BASIC INFORMATION ABOUT THIS DATAFRAME AND ITS DATA: ')
print(df.info())
