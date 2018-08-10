# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import yaml


def config_reader(Yaml_file):
    with open(Yaml_file) as yf:
        yx = yaml.load(yf)
    return yx


def config_writer(config_data, Yaml_file):
    with open(Yaml_file, 'w') as yf:
        yaml.dump(config_data, yf, default_flow_style=False)


if __name__ == "__main__":
    import json
    a = config_reader('./../temp/Redirect.yml')
    print(a)
    b = json.dumps(a)
    print(b)
