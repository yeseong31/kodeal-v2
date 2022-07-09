# Kodeal

## 🌐 [Deploy Web Page](https://kodeal.herokuapp.com/) 🌐

## 🛠️ Language & Tools  🛠️
![Python: Version](https://img.shields.io/badge/Python-3.10.5-3776AB.svg?logo=Python&logoColor=white)
![Django: Version](https://img.shields.io/badge/Django-4.0.6-092E20.svg?logo=Django&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545.svg?logo=MariaDB&logoColor=white)
![OpenAI Codex](https://img.shields.io/badge/OpenAI-000000.svg?logo=OpenAI&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098.svg?logo=Heroku&logoColor=white)
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

- 패키지 설치 이후 프로젝트의 최상위 디렉터리에 `.env` 파일을 생성하고 다음의 내용을 입력합니다.
  ```
  SECRET_KEY=
  CLEARDB_DATABASE_URL=
  DB_HOST=
  DB_NAME=
  DB_PASSWORD=
  DB_USER=
  EMAIL_HOST_PASSWORD=
  EMAIL_HOST_USER=
  REDIRECT_PAGE=
  JWT_SECRET_KEY=
  OPENAI_CODEX_KEY=
  CLIENT_ID=
  CLIENT_SECRET=
  LOCAL_DB_NAME=
  LOCAL_DB_USER=
  LOCAL_DB_PASSWORD=
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
  
## ✏️ Basic Layout ✏️
![image](https://user-images.githubusercontent.com/66625672/161430320-a59ec796-0448-45ce-b3ae-b048ecff6dd6.png)

## ✨ Service Flow Chart ✨ 
![image](https://user-images.githubusercontent.com/66625672/161430423-24ca87f0-f526-4441-a7b7-eb92199d6af8.png)

