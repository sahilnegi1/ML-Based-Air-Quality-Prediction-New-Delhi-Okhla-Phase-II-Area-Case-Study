# -*- coding: utf-8 -*-
"""okhla2AQI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/112sGQ9tHnEU_WRmnM9ki6YFDOj-0-5JK
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from sklearn.metrics import accuracy_score
from sklearn.svm import SVR
import warnings

data=pd.read_csv('/content/AQI_2018_2022.csv',encoding='unicode_escape')

data.head(3)

data.tail()

data.shape

data.info()



data.isnull().sum()

data.describe()

data.nunique()

data.columns



sns.pairplot(data=data)

plt.figure(figsize=(500,10))
plt.xticks(rotation=90)
sns.barplot(x='Date',y='PM2.5',data=data);

plt.figure(figsize=(500,10))
plt.xticks(rotation=90)
sns.barplot(x='Date',y='PM10',data=data);

plt.figure(figsize=(500,10))
plt.xticks(rotation=90)
sns.barplot(x='Date',y='NO2',data=data);

plt.figure(figsize=(500,10))
plt.xticks(rotation=90)
sns.barplot(x='Date',y='CO',data=data);

df.head()

#calculating aqi over NO2
def aqi_no2(no2):
    nqi=0
    if(no2<=40):
        nqi=(50-0)/(40-0)*(no2-0)+0
    elif(no2>40 and no2<=80):
        nqi=(100-51)/(80-41)*(no2-41)+51
    
    elif(no2>80 and no2<=180):
        nqi=(200-101)/(180-81)*(no2-81)+101
    
    elif(no2>180 and no2<=280):
        nqi=(300-201)/(280-181)*(no2-181)+201
    
    elif(no2>280 and no2<=400):
        nqi=(400-301)/(400-281)*(no2-281)+301
    else:
        nqi=(500-401)/(401-281)*(no2-401)+401
       
    return nqi

no2_to_aqi=np.array(data['NO2'])
aqi_for_no2=[]
for i in no2_to_aqi:
  
  ele = float(aqi_no2(i))
  aqi_for_no2.append(ele)

#for i in aqi_for_no2:
print(aqi_for_no2)

aqi_no2(150)

len(aqi_for_no2)

plt.figure(figsize=(500,10))
plt.xticks(rotation=90)
x=data['Date']
y=aqi_for_no2
plt.xlabel('Date')
plt.ylabel('AQI Accd. to NO2')
plt.plot(x,y,'+:b')

#calculating AQi over CO
def aqi_co(co):
    cqi=0
    if(co<=1.0):
        cqi=(50-0)/(1-0)*(co-0)+0
    elif(co>=1.1 and co<=2.0):
        cqi=(100-51)/(2-1.1)*(co-1.1)+51
    
    elif(co>=2.1 and co<=10):
        cqi=(200-101)/(10-2.1)*(co-2.1)+101
    
    elif(co>=10.1 and co<=17):
        cqi=(300-201)/(17-10.1)*(co-10.1)+201
    
    elif(co>=17.1 and co<=34):
        cqi=(400-301)/(34-17.1)*(co-17.1)+301
    else:
        cqi=(500-401)/(35-17.1)*(co-35)+401
    return cqi

co_to_aqi=np.array(data['CO'])
aqi_for_co=[]
for i in co_to_aqi:
    ele = float(aqi_co(i))
    aqi_for_co.append(ele)

#for i in aqi_for_co:
print(aqi_for_co)

aqi_co(110)

len(aqi_for_co)

df.head()

plt.figure(figsize=(500,10))
plt.xticks(rotation=90)
x=data['Date']
y=aqi_for_co
plt.xlabel('Date')
plt.ylabel('AQI Accd. to Carbon Monoxide')
plt.plot(x,y,'o:g')

def aqi_pm2(pm2):
    pm2qi=0
    if(pm2<=30):
        pm2qi=(50-0)/(30-0)*(pm2-0)+0
    elif(pm2>30 and pm2<=60):
        pm2qi=(100-51)/(60-31)*(pm2-31)+51
    
    elif(pm2>60 and pm2<=90):
        pm2qi=(200-101)/(90-61)*(pm2-61)+101
    
    elif(pm2>90 and pm2<=120):
        pm2qi=(300-201)/(120-91)*(pm2-91)+201
    
    elif(pm2>120 and pm2<=250):
        pm2qi=(400-301)/(250-121)*(pm2-121)+301
    else:
        pm2qi=(500-401)/(251-121)*(pm2-250)+401
    return pm2qi


pm2_to_aqi=np.array(data['PM2.5'])
aqi_for_pm2=[]
for i in pm2_to_aqi:
    ele = float(aqi_pm2(i))
    aqi_for_pm2.append(ele)

#for i in aqi_for_pm2:
print(aqi_for_pm2)

aqi_pm2(431)

plt.figure(figsize=(500,10))
plt.xticks(rotation=90)
x=data['Date']
y=aqi_for_pm2
plt.xlabel('Date')
plt.ylabel('AQI Accd. to PM2.5')
plt.plot(x,y,'*:y')

def aqi_pm10(pm10):
    pm10qi=0
    if(pm10<=50):
        pm10qi=(50-0)/(50-0)*(pm10-0)+0
    elif(pm10>50 and pm10<=100):
        pm10qi=(100-51)/(100-51)*(pm10-51)+51
    
    elif(pm10>100 and pm10<=250):
        pm10qi=(200-101)/(250-101)*(pm10-101)+101
    
    elif(pm10>250 and pm10<=350):
        pm10qi=(300-201)/(350-251)*(pm10-251)+201
    
    elif(pm10>350 and pm10<=430):
        pm10qi=(400-301)/(430-351)*(pm10-351)+301
    else:
        pm10qi=(500-401)/(431-352)*(pm10-431)+401
    return pm10qi

pm10_to_aqi=np.array(data['PM10'])
aqi_for_pm10=[]
for i in pm10_to_aqi:
    ele = float(aqi_pm10(i))
    aqi_for_pm10.append(ele)
print(pm10_to_aqi)

aqi_pm10(413)

len(pm10_to_aqi)

plt.figure(figsize=(500,10))
plt.xticks(rotation=90)
x=data['Date']
y=aqi_for_pm10
plt.xlabel('Date')
plt.ylabel('AQI Accd. to PM10')
plt.plot(x,y)

for i in range(0,10):
  print(i)

def cal_aqi(aqi_for_pm2,aqi_for_pm10,aqi_for_no2,aqi_for_co):
  p2=aqi_pm2(aqi_for_pm2)
  p1=aqi_pm10(aqi_for_pm10)
  n=aqi_no2(aqi_for_no2)
  c=aqi_co(aqi_for_co)
  aqi=max(n,c,p2,p1)
  return aqi

carbon=data['CO']
particle2=data['PM2.5']
particle10=data['PM10']
nitrogen=data['NO2']

AQI=[]
for i in range(0,1757):
    ele = (cal_aqi(particle2[i],particle10[i],nitrogen[i],carbon[i]))
    AQI.append(ele)

print(AQI)



cal_aqi(135.96,250.91,93.18,2.82)

data.tail()

df = pd.DataFrame(np.column_stack([aqi_for_no2, aqi_for_co, aqi_for_pm2,aqi_for_pm10,AQI]), 
                               columns=['NO2_AQI', 'CO_AQi', 'PM2.5_AQi','PM10_AQi','AQi'])

df.head()

def AQI_range(x):
  if(x<=50):
    return "GOOD"
  elif(x>50 and x<=100):
    return "SATISFACTORY"
  elif(x>100 and x<=200):
    return "MODERATE"
  elif(x>200 and x<=300):
    return "POOR"
  elif(x>300 and x<=400):
    return "Very Poor"
  elif(x>400):
    return "SEVERE"

aqi_range=[]
for i in range(1757):
    ele = AQI_range(AQI[i])
    aqi_range.append(ele)

print(aqi_range)

AQI_range(312)

data.head()

df = pd.DataFrame(np.column_stack([data['Date'],aqi_for_no2, aqi_for_co, aqi_for_pm2,aqi_for_pm10,AQI,aqi_range]), 
                               columns=['date','NO2_AQI', 'CO_AQi', 'PM2.5_AQi','PM10_AQi','AQi','AQI_Range'])

df.tail()

data = pd.DataFrame(np.column_stack([data['Date'],data['PM2.5'], data['PM10'], data['NO2'],data['CO'],AQI,aqi_range]), 
                               columns=['date','PM2.5', 'PM10', 'NO2','CO','AQi','AQI_Range'])

data.head()

x=data[['PM2.5','PM10','NO2','CO']]
y=data['AQi']

x.head()

y.head()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=70)
#random state

lr=LinearRegression()
lr.fit(x_train,y_train)



x_test.head()

y_test.head()

x_train

y_train.head()



train_pred=lr.predict(x_train)
train_pred

lr.predict([[98.9,224.6,88.04,1.13]])



test_pred=lr.predict(x_test)
test_pred

test_pred

a=pd.DataFrame({'REAL': y_test,'PREDICTED':test_pred.reshape(-1)})
a

plt.xlabel('x_test data')
plt.ylabel('prediction data')
plt.plot(x_test,test_pred,'x')

plt.xlabel('x_test data')
plt.ylabel('y_test data')
plt.plot(x_test,y_test,'x')

test_pred.shape

plt.title('Combined Testing & Prediction Graph')
plt.plot(x_test,y_test,'o',label='Actual Data')
plt.plot(x_test,test_pred,'x',label='Predicted Data')
plt.legend()



lr.score(x_train,y_train)

from sklearn import metrics
rmse_train=(np.sqrt(metrics.mean_squared_error(y_train,train_pred)))
rmse_test=(np.sqrt(metrics.mean_squared_error(y_test,test_pred)))
print("rmse_train=",str(rmse_train))
print("rmse_test=",str(rmse_test))
print("*"*50)
print("RSquared for train=",lr.score(x_train,y_train))
print("RSquared for test=",lr.score(x_test,y_test))

lr.predict([[98.9,224.6,88.04,1.13]])



df.head()



dt=DecisionTreeRegressor()
dt.fit(x_train,y_train)

train_pred=dt.predict(x_train)
train_pred

test_pred=dt.predict(x_test)
test_pred

plt.title('Combined Testing & Prediction Graph')
plt.plot(x_test,y_test,'o',label='Actual Data')
plt.plot(x_test,test_pred,'x',label='Predicted Data')
plt.legend()

dt.score(x_train,y_train)

rmse_train=(np.sqrt(metrics.mean_squared_error(y_train,train_pred)))
rmse_test=(np.sqrt(metrics.mean_squared_error(y_test,test_pred)))
print("rmse_train=",str(rmse_train))
print("rmse_test=",str(rmse_test))
print("*"*50)
print("RSquared for train=",dt.score(x_train,y_train))
print("RSquared for test=",dt.score(x_test,y_test))

#decision tree overfitting

rf=RandomForestRegressor()
rf.fit(x_train,y_train)
train_pred=rf.predict(x_train)
test_pred=rf.predict(x_test)

plt.title('Combined Testing & Prediction Graph')
plt.plot(x_test,y_test,'o',label='Actual Data')
plt.plot(x_test,test_pred,'x',label='Predicted Data')
plt.legend()

rmse_train=(np.sqrt(metrics.mean_squared_error(y_train,train_pred)))
rmse_test=(np.sqrt(metrics.mean_squared_error(y_test,test_pred)))
print("rmse_train=",str(rmse_train))
print("rmse_test=",str(rmse_test))
print("*"*50)
print("RSquared for train=",rf.score(x_train,y_train))
print("RSquared for test=",rf.score(x_test,y_test))

#Support Vector Regressor
svr=SVR()
svr.fit(x_train,y_train)
train_pred=svr.predict(x_train)
test_pred=svr.predict(x_test)

plt.title('Combined Testing & Prediction Graph')
plt.plot(x_test,y_test,'o',label='Actual Data')
plt.plot(x_test,test_pred,'x',label='Predicted Data')
plt.legend()

rmse_train=float(np.sqrt(metrics.mean_squared_error(y_train,train_pred)))
rmse_test=float(np.sqrt(metrics.mean_squared_error(y_test,test_pred)))
print("rmse_train=",str(rmse_train))
print("rmse_test=",str(rmse_test))
print("*"*50)
print("RSquared for train=",svr.score(x_train,y_train))
print("RSquared for test=",svr.score(x_test,y_test))



"""Classification

