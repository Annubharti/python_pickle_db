import meradb
# db = meradb.load("table.db")
# db.set('fiestName', 'Annu')
# db.set('lastName', 'Bharti')
# db.set('age', 21)
# db.set('qualification', 'Intermediate')
# db.set('address','Bangalore')
# db.get_all()
# db.rem('age')
# # db.dump()
# db.exist('firstname')
# db.total_keys()
# db.del_db()
# db.random_insert(8)
# db2 = meradb.load('doosra.db')
# db2.set('key', 'value2')
# db2.get('key')
second = meradb.load("some_other_db.db",True)
second.set(2,"hdh")
second.set("pair_name", "Deepa")
second.demerge("table.db")
second.dump()
