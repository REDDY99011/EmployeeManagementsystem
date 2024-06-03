import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age TEXT,
            doj TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            address TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()
        
    # Insert Function
    def insert(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("INSERT INTO employees(name, age, doj, email, gender, contact, address) VALUES (?,?,?,?,?,?,?)",
                         (name, age, doj, email, gender, contact, address))
        self.con.commit()
        
    # Fetch All Data from DB 
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows = self.cur.fetchall()
       # print(rows)
        return rows 
    
     # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("DELETE FROM employees WHERE id=?", (id,))
        self.con.commit()
    

     # Update a Record in DB
    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute("UPDATE employees SET name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? WHERE id=?",
                         (name, age, doj, email, gender, contact, address, id))
        self.con.commit()



# Create an instance of the Database class
o = Database("Employee1.db")

# Insert a new record
#o.remove("3")
#o.insert("Shayam kumar","35","12-20-2020","samkumar@gmail.com","Male","9731824888","Maski")
