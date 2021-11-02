import os

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{pw}@{url}/{db}".format(
    user="admin",
    pw="wasdas5257",
    url="database-2.cten155hsop6.ap-northeast-2.rds.amazonaws.com",
    db="mydatabase",
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"
