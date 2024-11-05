# [Open-Source App Generator](https://app-generator.dev/)

[Open-Source Tools](https://app-generator.dev/tools/django-generator) for solo-devs, students and companies - Generate [Digital Products](https://app-generator.dev/product/),
Update legacy code by chat, Inject new modules, Software Auto-healing, AI, Deployment automation (any provider), Docker, K8s.

- 👉 `LIVE Demo`: https://app-generator.dev
- 👉 Get [Support](https://app-generator.dev/ticket/create/) via email and `Discord`   

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
- [Developer Tools](https://app-generator.dev/docs/developer-tools.html)
  - [Django App Generator](https://app-generator.dev/tools/django-generator)
  - [CSV Processor](https://app-generator.dev/tools/csv-processor)
  - [DataBase Migrator](https://app-generator.dev/tools/db-migrator)
  - [DataBase Processor](https://app-generator.dev/tools/db-processor)
  - [Dynamic Django](https://app-generator.dev/docs/developer-tools/dynamic-django/index.html) Tool (commercial)
  - [CSV to DB Table](https://app-generator.dev/docs/developer-tools/csv-to-table.html)
  - [CSV to API](https://app-generator.dev/docs/developer-tools/csv-to-api.html)
  - [CSV to DataTable](https://app-generator.dev/docs/developer-tools/csv-to-datatable.html)
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

## Stack

- Python/Django
- React
- Docker
- CI/CD - LIVE Deploy on Digital Ocean

<br />

## Manual Build

> Step #1 - Download the code

```bash
$ git clone https://github.com/app-generator/app-generator.git
$ cd app-generator
```

> Step #2 - Install modules

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

> Step #3 - Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> Step #4 - Create the ENV file

The `.env` can be created from the `env.sample` file, provided in the root of the project

```bash
$ cp env.sample .env
```

> Step #5 - Compile UI (that uses Tailwind)

```bash
$ pnpm i
$ pnpm run build
```

> Step #5 - Execute `collectstatic` for Django statics

```bash
$ python manage.py collectstatic
$ python manage.py migrate
```

> Start the APP

```bash
$ python manage.py createsuperuser # create the admin
$ python manage.py runserver       # start the project
```

At this point, the app runs at `http://127.0.0.1:8000/`.

<br />

## Compile [Documentation](https://app-generator.dev/docs/index.html)

The Documentation being generated by [](https://www.sphinx-doc.org/en/master/), the compilation requires a linux box

```bash
$ cd docs && rm -rf build && make html
# Or via a while loop
$ cd docs ; while true ; do rm -rf build/ ; make html ; sleep 10 ; done
```

The output is saved on `docs/build` and rendered on `/docs/` URI

<br />

## CLI Interface

All CLI tools are listed by `dev_tools` subcommand:

`$ python manage.py dev_tools`

Below sections explains each dev_tool added to the codebase - If somethings is not working in your environment, please contact [support](https://appseed.us/support/).

### Generate Code

> For now, only Django code is supported.

```bash
$ python manage.py tool_generator -i # Print HELP 
$ python manage.py tool_generator -f sources/input-template-volt.json
```

The generated code is saved in `generated_code` DIR. Open the sources using your favorite editor and start the project. The easier way is to use Docker:

<br />

### Generate Project Template

> Using this tool, we can generate a JSON template used later by the generator

```bash
$ python manage.py tool_generator_interactive -i # Print HELP 
$ python manage.py tool_generator_interactive    # Generate JSON File  
...
# (Truncated Output)
$ python manage.py tool_generator_interactive

[?] Project Friendly Name: Some Django project
[?] The Backend Framework:                                                                                                               
 > django
   flask (soon)
   nodejs (soon)

[?] The UI Kit:                                                                                                                          
 > datta
   volt
   soft-dashboard

[?] The Database:                                                                                                                        
 > sqlite
   mysql
   pgsql
...
# (Truncated Output)
...
> File saved = sources\Nt5QWHGI_django_template.json
> HOW to generate code:
    |-- python manage.py tool_generator -f sources/Nt5QWHGI_django_template.json   
```

By running the sugegsted command, we should be able to generate a valid Django Project.

<br />

### Upload to GitHub

> Note: For having SUCCESS on this operation, a `GITHUB_KEY` is required in `.env` - read [more](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

```bash
$ python manage.py tool_github_uploader -i # Print HELP 
$ python manage.py tool_github_uploader -d generated_code/GENERATED_PROJECT -k GITHUB_KEY 
```

Once the operation is finished, the generated project should be saved under the account associated with the `GITHUB_KEY`.

<br />

### Inspect DB (sqlite, MySql, PgSql)

```bash
# SQLite scan 
$ python manage.py tool_db_processor -f media/tools/db_inspect/db_sqlite.json
# OR
# MySql scan
$ python manage.py tool_db_processor -f media/tools/db_inspect/db_mysql.json
...
# (Truncated Output)
> Processing media/tools/db_inspect/db_sqlite.json
    |-- type      : db
    |-- DB driver : SQLITE
    |-- DB name   : media/tools/common/sample.sqlite3
    |-- DB host   : None
    |-- DB port   : None
    |-- DB user   : None
    |-- DB pass   : None

 > Dump data for [api_user_user]
 > Dump data for [api_authentication_activesession]
 > Dump data for [auth_group]
 > Dump data for [api_user_user_groups]
 > Dump data for [django_content_type]
 > Dump data for [auth_permission]
 > Dump data for [api_user_user_user_permissions]
 > Dump data for [auth_group_permissions]
 > Dump data for [django_admin_log]
 > Dump data for [django_migrations]
 > Dump data for [django_session]
```

The SQL dump is done in the `tmp` DIRECTORY

```bash
ROOT
  |-- tmp
      |-- 05_27_58_SQLITE.sql
      |-- 05_28_04_SQLITE_api_user_user 
```

<br />

### Migrate DB

> Note: the feature works with SQLite, MySql and PostgreSQL.

The source and target DB credentials should be provided in JSON format. Here are the provided samples

- [SQLite Sample](https://github.com/app-generator/app-generator/blob/main/media/tools/db_migrator/db_source_sqlite.json)
- [MySql Sample](https://github.com/app-generator/app-generator/blob/main/media/tools/db_migrator/db_dest.json)

> How to use it:

```bash
$ python manage.py tool_db_migrator -s DB_SOURCE.json -t DB_TARGET.json           # Perform Checks
$ python manage.py tool_db_migrator -s DB_SOURCE.json -t DB_TARGET.json --migrate # Migrate the data 
```

<br />

### CSV processor

Authenticated users can process CSV files and apply transformers.

> DEMO: https://app-generator.dev/tools/csv-processor/

<br />

### Inspect CSV Files

```bash
$ python manage.py tool_inspect_source -f media/tools/csv/csv_inspect.json    # Truncated output
$ python manage.py tool_inspect_source -f media/tools/csv/csv_inspect.json -k # Print all rows 
# OR for distant CSV files
$ python manage.py tool_inspect_source -f media/tools/csv/csv_inspect_distant.json
...
# (Truncated Output)
 > Processing media/tools/csv/csv_inspect.json
       |-- file: media/tools/csv/titanic.csv
       |-- type: csv
{'PassengerId': {'type': 'int64'}, 'Survived': {'type': 'int64'}, 'Pclass': {'type': 'int64'}, 'Name': {'type': 'object'}, 'Sex': {'type': 'object'}, 'Age': {'type': 'float64'}, 'SibSp': {'type': 'int64'}, 'Parch': {'type': 'int64'}, 'Ticket': {'type': 'object'}, 'Fare': {'type': 'float64'}, 'Cabin': {'type': 'object'}, 'Embarked': {'type': 'object'}}
[1] - PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
[2] - 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
[3] - 2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
[4] - 3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
[5] - 4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S
[6] - 5,0,3,"Allen, Mr. William Henry",male,35,0,0,373450,8.05,,S
[7] - 6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q
[8] - 7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S
[9] - 8,0,3,"Palsson, Master. Gosta Leonard",male,2,3,1,349909,21.075,,S
[10] - 9,1,3,"Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",female,27,0,2,347742,11.1333,,S
...
```

<br />

### List available commands

```bash
$ python manage.py help 
# (Truncated Output)
Type 'manage.py help <subcommand>' for help on a specific subcommand.
Available subcommands:
...
[cli]
    help_print_apps
    help_print_cfg
    help_print_models
...
```

<br />

### List Registered Apps

```bash
$ python manage.py help_print_apps
# (Truncated Output)
 APP -> Webpack Loader
 APP -> Administration
 APP -> Authentication and Authorization
 ...
```

<br />

### List Registered Models

```bash
$ python manage.py help_print_models
# (Truncated Output)
APP -> Github
APP -> Google
APP -> Django_Quill
APP -> Celery Results
        |--> django_celery_results.models.TaskResult
          |--> id: AutoField
          |--> task_id: CharField
          |--> periodic_task_name: CharField
          |--> task_name: CharField
          |--> task_args: TextField
          |--> task_kwargs: TextField
          |--> status: CharField
          |--> worker: CharField
          |--> content_type: CharField
          |--> content_encoding: CharField
          |--> result: TextField
          |--> date_created: DateTimeField
          |--> date_done: DateTimeField
          |--> traceback: TextField
          |--> meta: TextField
        |--> django_celery_results.models.ChordCounter
          |--> id: AutoField
          |--> group_id: CharField
          |--> sub_tasks: TextField
          |--> count: PositiveIntegerField
        |--> django_celery_results.models.GroupResult
          |--> id: AutoField
          |--> group_id: CharField
          |--> date_created: DateTimeField
          |--> date_done: DateTimeField
          |--> content_type: CharField
          |--> content_encoding: CharField
          |--> result: TextField
```

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

Crafted and actively supported by [AppSeed](https://appseed.us/) - *<support@appseed.us>*
