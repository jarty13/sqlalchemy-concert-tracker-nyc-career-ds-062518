from base import *

class City(Base):
    __tablename__= 'cities'
    id = Column(Integer, primary_key = True)
    name = Column(Text) #string
    venues= relationship ('Venue', back_populates='city')
