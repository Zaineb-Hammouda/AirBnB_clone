#!/usr/bin/python3

"""
The instantiation of our models directory creates a unique FileStorage
instance for the application. This allows the application to store and
retrieve BaseModel instances in a file system
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
