from sklearn.preprocessing import LabelEncoder
import numpy as np
import streamlit as st
from tab_df.logics import Dataset

class Encoding:
    def __init__(self, data):
        self.data = data

        # Check if data is available
        if self.data is None:
            raise ValueError("No data available. Use set_data() to load data first.")

    def label_encoding(self):
        if self.data is None:
            raise ValueError("No data available. Use set_data() to load data first.")

        # Convert Dataset to DataFrame
        df = self.data        

        df['duration'] = np.log(df['duration']+0.01)
        
        df = df[(df['duration'] < 7.42) & (df['duration'] > 3.045)]
        
        df['age'] = np.log(df['age'])
        
        df = df[(df['age'] > 2.89) & (df['age'] < 4.419)]
        
        df['month'] = df['month'].map({'may':5, 'jun':6, 'jul':7, 'aug':8, 'oct':10, 'nov':11, 'dec':12, 'mar':3, 'apr':4,
               'sep':9}).astype(int)
        
        
        df['education'] = df.education.map({'unknown':0,'illiterate':0,'basic.4y':0,'basic.6y':0, 'basic.9y':1,'high.school':0,
                                             'professional.course':1, 'university.degree':2})
        
        df['job']=df['job'].map({'admin.':1, 'blue-collar':2, 'technician':1,'services':2,'management':3, 'entrepreneur':3,'self-employed':3,'retired':3, 
         'unemployed':3,'housemaid':3,'unknown':3,'student':3})
        
        df['marital']=df['marital'].map({'married':0, 'single':1, 'divorced':1,'unknown':1})
        
        df['default']=df['default'].map({'yes':1, 'no':0, 'unknown':1})
        
        df['housing'] = df['housing'].map({'yes' : 1, 'no': 0,'unknown':0})
        
        df['loan'] = df['loan'].map({'yes' : 1, 'no': 0,'unknown':0})
        
        df['y'] = df['y'].map({'yes' : 1, 'no': 0})
        
        df['contact'] = df['contact'].map({'cellular' : 1, 'telephone': 0})
        
        df['day_of_week'] = df['day_of_week'].map({'thu' : 5, 'mon': 2,'wed':4,'tue':3,'fri':6})
        
        df['poutcome'] = df['poutcome'].map({'nonexistent' : 0, 'failure': 1,'success':1})
        
        # Shift the 'emp.var.rate' column to make it positive
        min_value = df['emp.var.rate'].min()
        shift_constant = abs(min_value) + 0.1  # Add a small constant to ensure positivity
        df['emp.var.rate'] = df['emp.var.rate'] + shift_constant
        
        # Log transformation on the shifted 'emp.var.rate' column
        df['emp.var.rate'] = np.log1p(df['emp.var.rate'])
        
        
        # Shift the 'cons.conf.idx' column to make it positive
        min_value = df['cons.conf.idx'].min()
        shift_constant = abs(min_value) + 0.1  # Add a small constant to ensure positivity
        df['cons.conf.idx'] = df['cons.conf.idx'] + shift_constant
        
        # Log transformation on the shifted 'cons.conf.idx' column
        df['cons.conf.idx'] = np.log1p(df['cons.conf.idx'])
        
        df = df[df['cons.conf.idx'] >= 1.569]
        
        df['cons.price.idx'] = np.log(df['cons.price.idx'])
        
        df['euribor3m'] = np.log(df['euribor3m'])
        
        df['nr.employed'] = np.log(df['nr.employed'])
        
        df['campaign'] = np.log(df['campaign'])
        
        df = df[df['campaign'] <= 2.708]
        
        df=df.drop(['pdays','nr.employed'],axis=1)
        return df
        
    def splitting_x(self):
        # Split features
        return self.data.drop(['y','poutcome','contact','default','previous','emp.var.rate','month',
                               'cons.price.idx','job','age','cons.conf.idx','campaign','duration','marital'], axis=1)

    def splitting_y(self):
        # Split target
        return self.data['y']

    def head_df(self):
        if self.data is not None:
            return self.data.head()
        else:
            return "No data available"
