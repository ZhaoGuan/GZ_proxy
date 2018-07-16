# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import yaml


def config_reader(Yaml_file):
    yf = open(Yaml_file)
    yx = yaml.load(yf)
    yf.close()
    return yx


if __name__ == "__main__":
    print(config_reader('./../temp/Filter.yml'))
