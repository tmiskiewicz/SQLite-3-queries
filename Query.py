import sqlite3
import pandas as pd


conn =sqlite3.connect('chinook.db')
c = conn.cursor()

class Query:  
    
    def value_of_invoice_bigger():
        billing_country = input('Please, enter name of country: ')
        amount_of_invoice = int(input('Please, enter the value of amount: '))
        name_of_excel = input('Please name file: ')
        
        df = pd.read_sql_query(f"""SELECT * FROM invoices 
                               WHERE BillingCountry = '{billing_country}' 
                               AND Total > '{amount_of_invoice}'""", conn)
        
        df.to_excel(f"{name_of_excel}.xlsx",index=False)
      
    def value_of_invoice_smaller():
        billing_country = input('Please, enter name of country: ')
        amount_of_invoice = int(input('Please, enter the value of amount: '))
        name_of_excel = input('Please name file: ')
        
        df = pd.read_sql_query(f"""SELECT * FROM invoices 
                               WHERE BillingCountry = '{billing_country}' 
                               AND Total < '{amount_of_invoice}'""", conn)
        
        df.to_excel(f"{name_of_excel}.xlsx",index=False)
    
    def total_value_by_countries():
        name_of_excel = input('Please name file: ')
        
        df = pd.read_sql_query(f"""SELECT BillingCountry, SUM(Total)
                                FROM invoices
                                GROUP BY BillingCountry""", conn)
                                
        df.to_excel(f"{name_of_excel}.xlsx",index=False)
    
    def total_value_one_country():
        billing_country = input('Please, enter name of country: ')
        name_of_excel = input('Please name file: ')
        
        df = pd.read_sql_query(f"""SELECT SUM(Total) 
                               AS Value_of_invoices_in_{billing_country}
                               FROM invoices
                               WHERE BillingCountry='{billing_country}'""", conn)
        
        df.to_excel(f"{name_of_excel}.xlsx",index=False)


Query.value_of_invoice_bigger()











































