import re
import math

class Person:
    def __init__(self, row, header, the_id):
        self.__dict__ = dict(zip(header, row))
        self.id = the_id

    @staticmethod
    def check_text_length(instances, rules):
        for i in instances:
            c = 0
            for j in rules["Validation_rules"]['check_text_length']['columns']:
                x = getattr(i, j)
                if len(x) > int(rules["Validation_rules"]['check_text_length']['number'][c]):
                    raise ValueError(f'column:{j} \n id:{i.id} \n Too big string')
                c += 1

    @staticmethod
    def check_number(instances, rules):
        for i in instances:
            for j in rules["Validation_rules"]['check_number']:
                x = getattr(i, j)
                if not type(x) == int or type(x) == float:
                    raise ValueError(f'column:{j} \n id:{i.id} \n It is not a number')

    @staticmethod
    def check_blank(instances, rules):
        for i in instances:
            for j in rules["Validation_rules"]['check_blank']:
                x = getattr(i, j)
                y = 0
                try:
                    if math.isnan(float(x)) is True:
                        y = 1
                except:
                    pass
                if y == 1:
                    raise ValueError(f'column:{j} \n id:{i.id} \n can not be nan')

    @staticmethod
    def check_email(instances, rules):
        y = 0
        for i in instances:
            for j in rules["Validation_rules"]['check_email']:
                x = getattr(i, j)
                regex = re.compile('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
                try:
                    if not re.fullmatch(regex, x):
                        y = 1
                except:
                    pass
                if y == 1:
                    raise ValueError(f'column:{j} \n id:{i.id} \n Invalid email')

    @staticmethod
    def check_uniqueness(instances, rules):
        for j in rules["Validation_rules"]['check_uniqueness']:
            a_list = []
            for i in instances:
                x = getattr(i, j)
                a_list.append(x)
                a_set = set(a_list)
                contains_duplicates = len(a_list) != len(a_set)
                if contains_duplicates:
                    raise ValueError(f'column:{j} \n id:{i.id} \n Duplicate value')