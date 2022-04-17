import yaml


def get_yaml_configs(file="./config.yaml"):
    with open(file, "r") as y:
        yc = yaml.load(y, Loader=yaml.Loader)

    return yc
