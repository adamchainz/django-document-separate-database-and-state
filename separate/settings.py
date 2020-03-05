import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.environ.get("DEBUG", "") == "1"

SECRET_KEY = "ncz8ett3mo5wzm9l7wub6uc^hqir-$2465w6is%m)_&kc=je95"

# Dangerous: disable host header validation
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    "separate.core",
]

ROOT_URLCONF = "separate.urls"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}
