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


def rewriter_config(key, value, Yamlfile):
    config = config_reader(Yamlfile)
    if isinstance(config[key], list):
        config[key].append(value)
    else:
        config[key] = value
    config_writer(config, Yamlfile)


def clear_config_key(key, value, Yamlfile):
    config = config_reader(Yamlfile)
    config[key] = value
    config_writer(config, Yamlfile)


if __name__ == "__main__":
    import json

    config_writer({'Request': [], 'Response': []}, './../temp/a.yml')
    a = config_reader('./../temp/a.yml')
    print(a)
    b = json.dumps(a)
    print(b)
