# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sqlalchemy
import psycopg2
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from models import User, Address, Base

engine = sqlalchemy.create_engine("postgresql://tegerte:start1@localhost:5432/db_test")


Session = sessionmaker(bind=engine)
session = Session()


# meta = MetaData()


def create_tables(name):
    Base.metadata.create_all(engine)
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


def create_user(name: str, fullname: str, nickname: str) -> str:
    inst = User(name=name, fullname=fullname, nickname=nickname)
    session.add(inst)
    return inst.name


# Press the green button in the gutter to run the script.
def list_users():
    for instance in session.query(User).order_by(User.id):
        print(instance.name, instance.fullname)


def list_users_as_sql():
    for instance in session.query().from_statement(text("Select * from users")):
        print(instance)


if __name__ == "__main__":
    # create a nice user:
    usr = create_user("ed", "eddy egerter", "bla")
    print(f"Created user {usr}.")
    create_tables("PyCharm")
    session.commit()
    list_users()
    list_users_as_sql()
