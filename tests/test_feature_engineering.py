import pandas as pd
from src.feature_engineering import add_home_advantage_feature, add_rolling_form_feature

def test_add_home_advantage_feature():
    df = pd.DataFrame({
        "team": ["A", "B"],
        "home_team": ["A", "C"],
        "points": [3, 0]
    })
    df = add_home_advantage_feature(df)
    assert "home_advantage" in df.columns
    assert df.loc[0, "home_advantage"] == 1
    assert df.loc[1, "home_advantage"] == 0


def test_add_rolling_form_feature():
    df = pd.DataFrame({
        "team": ["A", "A", "A", "B", "B"],
        "points": [3, 1, 0, 3, 3]
    })
    df = add_rolling_form_feature(df, window=2)
    assert "rolling_form" in df.columns
    # Første rad: bare 3 poeng
    assert df.loc[0, "rolling_form"] == 3
    # Andre rad: 3 + 1 = 4
    assert df.loc[1, "rolling_form"] == 4
    # Tredje rad: siste 2 kamper (1 + 0) = 1
    assert df.loc[2, "rolling_form"] == 1
