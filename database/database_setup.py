import os
import sys

# These will come in handy when we are writing our mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# These code we will use in the configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# in order to create our foreign key relationships
# this, too, will be used when we write up our mapper
from sqlalchemy.orm import relationship

# these code we will use in our configuration code at the end of the file
from sqlalchemy import create_engine

# this code will help us get set up when we begin to wirte our class code
Base = declarative_base()


class Restaurant(Base):
    # Table Name
    __tablename__ = "restaurant"

    # Column Name
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class MenuItem(Base):
    # Table Name
    __tablename__ = 'menu_item'

    # Column Name
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    course = Column(String(250))
    price = Column(String(80))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

    restaurant = relationship(Restaurant)


###### insert at end of file ######
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
