from sqlalchemy import Column, Integer, String, DateTime, ARRAY
import datetime
from .database import Base
"""
    Define the models for different tables in the database
    such as Song, Podcast, and AudioBook.
"""
class Song(Base):
    __tablename__ = "song"
    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(length=100), nullable = False)
    Duration = Column(Integer, nullable = False)
    Uploaded_Time = Column(DateTime, default=datetime.datetime.utcnow)

class Podcast(Base):
    __tablename__ = "podcast"
    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(length=100), nullable = False)
    Duration = Column(Integer, nullable = False)
    Uploaded_Time = Column(DateTime, default=datetime.datetime.utcnow)
    Host = Column(String(length=100), nullable = False)
    Participants = Column(String(length=100))

class AudioBook(Base):
    __tablename__ = "audiobook"
    ID = Column(Integer, primary_key=True, index=True)
    Title = Column(String(length=100), nullable = False)
    Author = Column(String(length=100), nullable = False)
    Narrator = Column(String(length=100), nullable = False)
    Duration = Column(Integer, nullable = False)
    Uploaded_Time = Column(DateTime, default=datetime.datetime.utcnow)