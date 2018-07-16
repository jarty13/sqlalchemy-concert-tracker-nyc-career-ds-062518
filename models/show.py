from base import *
class Show(Base):
    __tablename__='shows'
    id = Column(Integer, primary_key = True)
    date= Column(Date)
    band_id= Column (Integer, ForeignKey('bands.id'))
    band = relationship('Band', back_populates= 'shows')
    venue_id = Column(Integer, ForeignKey ('venues.id'))
    venue = relationship('Venue', back_populates ='shows')
    songs = relationship ('Song', secondary= "showsongs", back_populates='shows')
    users = relationship ('User', secondary='usershows', back_populates='shows')
    #songs = relationship ('Song', secondary= "showsongs")
    #users = relationship ('User', secondary='usershows')
