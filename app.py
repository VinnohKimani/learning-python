#O.R.M -> Object Relational Mappers
#Translating db rows into objects using OOP

import sqlite3

#create connection to our db
con = sqlite3.connect("e-commerce.sqlite3")

#create a cursor that can e used to execute sql statements
cur = con.cursor()

class Customer:
    TABLE_NAME = 'customers'
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def save(self):
        sql = f"""
             INSERT INTO {self.TABLE_NAME}(name, phone)
             VALUES (?, ?)
"""
        cur.execute(sql, (self.name, self.phone))
        con.commit()
        print(f"{self.name} inserted succefully")

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME}(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             phone TEXT NOT NULL UNIQUE
            )
"""
        cur.execute(sql)
        #this persists the changes to our db
        con.commit()
        print("Customers table created")

Customer.create_table()

customer1 = Customer("Kimani", "079876543")
customer1.save()
