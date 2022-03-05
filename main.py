from models.person_model import Person
from services.person_service import *

if __name__ == '__main__':

    data, rules = read_user_csv_and_rules()

    # check csv headers
    if check_csv_headers(data, rules):
        # create objects
        instances = [Person(a, data[0], f"person_{i + 1}") for i, a in enumerate(data[1:])]

        # check Validation_rules
        for i in rules["Validation_rules"]:
            params = (instances, rules)
            getattr(Person, i)(*params)





