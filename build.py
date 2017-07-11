import pandas as pd
import seaborn as sns
from scipy.stats import norm

def get_categorical_variables(df):
    columns = ['dept', 'join_date', 'quit_date']
    for col in columns:
        df[col] = df[col].astype('category')
    return columns


def get_numerical_variables(df):
    numerical_variables = list(df.select_dtypes(include=['float64', 'int64']))
    return numerical_variables


def get_numerical_variables_percentile(df):
    return df.describe().T


def get_categorical_variables_modes(df):
    return df[get_categorical_variables(df)].mode()


def get_missing_values_count(df):
    return pd.DataFrame(df.isnull().sum())


def plot_histogram_with_numerical_values(df):
    plt.figure(figsize = (15,6))
    plt.subplot(221)
    sns.distplot(df[numerical_variables[0]], bins=10, color='yellow', fit=norm, kde=False)
    plt.subplot(222)
    sns.distplot(df[numerical_variables[1]], bins=10, color='yellow', fit=norm, kde=False)
    plt.subplot(223)
    sns.distplot(df[numerical_variables[2]], bins=10, color='yellow', fit=norm, kde=False)
    plt.subplot(224)
    sns.distplot(df[numerical_variables[3]], bins=10, color='yellow', fit=norm, kde=False)
