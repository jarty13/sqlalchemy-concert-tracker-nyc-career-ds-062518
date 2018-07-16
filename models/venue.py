from base import *

class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    capacity = Column(Integer)
    shows = relationship('Show', back_populates= "venue")
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship ('City', back_populates = 'venues')
