from models.db import conn, cursor

class  Doctor:
    TABLE_NAME = 'doctors'

    def __init__(self, name, age = 18):
        self.id = None
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"<Doctor {self.id}: {self.name}"

    def save(self):
        sql = f"INSERT INTO {self.TABLE_NAME} (name) VALUES(?) "

        cursor.execute(sql, (self.name,))
        conn.commit()
        #Accessing the id form the database since it is declared as none
        self.id =cursor.lastrowid
     
    def update(self, name):
        if not self.id:
            return "No id"
        
        sql = f"UPDATE {self.TABLE_NAME} SET name = ? WHERE id = ?"
        cursor.execute(sql, (name, self.id))
        conn.commit()


    @classmethod
    def find_one(cls, id):
        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE id = ?"

        row = cursor.execute(sql, (id,)).fetchone()
        
        if row == None:
            return None
        
        #convert table class to instance
        print("DB row: ", row)
        doctor = cls(row[1])
        doctor.id = row[0]

        return doctor
    
    @classmethod
    def find_many_by_ids(cls, *id):
        placeholders = ','.join('?' for _ in id)
        print(placeholders)
        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE id IN ({placeholders})"

        row = cursor.execute(sql, id).fetchall()
        return row

    @classmethod
    def create_many(cls, doctors):
        sql = f"INSERT INTO {cls.TABLE_NAME} (name) VALUES(?) "
        cursor.executemany(sql, doctors)
        conn.commit()


    @classmethod
    def create_table(cls):
        sql = f"""
             CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME}(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL
             )
         """
        cursor.execute(sql)
        conn.commit()
        print("Doctors table created")

Doctor.create_table()