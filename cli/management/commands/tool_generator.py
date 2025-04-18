import os, json, uuid, shutil, pprint
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.common.models import *
from helpers.generator import * 

def generate_flask( SRC_DIR, INPUTS, JSON_DATA ):

    pprint.pp( INPUTS )

    retCode = flask_custom_user_gen( SRC_DIR, JSON_DATA ) 
    if COMMON.OK != retCode:
        print( 'ERROR: generate CUSTOM USER' )   
        return
    
    # Process Models
    retCode = flask_models_gen( SRC_DIR, JSON_DATA )
    if COMMON.OK != retCode:
        print( 'ERROR: generate MODELS' )   
        return
      
    # Dynamic DT
    if INPUTS['dynamic_dt']:
        dyn_dt_sources(SRC_DIR, JSON_DATA)

    # Process Docker
    if not INPUTS['docker']:
        # remove files
        file_delete( os.path.join( SRC_DIR, 'Dockerfile'         ) )
        file_delete( os.path.join( SRC_DIR, 'docker-compose.yml' ) )
        file_delete( os.path.join( SRC_DIR, 'gunicorn-cfg.py'    ) )
        file_delete( os.path.join( SRC_DIR, '.dockerignore'      ) )
        dir_delete(  os.path.join( SRC_DIR, 'nginx'              ) )

    # Process CI/CD
    if not INPUTS['cicd']:
        # remove files
        file_delete( os.path.join( SRC_DIR, 'build.sh'    ) )
        file_delete( os.path.join( SRC_DIR, 'render.yaml' ) )

    # Process celery
    if not INPUTS['celery']:
        # remove files  
        pass 

    # Process auth_github
    if not INPUTS['auth_github']:
        # remove files
        pass 

    # Enable MySql
    if INPUTS['db_mysql']:
        # add deps & ENV
        deps_add( SRC_DIR, 'flask-mysqldb', '2.0.0')

    # Enable PgSql
    if INPUTS['db_pgsql']:
        # add deps & ENV
        #deps_add( SRC_DIR, 'psycopg2', '2.9.9')
        deps_add( SRC_DIR, 'psycopg2-binary', '2.9.10')

    return COMMON.OK 

