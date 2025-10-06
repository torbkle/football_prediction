def home_advantage_feature(df):
    """Legg til en enkel feature: 1 hvis hjemmelag, 0 hvis bortelag"""
    df["home_advantage"] = (df["home_team"] == df["team"]).astype(int)
    return df
