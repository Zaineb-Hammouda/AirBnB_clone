#!/usr/bin/python3
"""
the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel
    public class attr:
        state_id
        name
    """
    state_id = ""
    name = ""
