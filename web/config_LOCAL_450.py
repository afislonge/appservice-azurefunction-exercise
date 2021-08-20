import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = True
    POSTGRES_URL = "udacitydemoserver.postgres.database.azure.com"  # TODO: Update value
    POSTGRES_USER = "udacitydbadmin@udacitydemoserver"  # TODO: Update value
    POSTGRES_PW = "@l0ng31977"  # TODO: Update value
    POSTGRES_DB = "techconfdb"  # TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    # xkUuhBVCQlo4LsN53Cp+rER6Qtkop/uGE05PGtI9iS4=
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING = 'Endpoint=sb://udacitybus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=5lYkOMHNuCL8TAnop31fxHlBeGE4LOYSQ3aZrXs4fjo='  # TODO: Update value
    SERVICE_BUS_QUEUE_NAME = 'udacityqueue'
    ADMIN_EMAIL_ADDRESS: 'afis.longe@venturegardengroup.com'
    # Configuration not required, required SendGrid Account
    SENDGRID_API_KEY = ''


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
