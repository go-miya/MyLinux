from base.db.mysql_client import Base, db_session, engine
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    __tablename__ = 'City'

    area_id = Column(Integer, autoincrement="auto", nullable=False, primary_key=True)
    area_name = Column(String(50), nullable=False)


class CityPaths(Base):
    __tablename__ = 'CityPaths'

    id = Column(Integer, autoincrement="auto", nullable=False, primary_key=True)
    ancestor = Column(Integer, ForeignKey('City.area_id'), nullable=False)
    descendant = Column(Integer, ForeignKey('City.area_id'), nullable=False)

    def __repr__(self):
        return "<CityPaths(ancestor='%s', descendant='%s')>" % (
            self.ancestor, self.descendant)


# Base.metadata.create_all(engine)


# session = db_session()
# city = City(area_name="上海")
# session.add(city)
# print(city.area_name, city.area_id)
# session.commit()
