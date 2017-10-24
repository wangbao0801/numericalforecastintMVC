"""
Django settings for NFMSbyDjango project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 注意此时BASE_DIR与BASE_TEMPLATE_DIRS路径相同
# E:\01开发\numericalforecastintMVC\NFMSbyDjango
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# E:\01开发\numericalforecastintMVC\NFMSbyDjango
BASE_TEMPLATE_DIRS = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))#获取当前脚本的父目录
print(BASE_DIR)
print(BASE_TEMPLATE_DIRS)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j9%o88ia6c-9pwyomq1y)_a8vkxj^q(e)3@w(c1e@2rpgff@y#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'NFMS',
    'Forecast',
    # 'ForecastTest',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NFMSbyDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'NFMSbyDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    #单位台式机
    #aw
    # 'default': {
    #
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'nfsys',
    #    'USER': 'root',
    #    'PASSWORD': '123456',
    #    'HOST': '',
    #    'PORT': '',
    # }
    # 5510
    # 'default': {
    #
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'nfsysbydj',
    #     'USER': 'root',
    #     'PASSWORD': '123456',
    #     'HOST': '',
    #     'PORT': '',
    # }
    'default': {

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nfsysbydj',
        'USER': 'root',
        'PASSWORD': 'icanflyeva',
        'HOST': '',
        'PORT': '',
    }

}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# os.path.abspath(os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(BASE_DIR,'static')
#E:\01开发\numericalforecastintMVC\NFMSbyDjango\static

# STATICFILES_DIRS = [
#     # "%s/%s" %(BASE_DIR, "static"),
#     os.path.join(BASE_DIR, 'static'),
# ]

# print(STATIC_ROOT)
# print(STATIC_ROOT.replace('\\','/'))


STATICFILES_DIRS = [
    # os.path.join(STATIC_ROOT, "static").replace('\\', '/'),
    ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
    ('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
    ('fonts', os.path.join(STATIC_ROOT, 'fonts').replace('\\', '/')),
    ('img', os.path.join(STATIC_ROOT, 'img').replace('\\', '/')),
    # ('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/')),
    # ('upload', os.path.join(STATIC_ROOT, 'upload').replace('\\', '/')),
]
#
# STATICFILES_DIRS = [
#     # STATIC_ROOT,
#     # STATIC_ROOT.replace('\\','/')
#     os.path.join(BASE_DIR, "static"),
#
#     # ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
#     # ('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
#     # ('fonts', os.path.join(STATIC_ROOT, 'fonts').replace('\\', '/')),
#     # ('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/')),
#     # ('upload', os.path.join(STATIC_ROOT, 'upload').replace('\\', '/')),
# ]
# print(STATICFILES_DIRS)
# print(STATICFILES_DIRS)
TEMPLATE_DIRS = (
    os.path.join(BASE_TEMPLATE_DIRS,  'templates'),
)



# TEMPLATE_DIRS = (
#     os.path.join(BASE_TEMPLATE_DIRS,'AssetsPoolApp'),
# )

# 添加静态文件
# STATICFILES_DIRS=(
#     os.path.join(BASE_DIR,'static')
# )


# 部分自定义的配置节
FTP_URL="128.5.6.21"
# TARGET_DIR="D:\测试"
# TARGET_DIR="E:\\03协同开发\\数值预报显示系统\\numericalforecastintMVC\\NFMSbyDjango\\static\\img\\download"
TARGET_DIR=os.path.join(BASE_DIR,'static','img','download')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
# MEDIA_URL = '/media/'

