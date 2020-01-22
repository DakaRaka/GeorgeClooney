import json

def load_data():
    """
    Load data from the hard disk, return it
    """
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)

    except FileNotFoundError:
        with open ('data.json', 'w+') as f:
            data = {}
            json.dump(data, f)
    finally:
        return data

def save_data(data):
    """
    Save data to the hard disk

    """

    with open('./data.json', 'w') as f:
        json.dump(data, f)
