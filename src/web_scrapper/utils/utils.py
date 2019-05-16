import configparser, os
import logging.config
import yaml
import json
import itertools

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def setup_logging_with_config(file_name, default_level='DEBUG'):
    path = os.path.join(DIR_PATH, '..', '..', '..', 'conf', file_name)
    env_key = os.getenv('LOG_CFG', None)

    if env_key: path = env_key

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def get_scrapper_config():
    config = configparser.ConfigParser()
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(DIR_PATH, '..', 'conf', 'config.ini')
    config.read(path)

    return config

def get_server_config():
    config = configparser.ConfigParser()
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(DIR_PATH, '..', '..', '..', 'conf', 'config.ini')
    config.read(path)

    return config

def get_windows_service_config():
    config = configparser.ConfigParser()
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(DIR_PATH, '..', '..', '..', 'conf', 'windows_service_config.ini')
    config.read(path)

    return config

def get_verb_dict(logger):
    file_name = 'verb_dict.json'
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    verb_dict = os.path.join(DIR_PATH, '..', 'conf', 'verb_dict.json')
    try:
        with open(verb_dict, 'r') as f: return json.load(f)
    except IOError as e:
        logger.error('Failed to read file {}. Exception follows. {}'.format(file_name, e))
        raise Exception('Failed to read file {}. Exception follows. {}'.format(file_name, e))

def reversed_enumerate(sequence, start):
    sequence = sequence[:start]
    return zip(
        reversed(range(len(sequence))),
        reversed(sequence),
    )