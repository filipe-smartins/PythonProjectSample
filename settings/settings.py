from os import environ, path

from dotenv import load_dotenv

env_file = path.join(path.dirname(__file__), '.env')
load_dotenv(env_file)


name = environ.get('NAME')