class Command(BaseCommand):

    help = 'Generate Code'

    def add_arguments(self, parser):
        
        parser.add_argument('-i', '--info'      , action='store_true', help='Prin Help'            )
        parser.add_argument('-f',                 type=str,            help='JSON Input File'      )
        parser.add_argument('-p', '--print'     , action='store_true', help='Print INPUT infos'    )
        parser.add_argument('-s', '--simulate'  , action='store_true', help='Simulate the process' )

    def handle(self, *args, **kwargs):

        ARG_HELP   = kwargs[ 'info' ]
        ARG_JSON   = kwargs[ 'f'    ]
        ARG_PRINT  = kwargs[ 'print' ]
        ARG_SIMU   = kwargs[ 'simulate' ]

        if ARG_HELP:
            print(f"")
            print(f" > HELP: Generator (CLI version)")
            print(f"    -i (or --info)      : Print this help, and exit")
            print(f"    -f <INPUT.json>     : Specify JSON to use as input")
            print(f"    -p (or --print)     : Print INPUT infos, and exit")
            print(f"    -s (or --simulate)  : Simulate the generation (no output code), and exit")
            print(f"")

            return  

        # print(' > Using input: ' + json_file )                    

        JSON_PATH = os.path.join( INPUT_JSON_VOLT )

        if ARG_JSON:
            JSON_PATH = ARG_JSON    
            
        # load data
        JSON_DATA = json_load( JSON_PATH )

        if not JSON_DATA:
            print( ' > Err loading JSON: ' + JSON_PATH )            
            return

        print( ' > Processing ' + JSON_PATH ) 

        # Copy file
        f_path, f_name = os.path.split( JSON_PATH ) 
        shutil.copyfile( JSON_PATH, os.path.join(DIR_GEN_APPS, f_name) )

        ### Start Processing 

        DIR_ID  = f_name.replace('.json', '_generated') # uuid.uuid4().hex   
        SRC_DIR = os.path.join( DIR_GEN_APPS, DIR_ID )

        input_design       = JSON_DATA['design']
        input_backend      = JSON_DATA['backend']
        input_docker       = True if ( JSON_DATA['deploy']['docker' ] == '1'      ) else False
        input_cicd         = True if ( JSON_DATA['deploy']['ci_cd'  ] == '1'      ) else False
        input_go_live      = True if ( JSON_DATA['deploy']['go_live'] == '1'      ) else False
        input_celery       = True if ( JSON_DATA['tools']['celery'  ] == '1'      ) else False
        input_auth_github  = True if ( JSON_DATA['auth']['github'   ] == '1'      ) else False
        input_db_mysql     = True if ( JSON_DATA['db']['driver'     ] == 'mysql'  ) else False
        input_db_pgsql     = True if ( JSON_DATA['db']['driver'     ] == 'pgsql'  ) else False

        input_api_gen = False 
        if 'api_generator' in JSON_DATA['tools']: 
            input_api_gen = True if ( len( JSON_DATA['tools']['api_generator'] ) > 0 ) else False

        input_dyn_dt = False 
        if 'dynamic_dt' in JSON_DATA['tools']: 
            input_dyn_dt = True if ( len( JSON_DATA['tools']['dynamic_dt'] ) > 0 ) else False

        # bundle input in a DICT    
        INPUTS = {}
        INPUTS[ 'design'      ] = input_design  
        INPUTS[ 'backend'     ] = input_backend  
        INPUTS[ 'docker'      ] = input_docker  
        INPUTS[ 'cicd'        ] = input_cicd  
        INPUTS[ 'go_live'     ] = input_go_live  
        INPUTS[ 'celery'      ] = input_celery  
        INPUTS[ 'auth_github' ] = input_auth_github  
        INPUTS[ 'db_mysql'    ] = input_db_mysql  
        INPUTS[ 'db_pgsql'    ] = input_db_pgsql  
        INPUTS[ 'dynamic_dt'  ] = input_dyn_dt

        if ARG_PRINT:
            print(f"")
            print(f" > Print Generator Input")
            print(f"    design        : " + input_design )
            print(f"    api_generator : " + str(input_api_gen) )
            print(f"")

            return               

        retCode = reset_sources( SRC_DIR, input_backend )
        if COMMON.OK != retCode:
            print( f"ERROR: reset_sources() for {input_backend}" )
            return

        # Check Backend
        if 'flask' == input_backend:
            print( 'Generate Flask Codebase' )   
            return generate_flask( SRC_DIR, INPUTS, JSON_DATA )

        # Inject UI
        # DASHBOARDs
        if 'soft' == input_design :
            product_soft( SRC_DIR )
        elif 'argon' == input_design :
            product_argon( SRC_DIR )
        elif 'material' == input_design:
            product_material( SRC_DIR )        
        elif 'corporate' == input_design:
            product_corporate( SRC_DIR )          
        elif 'black' == input_design:
            product_black( SRC_DIR )          
        elif 'berry' == input_design:
            product_berry( SRC_DIR )          
        elif 'datta' == input_design:
            product_datta( SRC_DIR )          
        elif 'gradient' == input_design:
            product_gradient( SRC_DIR )          
        elif 'volt' == input_design:
            product_volt( SRC_DIR )
        elif 'adminlte' == input_design:
            product_adminlte( SRC_DIR )          
        elif 'tabler' == input_design:
            product_tabler( SRC_DIR )          

        ## KITs
        elif 'soft-kit' == input_design:
            product_soft_kit( SRC_DIR )
        elif 'material-kit' == input_design:
            product_material_kit( SRC_DIR )
        elif 'pixel' == input_design:
            product_pixel( SRC_DIR )

        else:
            print( 'ERROR: Unsupported Design: ' + input_design )
            print( '     |- Expected: soft, material, argon, corporate, black, berry, datta, gradient, volt, adminlte, tabler, soft-kit, material-kit, pixel' )
            return            

        # DB Driver
        if input_db_mysql or input_db_pgsql: 
            retCode = customize_db( SRC_DIR, JSON_DATA ) 
            if COMMON.OK != retCode:
                print( 'ERROR: customize DB' )   
                return 
        
        # Extended User Model
        retCode = custom_user_gen( SRC_DIR, JSON_DATA ) 
        if COMMON.OK != retCode:
            print( 'ERROR: generate CUSTOM USER' )   
            return

        # Add Models
        retCode = models_gen( SRC_DIR, JSON_DATA )
        if COMMON.OK != retCode:
            print( 'ERROR: generate MODELS' )   
            return

        # Added Render Support  
        if input_cicd:
            api_gen_render(SRC_DIR, f_name)

        # Generate Celery, if TRUE == input_celery
        api_gen_celery(SRC_DIR, input_celery)
        
        if input_auth_github:
            deps_add(SRC_DIR, 'django-allauth', '0.58.1')
            urls_add_rule(SRC_DIR, "path('accounts/', include('allauth.urls'))" )
            settings_apps_add(SRC_DIR, 'allauth')
            settings_apps_add(SRC_DIR, 'allauth.account')
            settings_apps_add(SRC_DIR, 'allauth.socialaccount')
            settings_apps_add(SRC_DIR, 'allauth.socialaccount.providers.github')
            settings_middleware_add(SRC_DIR, 'allauth.account.middleware.AccountMiddleware')
            api_gen_outh_github(SRC_DIR)

        # Added API via Generator
        if input_api_gen:
            deps_add(SRC_DIR, 'django-dynamic-api', '1.0.4')
            settings_apps_add(SRC_DIR, 'django_dyn_api')
            settings_apps_add(SRC_DIR, 'rest_framework')
            settings_apps_add(SRC_DIR, 'rest_framework.authtoken')
            api_gen_sources(SRC_DIR, JSON_DATA)
            #api_gen_script(SRC_DIR) # no need
            api_gen_docker(SRC_DIR)
        else:
            print( ' > API GEN: No INPUT' ) 

        #dir_delete( SRC_DIR )
