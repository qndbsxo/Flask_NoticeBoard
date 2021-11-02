import os 

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{pw}@{url}/{db}'.format(
	user='root',
	pw="5257",
	url='localhost',
	db='mydatabase'		
)
SQLALCHEMY_TRACK_MODIFICATIONS= False
SECRET_KEY = "dev"