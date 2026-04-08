def add_features(df):

    def age_group(age):
        if age < 30: return "Young"
        elif age < 45: return "Mid"
        elif age < 60: return "Senior"
        else: return "Elder"

    df['AgeGroup'] = df['Age'].apply(age_group)

    return df