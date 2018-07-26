import sys

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.template import loader

# custom wrappers for app configs/models/fields/connections for extensibility


class AppModel:
    def __init__(self, model):
        self.model = model
        self.fields = []
        self.fields_by_name = {}

        for field in model._meta.fields:
            self.fields.append(model)
            self.fields_by_name[fields.name] = field


class App:
    def __init__(self, app_config):
        self.config = app_config
        self.models = []
        self.models_by_name = {}
        for model in app_config.get_models():
            self.models.append(model)
            self.models_by_name[model.__name__] = model


class AppDatabase:
    
    def __init__(self, name, database_settings, app_data):
        self.name = name
        self.settings = database_settings
        self.app_data = app_data

    def render(self):
        raise NotImplementedError


class MySQLDatabase(AppDatabase):

    def render(self):
        template = loader.get_template('app/database_mysql.rs')
        return (template.render(dict(app_data=self.app_data)))


class PostgreSQLDatabase(AppDatabase):

    def render(self):
        template = loader.get_template('app/database_postgresql.rs')
        return (template.render(dict(app_data=self.app_data)))


class SQLite3Database(AppDatabase):

    def render(self):
        template = loader.get_template('app/database_sqlite3.rs')
        return (template.render(dict(app_data=self.app_data)))





ENGINE_MAP = {
    'django.db.backends.mysql': MySQLDatabase,
    'django.db.backends.postgresql': PostgreSQLDatabase,
    'django.db.backends.sqlite3': SQLite3Database,
}


class AppData:

    def __init__(self):
        self.apps = []
        self.apps_by_name = {}
        for app_config in sorted(apps.get_app_configs(), key=lambda app_config:app_config.name):
            app = App(app_config)
            self.apps.append(app)
            self.apps_by_name[app_config.name] = app

        self.databases = []
        self.databases_by_name = {}
        for database_name, database_settings in settings.DATABASES.items():
            if database_settings['ENGINE'] in ENGINE_MAP:
                app_database = ENGINE_MAP[database_settings['ENGINE']](database_name, database_settings,
                        app_data=self)
            else:
                print('Unknown database engine: {}. Known engines: {}'.format(
                    database_settings['ENGINE'],
                    ENGINE_MAP.keys()),
                    file=sys.stderr
                )
                sys.exit(1)
            self.databases.append(app_database)
            self.databases_by_name[database_name] = app_database


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        #import pudb; pudb.set_trace()
        app_data = AppData()
        for app in app_data.apps:
            print(app.config.verbose_name)
            for model in app.models:
                print('    {}'.format(model.__name__))
                #model._meta.db_table
                #model._meta.db_tablespace
                #model._meta.pk
                #model._meta.verbose_name
                #model._meta.verbose_name_plural
                for field in model._meta.fields:
                    print('        ',field)
                    #field.blank
                    #field,choices
                    #field.cast_db_type(connection)
                    #field.column
                    #field.column
                    #field.db_index
                    #field.db_type(connection)
                    #field.db_parameters(connection)
                    #field.default
                    #field.is_relation
                    #field.many_to_many
                    #field.many_to_one
                    #field.name
                    #field.null
        template = loader.get_template('app/mod.rs')
        print(template.render(dict(app_data=app_data)))

