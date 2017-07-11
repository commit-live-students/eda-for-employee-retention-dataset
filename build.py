import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import operator
import matplotlib.pyplot as plt

df = pd.read_csv('data/employee_retention_data.csv')

def get_categorical_variables(df):
    return df[['dept','join_date','quit_date']]

def get_numerical_variables(df):
    return df.drop(['dept','join_date','quit_date'], axis=1)

def get_numerical_variables_percentile(df):
    df_temp = get_numerical_variables(df)
    return df_temp.describe().T

def get_categorical_variables_modes(df):
    cat_df = get_categorical_variables(df)
    return cat_df.mode()

def get_missing_values_count(df):
    return pd.DataFrame(pd.isnull(df).sum().rename('NA_count'))

def plot_histogram_with_numerical_values(df):
    num_df = get_numerical_variables(df)
    plt.subplot(221)
    plt.title(num_df.columns[0])
    sns.distplot(num_df.iloc[:,0], color='yellow', fit=norm, kde=False)
    plt.subplot(222)
    plt.title(num_df.columns[1])
    sns.distplot(num_df.iloc[:,1], color='yellow', fit=norm, kde=False)
    plt.subplot(223)
    plt.title(num_df.columns[2])
    sns.distplot(num_df.iloc[:,2], color='yellow', fit=norm, kde=False)
    plt.subplot(224)
    plt.title(num_df.columns[3])
    sns.distplot(num_df.iloc[:,3], color='yellow', fit=norm, kde=False)
