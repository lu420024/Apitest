import yaml


def read_data():
    f = open("../data/data.yaml", encoding="utf8")
    data = yaml.safe_load(f)

    return data


get_data = read_data()

print(get_data["heroes_name_list1"])
