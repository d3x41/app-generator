# [AppSeed v2](https://app-generator.dev/)

The [New version of AppSeed](https://app-generator.dev/) - Generate Digital Products, Update legacy code by chat, Inject new modules, Software Auto-healing, AI, Deployment automation (any provider), Docker, K8s. 

> 👉 `LIVE Demo`: https://app-generator.dev
 
<br />

## Features

- [One-Click Sign IN](https://app-generator.dev/users/signin/): `GitHub`
- [Marketplace](https://app-generator.dev/product/): mirrored from [AppSeed](https://appseed.us)
- Generator (CLI & Web Versions)
  - MVC: Django, NodeJS, Flask, FastAPI
  - Full-Stack: React, Vue with any API Backend
  - API [ manage visually the data ]
  - eCommerce
  - Website
- Deployment options: Render, AppSeed Cloud Digital Ocean, User Provider (AWS, DO, Azure)
- Developer Tools
  - AI introspection to different data sources
  - CSV processing and data extraction
  - CSV to model
- Sections:
  - [Products](https://app-generator.dev/product/)
  - [Blog](https://app-generator.dev/blog/) 
  - [Docs](https://app-generator.dev/docs/) 
  - [AI Agent](https://app-generator.dev/ai-processor/)
  - `Tools/`
  - `Deploy/`  
  - [Support](https://app-generator.dev/support/)
  - [Custom Development](https://app-generator.dev/custom-development/)
 
<br />

## SPECS

- [SPECS API](https://github.com/app-generator/appseed-v2/blob/main/apps/api/README.md)
- [SPECS Authentication](https://github.com/app-generator/appseed-v2/blob/main/apps/authentication/README.md)
- [SPECS Blog](https://github.com/app-generator/appseed-v2/blob/main/apps/blog/README.md)
- [SPECS Deploy](https://github.com/app-generator/appseed-v2/blob/main/apps/deploy/README.md)
- [SPECS Docs](https://github.com/app-generator/appseed-v2/blob/main/apps/docs/README.md)
- [SPECS Generator](https://github.com/app-generator/appseed-v2/blob/main/apps/generator/README.md)
- [SPECS Pages](https://github.com/app-generator/appseed-v2/blob/main/apps/pages/README.md)
- [SPECS Products](https://github.com/app-generator/appseed-v2/blob/main/apps/products/README.md)
- [SPECS Tasks](https://github.com/app-generator/appseed-v2/blob/main/apps/tasks/README.md)
- [SPECS DevTools](https://github.com/app-generator/appseed-v2/blob/main/apps/tools/README.md)

<br />

For more input please contact [support](https://appseed.us/support/) using the following: 

- Official Email `support@appseed.us`
- Discord: https://discord.gg/fZC6hup (3k+ members).

<br />

## Stack

- Python/Django
- React
- Docker
- CI/CD - LIVE Deploy on Digital Ocean

<br />

## Manual Build 

> Download the code 

```bash
$ git clone https://github.com/app-generator/appseed-v2.git
$ cd appseed-v2
``` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> Start the APP

```bash
$ python manage.py createsuperuser # create the admin
$ python manage.py runserver       # start the project
$ python manage.py runsslserver    # SSL Mode [ https://localhost:8000 ]
```

At this point, the app runs at `http://127.0.0.1:8000/`.  

<br />

## CLI Interface

### Generate Code 

> For now, only Django code is supported. 

```bash
$ python manage.py generator -i # Print HELP 
$ python manage.py generator -f sources/input-template-volt.json
```

The generated code is saved in `generated_code` DIR. Open the sources using your favorite editor and start the project. The easier way is to use Docker: 

```bash
$ cd generated_code/GENERATED_PROJECT/
$ docker-compose up --build
```

Wait for Docker completion and visit `http://localhost:5085` in the browser. 

<br />

### Upload project to GitHub

> Note: For having SUCCESS on this operation, a `GITHUB_KEY` is required - read [more](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens). 

```bash
$ python manage.py github -i # Print HELP 
$ python manage.py github -d generated_code/GENERATED_PROJECT/ -k GITHUB_KEY
```

Once the operation is finished, the generated project should be saved under the account associated with the `GITHUB_KEY`.

<br />

## Compile DOCS

The Documentation being generated by [](https://www.sphinx-doc.org/en/master/), the compilation requires a linux box 

```bash
$ cd docs && rm -rf build && make html
```
The output is saved on 

<br />

## Celery (async tasks)

- Make sure you have a Redis Server running: `redis://localhost:6379`
  - `$ redis-cli` and type `ping` 
- In the base directory inside `tasks_scripts` folder you need to write your scripts file.
- Run the celery command from the CLI.

```bash
$ export DJANGO_SETTINGS_MODULE="core.settings"  
$ celery -A core worker -l info -B
```

> Executed Tasks, [tasks_scripts](https://github.com/app-generator/appseed-v2/tree/main/tasks_scripts) DIR as defined in the [EXEC Schedule](https://github.com/app-generator/appseed-v2/blob/main/core/celery.py) 

- [Critical Tasks](https://github.com/app-generator/appseed-v2/blob/main/tasks_scripts/critical/critical_task.py) - executed every 5min
- [Hourly Tasks](https://github.com/app-generator/appseed-v2/blob/main/tasks_scripts/hourly/hourly_task.py)
- [Daily Tasks](https://github.com/app-generator/appseed-v2/blob/main/tasks_scripts/daily/daily_task.py) 
- [Weekly Tasks](https://github.com/app-generator/appseed-v2/blob/main/tasks_scripts/weekly/weekly_task.py)
- [Monthly Tasks](https://github.com/app-generator/appseed-v2/blob/main/tasks_scripts/monthly/monthly_task.py)

The output for each task can be found in the [LOGS](https://github.com/app-generator/appseed-v2/tree/main/tasks_scripts/logs) Directory. 

Here is a LOG sample generated by a critical task that runs at every 5min: 

- [tasks_scripts/logs/2024-05-20-16-30-critical_task.log](https://github.com/app-generator/appseed-v2/blob/main/tasks_scripts/logs/2024-05-20-16-30-critical_task.log)

<br />

## CLI

Once the VENV is activated, we can use the console to interact with the codebase:

> List available commands

```bash
$ python manage.py help 
(Truncated Output)
Type 'manage.py help <subcommand>' for help on a specific subcommand.
Available subcommands:
...
[cli]
    build_docs
    cmd_apps
    cmd_models
    cmd_showcfg
...
```

> Generate DOCS

```bash
$ python manage.py build_docs
```

> List Registered Apps

```bash
$ python manage.py cmd_apps
(Truncated Output)
 APP -> Webpack Loader
 APP -> Administration
 APP -> Authentication and Authorization
 ...
```

> List Registered Models

```bash
$ python manage.py cmd_models
(Truncated Output)
 APP -> Administration
         |- (model) -> <class 'django.contrib.admin.models.LogEntry'>
 APP -> Authentication and Authorization
         |- (model) -> <class 'django.contrib.auth.models.Permission'>
         |- (model) -> <class 'django.contrib.auth.models.Group'>
         |- (model) -> <class 'django.contrib.auth.models.User'>
```

> print Configuration 

```bash
$ python manage.py cmd_showcfg
(Truncated Output)
 Cfg Key: INSTALLED_APPS -> ['webpack_loader', 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'cli', 'apps.common', 'apps.pages', 'apps.users', 'apps.blog', 'debug_toolbar', 'allauth', 'allauth.account', 'allauth.socialaccount', 'allauth.socialaccount.providers.github', 'allauth.socialaccount.providers.google', 'django_quill']
 Cfg Key: DEBUG -> True
 Cfg Key: USE_TZ -> True
 Cfg Key: ROOT_URLCONF -> core.urls
 Cfg Key: MEDIA_ROOT -> D:\work\appseed-v2\media
 Cfg Key: APPEND_SLASH -> True
 Cfg Key: STATICFILES_FINDERS -> ['django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder']
 Cfg Key: STATICFILES_DIRS -> D:\work\appseed-v2\static
 Cfg Key: STATIC_ROOT -> D:\work\appseed-v2\staticfiles  
```

<br />

## Team

> **Core** 

- [Adrian](https://github.com/Sm0keDev) - Founder, Tech Lead, Automation, Design Patterns
- [Alex Paduraru](https://github.com/alexandru-paduraru) - Business Advisor & Investor
- [Valentin Raduti](https://github.com/deroude) - Full-Stack Senior (Design Patterns, Auth, Automation, React)
- [Teo Deleanu](https://github.com/tdeleanu) - Full-Stack Senior 

> **Developers/Contractors**

- [Mominur](https://github.com/mominur-helios) - Django/React Developer
- [Hasib](https://github.com/hasib-helios) - Django/React Developer
- [Sugeng](https://github.com/sgnd) - CI/CD, Deployment, Docker
- [Nur Askiah](https://github.com/nuraskiah) - Django/React Developer
- [Dhafit](https://github.com/dhafitf) - UI/UX, Frontend
- [Anamul](https://github.com/MySecondLanguage) - Python, Django TL

<br />

## LICENSE

[@EULA](./LICENSE.md)

<br />

---
Crafted and released under the [AppSeed](https://appseed.us/) brand by [Sm0ke](https://x.com/Sm0keDev)
