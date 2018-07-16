from base import *

class UserShow(Base):
    __tablename__='usershows'
    id=Column(Integer, primary_key = True)
    user_id= Column(Integer, ForeignKey ('users.id'))
    show_id = Column(Integer, ForeignKey ('shows.id'))
