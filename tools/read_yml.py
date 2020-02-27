import yaml

def get_yml():
    with open("../data/data.yml","r",encoding="utf-8") as f:
        print(yaml.safe_load(f))


def get_value():
    result = []
    data = get_yml()
    for i in data.values():
        result.append(tuple(i.values()))

    print(result)
if __name__ == '__main__':
    get_value()