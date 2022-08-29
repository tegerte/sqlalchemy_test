# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sqlalchemy
import psycopg2
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = sqlalchemy.create_engine('postgresql://tegerte:start1@localhost:5432/db_test')
Session = sessionmaker(bind=engine)
session=Session()


# meta = MetaData()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


User.addresses = relationship(
    "Address", order_by=Address.id, back_populates="user")


def create_tables(name):
    Base.metadata.create_all(engine)
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def create_user(name: str, fullname: str, nickname: str) -> str:
    inst = User(name=name, fullname=fullname, nickname=nickname)
    session.add(inst)
    return inst.name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_user('ed','eddy egerter','bla')
    create_tables('PyCharm')
    session.commit()
