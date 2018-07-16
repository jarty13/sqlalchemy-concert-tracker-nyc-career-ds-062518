from base import *

class ShowSong(Base):
    __tablename__= 'showsongs'
    id= Column (Integer, primary_key = True)
    length = Column(Integer)
    notes = Column(TEXT)
    show_id= Column(Integer, ForeignKey('shows.id'))
    song_id=Column(Integer, ForeignKey('songs.id'))
    #show= relationship(Show, back_populates = 'songs')
    #song = relationship(Song, back_populates = 'shows')
    #show = relationship(Show, backref=backref("showsongs", cascade="all, delete-orphan"))
    #song = relationship(Song, backref=backref("showsongs", cascade="all, delete-orphan"))
