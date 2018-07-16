from base import *

class Song(Base):
    __tablename__ ='songs'
    id = Column(Integer, primary_key= True)
    name = Column(Text)
    shows = relationship('Show', secondary = 'showsongs', back_populates ='songs')
