class Config:
    SECRET_KEY = 'chave_super_secreta'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/agencia_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False