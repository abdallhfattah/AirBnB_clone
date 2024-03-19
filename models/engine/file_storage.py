#!/usr/bin/python3

""" FileStorage to store ower users"""


class FileStorage:
    def __init__(self) -> None:
        # """ to create a unique FileStorage instance for your application """
        pass
        # __file_path
        # __objects

    def all(self):
        """returns the dictionary __objects"""
        print("oaisdjf")
        pass

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        print("oaisdjf")
        pass

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        print("oaisdjf")
        pass

    def reload(self):
        """  
          deserializes the JSON file to __objects
          (only if the JSON file (__file_path) exists ; otherwise, do nothing.
          If the file doesn't exist, no exception should be raised)
          """
        pass
