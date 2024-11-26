from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" db
db = create_engine("postgresql:///chinook")
# base will essentially grab the metadata produced by our db
# creates subclass to mapeverything back to us
base = declarative_base()

class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)

# instead of connecting to the database directly we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the databse using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all records from the Artist Table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only the "Name" column from the Artist Table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select only "Queen" from the Artist Table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by ArtistId #51 from the Artist Table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with ArtistId #51 on the Album Table
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select only the tracks of the composer "Queen" from the Track table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | ")