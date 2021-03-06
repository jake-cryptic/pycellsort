from os import sep

# Database logins
db_user = 'root'
db_password = None
db_addr = 'localhost'
db_port = 3306

# API keys
OCID_API_KEY = ''

# Download settings
DL_CHUNK_SIZE = 1024*1024 * 20
EXPORTS_DIR = '..{}exports{}'.format(sep, sep)

# Allowed data
ALLOWED_RATS = ['LTE']
ALLOWED_MNCS = {
	'234': ['10', '15', '20', '30', '55', '58']
}
ALLOWED_MCCS = list(ALLOWED_MNCS.keys())