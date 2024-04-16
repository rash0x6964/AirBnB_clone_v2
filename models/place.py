#!/usr/bin/python3
""" Place Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import environ as env

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey("places.id")),
    Column('amenity_id', String(60), ForeignKey("amenities.id"))
)

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    __reviews = relationship("Review", cascade="all, delete", backref="place")
    __amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        backref="place",
        viewonly=False
    )

    @property
    def reviews(self):
        """ get all refiews with the current place id """
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__reviews
        return [
            v for v in models.storage.all(models.Review).values()
            if v.place_id == self.id
        ]

    @property
    def amenities(self):
        """ get all amenities with the current place id """
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__amenities
        list = [
            v for v in models.storage.all(models.Amenity).values()
            if v.id in self.amenity_ids
        ]
        return (list)

    @amenities.setter
    def amenities(self, obj):
        """ Set amenity_ids """
        if isinstance(obj, self.__class__):
            self.amenity_ids.append(f"Amenity.{obj.id}")
