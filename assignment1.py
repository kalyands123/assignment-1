#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer


# In[2]:


file_path = 'kepler_data.xlsx'
kepler_data = pd.read_excel(file_path, skiprows=51)

kepler_data.columns = kepler_data.columns.str.strip()


# In[4]:


print("Initial Column names:", kepler_data.columns)

kepler_data.rename(columns={'Unnamed: 3': 'koi_disposition'}, inplace=True)
print(kepler_data.head())


# In[3]:


print("Initial Column names:", kepler_data.columns)
kepler_data.rename(columns={'Unnamed: 3': 'koi_disposition'}, inplace=True)
print(kepler_data.head())


# In[5]:


numeric_cols = kepler_data.select_dtypes(include=['float64', 'int64']).columns
non_numeric_cols = kepler_data.select_dtypes(exclude=['float64', 'int64']).columns

print(f"Numeric columns: {numeric_cols}")
print(f"Non-numeric columns: {non_numeric_cols}")


# In[6]:


if not numeric_cols.empty:
    numeric_imputer = SimpleImputer(strategy='mean')
    kepler_data[numeric_cols] = numeric_imputer.fit_transform(kepler_data[numeric_cols])
    print("Imputation of numeric columns completed.")

kepler_data[non_numeric_cols] = kepler_data[non_numeric_cols].astype(str)
non_numeric_imputer = SimpleImputer(strategy='most_frequent')
kepler_data[non_numeric_cols] = non_numeric_imputer.fit_transform(kepler_data[non_numeric_cols])


# In[7]:


label_encoder = LabelEncoder()
kepler_data['koi_disposition'] = label_encoder.fit_transform(kepler_data['koi_disposition'])


# In[8]:


non_numeric_cols = non_numeric_cols.drop('koi_disposition')
kepler_data = pd.get_dummies(kepler_data, columns=non_numeric_cols, drop_first=True)


# In[9]:


X = kepler_data.drop(['koi_disposition'], axis=1)
y = kepler_data['koi_disposition']

if len(kepler_data) > 1:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[10]:


clf = RandomForestClassifier()
clf.fit(X_train, y_train)


# In[11]:


y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(report)

