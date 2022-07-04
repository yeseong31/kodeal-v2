# Kodeal

## 🛠️ Language & Tools  🛠️
![Python: Version](https://img.shields.io/badge/Python-3.10.4-3776AB.svg?logo=Python&logoColor=white)
![Django: Version](https://img.shields.io/badge/Django-4.0.4-092E20.svg?logo=Django&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545.svg?logo=MariaDB&logoColor=white)
![OpenAI Codex](https://img.shields.io/badge/OpenAI-Codex-000000.svg?logo=OpenAI&logoColor=white)
<!--![Travis CI](https://img.shields.io/badge/TravisCI-3EAAAF.svg?logo=travis-ci&logoColor=white)-->

## 🔧 Setup 🔧

- 가상 환경을 생성한 후 가상 환경에 진입합니다.
  ```sh
  mkdir venvs
  cd venvs
  python -m venv kodeal
  cd myn/Scripts
  activate
  ```
<br>

- 원하는 위치로 이동하여 프로젝트를 clone합니다.
  ```sh
  $ git clone https://github.com/yeseong31/Django_Kodeal.git
  $ cd Django_Kodeal
  ```

<br>

- 프로젝트에 필요한 패키지를 설치합니다.
  ```sh
  (kodeal)$ pip install -r requirements.txt
  ```

  - 이때 프롬프트 창의 `(kodeal)` 표시는 `python -m venv` 명령어를 통해 생성된 kodeal이라는 이름의 가상 환경에 진입한 상태를 의미합니다. 
  
<br>

- 패키지 설치 이후 프로젝트 내 `config/settings` 위치로 이동하여 `my_settings.py` 파일을 생성합니다.
  ```python
  """my_settings.py"""
  
  # ----- Django settings -----
  DJANGO_SECRET_KEY =         # Django 프로젝트의 SECRET_KEY
  # ----- MariaDB(MySQL) settings -----
  DB_NAME =  		    # 데이터베이스 이름
  DB_USER =   		    # 데이터베이스 User 이름
  DB_PASSWORD = 		    # 데이터베이스 비밀번호
  # ----- Email settings -----
  EMAIL_HOST_USER =  	    # 이메일 주소(인증 링크 발송)
  EMAIL_HOST_PASSWORD = 	    # 이메일 비밀번호(인증 링크 발송) - 별도 설정 필요
  # ----- OpenAI Codex Key -----
  OPENAI_CODEX_KEY =     # OpenAI Codex API Key
  # ----- Naver Papago -----
  CLIENT_ID =                 # Papago API Client ID
  CLIENT_SECRET =        # Papago API Client Secret Key
  # Amazon S3
  AWS_ACCESS_KEY_ID =                # S3Access key ID
  AWS_SECRET_ACCESS_KEY =       # S3 Secret access key
  AWS_S3_BUCKET_LINK =             # S3 버킷 링크
  # ----- JWT Token -----
  JWT_SECRET_KEY =      # JWT 문자열
  # ----- end of settings -----
  
  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = {
      'secret': DJANGO_SECRET_KEY,
      'algorithm': 'HS256',
  }

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': DB_NAME,
          'USER': DB_USER,
          'PASSWORD': DB_PASSWORD,
          'HOST': '127.0.0.1',
          'PORT': '3306',
      }
  }

  # Email Authentication
  EMAIL = {
      'EMAIL_BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
      'EMAIL_USE_TLS': True,
      'EMAIL_PORT': '587',
      'EMAIL_HOST': 'smtp.gmail.com',
      'EMAIL_HOST_USER': EMAIL_HOST_USER,
      'EMAIL_HOST_PASSWORD': EMAIL_HOST_PASSWORD,
      'SERVER_EMAIL': 'KODEAL',
      'REDIRECT_PAGE': 'http://127.0.0.1:8000/'
  }
  
  # Amazon S3
  AWS_REGION = 'ap-northeast-2'
  AWS_STORAGE_BUCKET_NAME = 'kodeal-bucket'         # 버킷 이름
  AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)
  AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400', }
  DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
  ```

<br>

- 모든 설정 완료 시 다음의 명령어로 로컬 서버를 실행할 수 있습니다.
  ```sh
  (kodeal)$ set DJANGO_SETTINGS_MODULE=config.settings.local
  (kodeal)$ python manage.py runserver
  Watching for file changes with StatReloader
  Performing system checks...

  System check identified no issues (0 silenced).
  June 30, 2022 - 14:00:15
  Django version 4.0.5, using settings 'config.settings.local'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
  ```
