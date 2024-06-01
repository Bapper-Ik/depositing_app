import sqlite3
import time


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY, account_number text, account_name text, bank_name text, price text, via text, status text, duration text)')
        self.conn.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM records')
        rows = self.cur.fetchall()
        return rows
    
    def insert(self, acc_no, acc_name, bank_name, price, via, dts, status='PENDING'):
        self.cur.execute('INSERT INTO records VALUES (NULL,?,?,?,?,?,?,?)',
                         (acc_no, acc_name, bank_name, price, via, status, dts))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute('DELETE FROM records WHERE id=?', (id,))
        self.conn.commit()

    def update(self, id, acc_no, acc_name, bank_name, price, via):
        self.cur.execute('UPDATE records SET account_number=?,account_name=?,bank_name=?,price=?,via=? WHERE id=?',
                         (acc_no, acc_name, bank_name, price, via, id))
        self.conn.commit()

    def approve(self, id, frm):
        self.cur.execute(f"UPDATE records SET via=?, status='APPROVED' WHERE id=?", (frm, id))
        self.conn.commit()

   

# db = Database('deposit.db')

# db.insert(3173839813,'yakubu','first',30000,'first monie')
# db.insert(1124774000,'ibrahi,','unity',110000,'first monie')
# db.insert(3869629100,'musa','GTB',42000,'first monie')
