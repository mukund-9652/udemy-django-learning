SECRET_KEY = 'django-insecure-7#6a5z4qo@*0if-qc_yu6vn_+02)6)0ym&84q*t^nwfa2jpqas'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['167.71.236.188']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btredb',
        'USER':'dbadmin',
        'PASSWORD':'abc123!',
        'HOST':'localhost',
    }
}

EMAIL_HOST_USER='sit19cs040@sairamtap.edu.in'
EMAIL_HOST_PASSWORD=''
