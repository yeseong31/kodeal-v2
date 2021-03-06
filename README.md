# Kodeal

## π [Deploy Web Page](https://kodeal.herokuapp.com/) π

## π οΈ Language & Tools  π οΈ
![Python: Version](https://img.shields.io/badge/Python-3.10.5-3776AB.svg?logo=Python&logoColor=white)
![Django: Version](https://img.shields.io/badge/Django-4.0.6-092E20.svg?logo=Django&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545.svg?logo=MariaDB&logoColor=white)
![OpenAI Codex](https://img.shields.io/badge/OpenAI-000000.svg?logo=OpenAI&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098.svg?logo=Heroku&logoColor=white)
<!--![Travis CI](https://img.shields.io/badge/TravisCI-3EAAAF.svg?logo=travis-ci&logoColor=white)-->

## π§ Setup π§

- κ°μ νκ²½μ μμ±ν ν κ°μ νκ²½μ μ§μν©λλ€.
  ```sh
  mkdir venvs
  cd venvs
  python -m venv kodeal
  cd myn/Scripts
  activate
  ```
<br>

- μνλ μμΉλ‘ μ΄λνμ¬ νλ‘μ νΈλ₯Ό cloneν©λλ€.
  ```sh
  $ git clone https://github.com/yeseong31/Django_Kodeal.git
  $ cd Django_Kodeal
  ```

<br>

- νλ‘μ νΈμ νμν ν¨ν€μ§λ₯Ό μ€μΉν©λλ€.
  ```sh
  (kodeal)$ pip install -r requirements.txt
  ```

  - μ΄λ νλ‘¬ννΈ μ°½μ `(kodeal)` νμλ `python -m venv` λͺλ Ήμ΄λ₯Ό ν΅ν΄ μμ±λ kodealμ΄λΌλ μ΄λ¦μ κ°μ νκ²½μ μ§μν μνλ₯Ό μλ―Έν©λλ€. 
  
<br>

- ν¨ν€μ§ μ€μΉ μ΄ν νλ‘μ νΈμ μ΅μμ λλ ν°λ¦¬μ `.env` νμΌμ μμ±νκ³  λ€μμ λ΄μ©μ μλ ₯ν©λλ€.
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

- λͺ¨λ  μ€μ  μλ£ μ λ€μμ λͺλ Ήμ΄λ‘ λ‘μ»¬ μλ²λ₯Ό μ€νν  μ μμ΅λλ€.
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
  
## βοΈ Basic Layout βοΈ
![image](https://user-images.githubusercontent.com/66625672/161430320-a59ec796-0448-45ce-b3ae-b048ecff6dd6.png)

## β¨ Service Flow Chart β¨ 
![image](https://user-images.githubusercontent.com/66625672/161430423-24ca87f0-f526-4441-a7b7-eb92199d6af8.png)

