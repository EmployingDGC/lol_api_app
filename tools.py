import yaml


def get_yaml_configs(file="./config.yaml"):
    with open("learn_yaml.yaml", "r") as yaml_file:
        yaml_content = yaml.load(yaml_file)

    return yaml_content
