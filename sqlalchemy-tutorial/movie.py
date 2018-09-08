from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

# defining a many to many relationship with helper table
movie_actors_association = Table(
    'movies_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    actors = relationship("Actor", secondary=movie_actors_association)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date