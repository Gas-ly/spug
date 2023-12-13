DEBUG = False

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'spug',             # 替换为自己的数据库名，请预先创建好编码为utf8mb4的数据库
        'USER': 'root',        # 数据库用户名
        'PASSWORD': 'Txe2SbMjt3',  # 数据库密码
        'HOST': 'mysql-svc',        # 数据库地址
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'STRICT_TRANS_TABLES',
            #'unix_socket': '/opt/mysql/mysql.sock' # 如果是本机数据库,且不是默认安装的Mysql,需要指定Mysql的socket文件路径
        }
    }
}
