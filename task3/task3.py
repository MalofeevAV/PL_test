import sys
import json

file1, file2 = sys.argv[1:]
values_insert_json = dict()


def file_reader(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data


def file_writer(file, data):
    with open(file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def from_json_values_to_dict(file_values_json):
    values_json_dict = dict()
    for i in file_values_json["values"]:
        values_json_dict[i["id"]] = i["value"]
    return values_json_dict


def values_insert(test_json, values_dict):
    for element in test_json:
        if "value" in element:
            element["value"] = values_dict[element["id"]]
        if "values" in element:
            values_insert(element["values"], values_dict)
    return test_json


if __name__ == "__main__":
    file_test_json = file_reader(file1)
    file_values_json = file_reader(file2)

    values_json_dict = from_json_values_to_dict(file_values_json)
    values_insert_json["tests"] = values_insert(file_test_json["tests"], values_json_dict)

    file_writer("report.json", values_insert_json)
