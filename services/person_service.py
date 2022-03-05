import json
import pandas as pd

def read_user_csv_and_rules():
    # read csv
    data = pd.read_csv('files/csv.csv')
    data = data.T.reset_index().values.T.tolist()

    # read json
    with open('files/validation_rules.json') as json_file:
        rules = json.load(json_file)

    return data, rules

def check_csv_headers(data, validation_rules):
    for j in validation_rules['Headers']:
        if j in data[0]:
            pass
        else:
            raise ValueError('Wrong CSV Headers')
    return True


