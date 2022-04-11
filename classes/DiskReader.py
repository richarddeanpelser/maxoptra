from csv import DictReader
import json

class DiskReader:

    def import_csv(csv_file_path):
        csv_data = []
        with open(csv_file_path) as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                csv_data.append(row)
        return csv_data

    def json_reader(path):
            with open(path) as json_file:
                return json.load(json_file)    