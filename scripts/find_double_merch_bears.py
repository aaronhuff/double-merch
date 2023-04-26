from okay_bears.okay_bears import Bears
import json


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def write_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    data = load_json('data/bears.json')
    bears = Bears(data)
    double_merch_bears = []
    tokens = []
    for bear in bears:
        if bear.double_merch:
            double_merch_bears.append({
                    'name': bear.name,
                    'url': bear.image_url,
                    'merch_traits': bear.merch_traits,
                })
            tokens.append(bear.token_address)
    write_json(double_merch_bears, 'data/double_merch.json')
    write_json(tokens, 'data/tokens.json')
