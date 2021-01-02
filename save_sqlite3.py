import sqlite3

# connect DB 
conn = sqlite3.connect('top_cities.db')

# get an instance
c = conn.cursor()

# if cities table exists, it would be deleted
c.execute('DROP TABLE IF EXISTS cities')

# create DB table
c.execute("""
    create table cities (
        rank integer,
        city text,
        population integer
    )
""")

# insert data with tuple
c.execute('insert into cities values (?, ?, ?)', (1, '上海', 24150000))

# in this case insert them with tuple
# c.executemany('insert into cities values (?, ?, ?)', [
#     (1, '上海', 24150000),
#     (3, '北京', 21516000),
# ])

# insert data with dict
c.execute('insert into cities values (:rank, :city, :population)', {'rank':2, 'city':'カラチ', 'population': 235000000})

# insert many data with dict in row
c.executemany('insert into cities values (:rank, :city, :population)', [
    {'rank':3, 'city':'北京', 'population':21516000},
    {'rank':4, 'city':'天津', 'population':14722100},
    {'rank':5, 'city':'イスタンブル', 'population':14160467},
])

# commit data
conn.commit()

# select table and columns
c.execute('select * from cities')

# output columns
for row in c.fetchall():
    print(row)

# close the connection
conn.close()
