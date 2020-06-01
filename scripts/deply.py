from os import system as _
from os import path

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

INSTALL_APPS = [
    '',
    'Trinamic',
    'FieldValue',
    'MyUser',
]


def migrate():
    for app in INSTALL_APPS:
        _(f"python {BASE_DIR}/manage.py makemigrations {app}")

    for app in INSTALL_APPS:
        _(f"python {BASE_DIR}/manage.py migrate {app}")


if __name__ == '__main__':
    migrate()