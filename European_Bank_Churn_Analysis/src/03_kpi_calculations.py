def churn_rate(df):
    return df['Exited'].mean() * 100

def churn_by_geo(df):
    return df.groupby('Geography')['Exited'].mean() * 100