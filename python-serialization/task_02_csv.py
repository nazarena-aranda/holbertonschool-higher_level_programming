import csv
import json

def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
            
        with open('data.json', 'w') as f:
            json.dump(data, f)

        return True
    except Exception:
        return False