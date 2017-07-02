import pandas as pd

def get_categorical_variables(df):
    return df[['dept','join_date','quit_date']]


def get_numerical_variables(df):
    df_numeric = pd.DataFrame._get_numeric_data(df)
    return list(df_numeric)


def get_numerical_variables_percentile(df):
    return df.describe().transpose()


def get_categorical_variables_modes(df):
    return df[['dept','join_date','quit_date']].mode()


def get_missing_values_count(df):
    ndf = df.isnull().sum()
    ndf = pd.DataFrame(ndf)
    ndf2 = ndf.reset_index()
    ndf2 = ndf2.rename(columns={'index':'var_name',0:'missing_value_count'})
    return ndf2


def plot_histogram_with_numerical_values(df):
    employee_id = df['employee_id'].tolist()
    company_id = df['company_id'].tolist()
    seniority = df['seniority'].tolist()
    salary = df['salary'].tolist()

    fig, axes = plt.subplots(2, 2)

    axes[0,0].hist(employee_id)
    axes[0,0].set_title('employee_id')

    axes[0,1].hist(company_id)
    axes[0,1].set_title('company_id')

    axes[1,0].hist(seniority)
    axes[1,0].set_title('seniority')

    axes[1,1].hist(salary)
    axes[1,1].set_title('salary')

    plt.tight_layout()
    plt.show()
