import yaml


def load_config(
        config_path: str = '../config.yaml'
):
    with open(config_path, 'r') as f:
        return yaml.load(f, Loader=yaml.SafeLoader)