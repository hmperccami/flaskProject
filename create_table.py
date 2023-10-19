import sqlite3

conn = sqlite3.connect('db001.db')
print('Connected to database successfully')

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS hired_employees (
             id integer PRIMARY KEY,
             name text,
             departament_id integer,
             job_id integer,
             FOREIGN KEY (departament_id) REFERENCES departaments (id),
             FOREIGN KEY (job_id) REFERENCES jobs (id)
             );
    """
)

print('Created table successfully!')

conn.execute('CREATE TABLE IF NOT EXISTS departments ('
             'id integer PRIMARY KEY,'
             'departament text)')
print('Created table successfully!')

conn.execute('CREATE TABLE IF NOT EXISTS jobs ('
             'id integer PRIMARY KEY,'
             'job text)')
print('Created table successfully!')
conn.close()
