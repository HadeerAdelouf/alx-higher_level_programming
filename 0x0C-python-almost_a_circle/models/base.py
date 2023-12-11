#!/usr/bin/python3
""" Module that contains class Base """
import json
import csv
import os.path


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
        file_Name = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(file_Name, 'w') as f:
            f.write(lists)


    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if not json_string:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new
    
    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        LIST_d = cls.from_json_string(list_str)
        list_Ins = []

        for index in range(len(LIST_d)):
            list_Ins.append(cls.create(**LIST_d[index]))

        return list_Ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[x.id, x.width, x.height, x.x, x.y]
                             for x in list_objs]
            else:
                list_objs = [[x.id, x.size, x.x, x.y]
                             for x in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)


    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret_urn = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret_urn.append(cls.create(**d))
        return ret_urn
