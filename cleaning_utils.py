import pandas as pd

def split_rows(df, delim = "|"):
    cols = list(df.columns)
    newdf = {k: [] for k in cols}

    for index, row in df.iterrows():  
        for col in cols:
            if col=="Object Number":
                continue
            cell = str(row[col])
            parts = cell.split(delim)

            newdf[col].extend(parts)
        o_num = row['Object Number']
        o_nums = [o_num for i in range(len(parts))]
        newdf['Object Number'].extend(o_nums)


    return pd.DataFrame(newdf)


