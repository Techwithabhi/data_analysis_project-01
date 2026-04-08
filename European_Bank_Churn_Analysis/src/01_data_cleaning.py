def clean_data(df):
    df = df.drop(['Surname'], axis=1)
    df = df.drop_duplicates()
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    return df