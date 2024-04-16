#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity class """

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    # place_amenities = relationship(
    #     "Place",
    #     secondary=place_amenity,
    #     backref="amenity",
    # )
