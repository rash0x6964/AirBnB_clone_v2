#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ as env
import models.base_model
import models


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    __cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """get all cities with the current state id
            from filestorage
        """
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__cities
        return [
            v for v in models.storage.all(models.city.City).values()
            if v.state_id == self.id
        ]
