from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

#  executing the instructions from our localhost "chinook" db
db = create_engine("postgresql///:chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    
)
#  make connection
with db.connect() as connection: