from sqlalchemy import create_engine
import pandas as pd
#import pyodbc
import argparse 

#Create the argument parser 
parser = argparse.ArgumentParser(description="Clean data and Optionally upload to SQL")

#Create the argument 
parser.add_argument("--write_sql", action="store_true")
args = parser.parse_args()

data_summary = []

def summary(step, message, result, table_name="", ):
    print(message)
    data_summary.append({"step": step, "message": message, "result": result,"table_name": table_name})

#This function takes in a csv file 
def fileLoader(filepath, df_name="DataFrame"):
    try:
        df = pd.read_csv(filepath)
        output = (f"[{df_name}] Loaded successfully with {len(df)} rows")
        result = len(df)
        print(result)
        summary("filesLoaded", output, result, df_name)
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
        output = (f"Removed {before - after} duplicated rows from {df_name}")
        result = (f"{before - after}")
        summary("Duplicates", output, result, df_name)
        return df
    except Exception as error:
        print(f"Error removing duplicates: {error} from {df_name}")
        return df

def remove_nulls(df, df_name="DataFrame"):
    try:
        before = len(df)
        df = df.dropna()
        after = len(df)
        output = (f"Removed {before - after} nulls from {df_name}")
        result = (f"{before - after}")
        summary("NullsRemoved", output, result, df_name)
        return df
    except Exception as error:
        print(f"Error removing nullls: {error} from {df_name}")
        return df

def fix_dates(df, column, df_name="DataFrame"):
    try:
        df[column] = pd.to_datetime(df[column].str.strip('"'), format='%d/%m/%Y', errors = 'coerce')
        df = df.dropna(subset=[column])
        output = (f"{df_name} fixed {column} to correct format")
        summary("FixDates", output, df_name, df_name)
        return df 
    except Exception as error:
        print(f"{df_name} there was an erorr: {error}")
        return df


class dataEnrichment:
    def enrichData(self, df, col1, col2, new_col, df_name="DataFrame"):
        try:
            df[new_col] = (df[col2] - df[col1]).dt.days
            df = df[df[new_col] >=0]
            output = (f"{df_name}: Added column {new_col}")
            summary("enrichData", output, df_name, df_name)
            return df
        except Exception as error:
            print(f"{df_name} Error calculating no.of days {error}")
            return df 


if __name__ == "__main__":       
    Books = remove_duplicates(Books, "Books")
    Books = remove_nulls(Books, "Books")
    Books = fix_dates(Books, "Book checkout", "Books")
    Books = fix_dates(Books, "Book Returned", "Books")

    enricher = dataEnrichment()
    Books = enricher.enrichData(Books, "Book checkout", "Book Returned", "daysTakenToReturn", "Books")
    Books.to_csv("Data/Cleaned_Books.csv")

    Customers = remove_duplicates(Customers, "Customers")
    Customers = remove_nulls(Customers, "Customers")
    Customers.to_csv("Data/Cleaned_Customers.csv")


    if args.write_sql == True:
        server = 'localhost'
        database = 'LibrarySystem'
        driver = 'ODBC Driver 17 for SQL Server'

        connection_string = f"mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver={driver}"
        engine = create_engine(connection_string)

        books = pd.read_csv('Data/Cleaned_Books.csv')

        customers = pd.read_csv('Data/Cleaned_Customers.csv')

        books.to_sql(
            name='Books',
            if_exists="replace",
            con=engine 
        )

        customers.to_sql(
            name='Customers',
            if_exists="replace",
            con=engine
        )

        summary_df = pd.DataFrame(data_summary)

        summary_df.to_sql(
            name='datasummary',
            if_exists="replace",
            con=engine
        )

        print("Data written to SQL")
    else:
        print("Argument not met: Not writting to SQL")

