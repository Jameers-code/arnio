import arnio as ar
import re

def remove_special_chars(df, columns=None):
    """Remove special characters from string columns."""
    cols = columns or df.select_dtypes("object").columns
    for col in cols:
        df[col] = df[col].str.replace(r"[^a-zA-Z0-9\s]", "", regex=True)
    return df

ar.register_step("remove_special_chars", remove_special_chars)
