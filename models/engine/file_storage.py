#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            qqq = {
                k: v
                for k, v in FileStorage.__objects.items()
                if v.__class__ == cls and k != "_sa_instance_state"
            }
            return qqq
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            temp = {}
            for v in FileStorage.__objects.values():
                if hasattr(v, "_sa_instance_state"):
                    del v._sa_instance_state
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                if key != "_sa_instance_state":
                    temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete based on obj or not"""
        if obj:
            del FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]

    def close(self):
        """Close Method"""
        self.reload()
