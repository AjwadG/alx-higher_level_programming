#!/usr/bin/python3
"""base class module"""
import json
from os.path import exists
import csv
import turtle
import time
from random import random


class Base:
    """base class for all shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructior"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """"dict to json"""
        a = list_dictionaries
        if a is None or type(a) is not list or len(a) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"dict to file"""
        name = cls.__name__
        ls = []
        if list_objs is not None:
            for a in list_objs:
                ls.append(a.to_dictionary())
        with open(name + ".json", "w+", encoding="utf-8") as file:
            file.write(Base.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """"dict to json"""
        a = json_string
        if a is None or type(a) is not str or len(a) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """"crates new obj"""
        name = cls.__name__
        if name == "Rectangle":
            tmp = cls(1, 1)
        elif name == "Square":
            tmp = cls(1)
        else:
            tmp = None
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """"crates new obj from avlues in file"""
        name = cls.__name__ + ".json"
        if not exists(name):
            return []
        with open(name, "r+", encoding="utf-8") as file:
            tmp = cls.from_json_string(file.read())
        ls = []
        for a in tmp:
            ls.append(cls.create(**a))
        return ls

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """"dict to file"""
        name = cls.__name__
        ls = []
        if list_objs is not None:
            if name == "Rectangle":
                for a in list_objs:
                    ls.append([a.id, a.width, a.height, a.x, a.y])
            else:
                for a in list_objs:
                    ls.append([a.id, a.size, a.x, a.y])
        with open(name + ".csv", "w+", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(ls)

    @classmethod
    def load_from_file_csv(cls):
        """"crates new obj from avlues in file"""
        name = cls.__name__
        if not exists(name + ".csv"):
            return []
        with open(name + ".csv", "r+", encoding="utf-8", newline='') as file:
            tmp = csv.reader(file)
            ls = []
            for a in tmp:
                a = [int(i) for i in a]
                if name == "Rectangle":
                    dic = {"id": a[0], "width": a[1], "height": a[2],
                           "x": a[3], "y": a[4]}
                elif name == "Square":
                    dic = {"id": a[0], "size": a[1], "x": a[2], "y": a[3]}
                else:
                    return []
                ls.append(cls.create(**dic))
        return ls

    @staticmethod
    def draw(list_rectangles, list_squares):
        shapes = list_rectangles + list_squares
        for a in shapes:
            draw = turtle.Turtle()
            draw.color(random(), random(), random())
            draw.setpos(-a.x, -a.y)
            draw.pensize(7)
            draw.pendown()
            draw.forward(a.width)
            draw.right(90)
            draw.forward(a.height)
            draw.right(90)
            draw.forward(a.width)
            draw.right(90)
            draw.forward(a.height)
            draw.right(90)
            draw.end_fill()

        time.sleep(10)
