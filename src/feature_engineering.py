import pandas as pd

# Enkel feature: hjemmelagsfordel
def add_home_advantage_feature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Legger til en binÃ¦r feature 'home_advantage':
    1 hvis laget spiller hjemme, 0 ellers.
    """
    df["home_advantage"] = (df["home_team"] == df["team"]).astype(int)
    return df


# Rolling form-poeng siste N kamper
def add_rolling_form_feature(df: pd.DataFrame, window: int = 5) -> pd.DataFrame:
    """
    Legger til en feature 'rolling_form' som summerer poeng
    over de siste `window` kampene for hvert lag.
    Forutsetter at df har kolonnene 'team' og 'points'.
    """
    df["rolling_form"] = (
        df.groupby("team")["points"]
          .rolling(window=window, min_periods=1)
          .sum()
          .reset_index(0, drop=True)
    )
    return df
