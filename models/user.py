from base import *
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__= 'users'
    id = Column(Integer, primary_key= True)
    name = Column(Text)
    shows= relationship('Show', secondary='usershows',back_populates ='users')

    def total_shows(self):
        return len(self.shows)


    def first_show(self):
        self.shows.sort(key=lambda show: show.date)
        first = self.shows[0]
        format_first = f"{first.band.name} - {first.date.strftime('%m/%d/%Y')} - {first.venue.name}, {first.venue.city.name}"
        return format_first
