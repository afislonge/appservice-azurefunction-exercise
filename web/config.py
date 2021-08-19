import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="udacitydemoserver.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="udacitydbadmin@udacitydemoserver" #TODO: Update value
    POSTGRES_PW="@l0ng31977"   #TODO: Update value
    POSTGRES_DB="demo"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm' #xkUuhBVCQlo4LsN53Cp+rER6Qtkop/uGE05PGtI9iS4=
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://udacityservicebus2.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=fMV0xyn4ZrUO4E8zUcSvKgRvkz1ndqSSL5fSZ9n4rSo=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'afis.longe@venturegardengroup.com'
    SENDGRID_API_KEY = '' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
