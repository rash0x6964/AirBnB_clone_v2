#!/usr/bin/python3
""" Place Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import environ as env

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

    @property
    def reviews(self):
        """get all refiews with the current place id
            from filestorage
        """
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__reviews
        return [
            v for v in models.storage.all(models.Review).values()
            if v.place_id == self.id
        ]
