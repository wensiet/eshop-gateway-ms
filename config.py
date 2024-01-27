import yaml

CONFIG_PATH = "config.yaml"


def get_config():
    with open(CONFIG_PATH) as f:
        try:
            config = yaml.safe_load(f)
            return config
        except yaml.YAMLError as exc:
            print(f"Unable to load config: {exc}")
            exit(1)