"""

#KNN
x1=df[['NO2_AQI','CO_AQi','PM2.5_AQi','PM10_AQi']]
y1=df['AQI_Range']

x1_train,x1_test,y1_train,y1_test=train_test_split(x1,y1,test_size=0.3,random_state=70)

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier().fit(x1_train,y1_train)

train_pred=knn.predict(x1_train)
test_pred=knn.predict(x1_test)

acu=accuracy_score(test_pred,y1_test)

acu

print("KAPPA SCORE = ",metrics.cohen_kappa_score(test_pred,y1_test))

knn.predict([[152,0,359,290]])

test_pred.shape

plt.title('Combined Testing & Prediction Graph')
plt.xlabel('AQI')
plt.ylabel('AQI Range')
plt.plot(x1_test,y1_test,'o',label='Actual Data')
plt.plot(x1_test,test_pred,'x',label='Predicted Data')
plt.legend()

#Support Vector Classifier
from sklearn.svm import SVC
clf=SVC(gamma='auto').fit(x1_train,y1_train)

train_pred=clf.predict(x1_train)
test_pred=clf.predict(x1_test)

acu=accuracy_score(test_pred,y1_test)
acu

print("KAPPA SCORE = ",metrics.cohen_kappa_score(test_pred,y1_test))

clf.predict([[152,0,359,290]])

#SVC is Underfitting
#Linear Regression In Regression Is performing Very Well
#and
#KNN in Classification Is Performing Very Well

#final use of model below using linear regression and knn

print("Hello And Welcome to Okhla Phase 2 AQI Predictor Model")
print("*"*54)
a=float(input("Enter The MAX PM2.5 = "))
b=float(input("Enter The MAX PM10 = "))
c=float(input("Enter The MAX NO2 = "))
d=float(input("Enter The MAX CO = "))
print("*"*54)
Aqi=cal_aqi(a,b,c,d)
q=AQI_range(Aqi)
print("Calculated AQI & its Range")
print("AQI = ",Aqi)
print("AQI_Range = ",q)
print("*"*54)
u=rf.predict([[a,b,c,d]])
i=knn.predict([[a,b,c,d]])
print("Predicted AQI & its Range")
print("AQI = ",u)
print("AQI_Range = ",i)
print("*"*54)

3

