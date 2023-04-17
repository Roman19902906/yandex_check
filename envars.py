import os

from dotenv import load_dotenv, find_dotenv
from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists
load_dotenv(find_dotenv())

BASE_URL_YANDEX_PASSPORT = os.getenv('BASE_URL_YANDEX_PASSPORT')
