import databaseRE as db

# add a record to the database
# db.addOne('Lucifer', 'Morningstar', 'casanovafromhell@gmail.com')

# delete a record from the table
# db.deleteOne(9)

# add a list of records to the table
# recordList = [
#     ('Chloe', 'Decker', 'detectivitity@gmail.com'),
#     ('Dan', 'Espinoza', 'douchaniel@yahoo.com')
# ]
# db.addMany(recordList)

# Lookup using WHERE by email
# result = db.lookUpByEmail('mudittiwari2000@gmail.com')
# print(next(result))
# for attr in db.lookUpByEmail('mudittiwari2000@gmail.com'):
#     print(attr)

# show all the records
db.showAll()