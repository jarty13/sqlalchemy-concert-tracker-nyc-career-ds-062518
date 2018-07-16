from base import *

class Band(Base):
    __tablename__= 'bands'
    id = Column(Integer, primary_key= True)
    name = Column(Text)
    shows = relationship('Show', back_populates= 'band')
