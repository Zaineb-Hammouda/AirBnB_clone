#!/usr/bin/python3
"""
the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel
    public class attrs:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
