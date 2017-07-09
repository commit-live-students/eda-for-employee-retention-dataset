import pandas as pd
df = pd.read_csv('data/employee_retention_data.csv')

def get_categorical_variables(df):
    return df.select_dtypes(include=['object']).columns

def get_numerical_variables(df):
    return df.select_dtypes(exclude=['object']).columns


def get_numerical_variables_percentile(df):
    return df.select_dtypes(exclude=['object']).describe()


def get_categorical_variables_modes(df):
    return df.select_dtypes(include=['object']).mode()


def get_missing_values_count(df):
    return df.isnull()


def plot_histogram_with_numerical_values(df):
    return df.plot.hist(bins=20)
