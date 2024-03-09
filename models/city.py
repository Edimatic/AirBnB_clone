#!/usr/bin/python3

"""
    Showing the class of every Cities
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a cities

    Attributes:
        state_id (str): The state id
        name (str): The name of the cities
    """

    state_id = ""
    name = ""
