import pandas as pd

def fileLoader(filepath, df_name="DataFrame"):
    try:
        df = pd.read_csv(filepath)
        print(f"[{df_name}] Loaded successfully with {len(df)} rows")
        return df
    except Exception as error:
        print(f"{df_name} Error loading CSV: {error}")
        return None
    
Books = fileLoader("Data/03_Library Systembook.csv", "Books")
Customers = fileLoader("Data/03_Library SystemCustomers.csv", "Customers")

def remove_duplicates(df, df_name="DataFrame"):
    try:
        before = len(df)
        df= df.drop_duplicates()
        after = len(df)
        print(f"Removed {before - after} duplicated rows from {df_name}")
        return df
    except Exception as error:
        print(f"Error removing duplicates: {error} from {df_name}")
        return df

def remove_nulls(df, df_name="DataFrame"):
    try:
        before = len(df)
        df = df.dropna()
        after = len(df)
        print(f"Removed {before - after} nulls from {df_name}")
        return df
    except Exception as error:
        print(f"Error removing nullls: {error} from {df_name}")
        return df

def fix_dates(df, column, df_name="DataFrame"):
    try:
        df[column] = pd.to_datetime(df[column].str.strip('"'), format='%d/%m/%Y', errors = 'coerce')
        df = df.dropna(subset=[column])
        print(f"{df_name} fixed {column} to correct format")
        return df 
    except Exception as error:
        print(f"{df_name} there was an erorr: {error}")
        return df



Books = remove_duplicates(Books, "Books")
Books = remove_nulls(Books, "Books")
Books = fix_dates(Books, "Book checkout", "Books")
Books = fix_dates(Books, "Book Returned", "Books")
Books.to_csv("Data/Cleaned_Books.csv")

Customers = remove_duplicates(Customers, "Customers")
Customers = remove_nulls(Customers, "Customers")
Customers.to_csv("Data/Cleaned_Customers.csv")
