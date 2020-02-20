from django.conf import settings

DEFAULT_DATABASE = 'default'
MONGO_DATABASE = 'mongo'
MEDIA_DATABASE = 'media'


class Router:
    def get_database_name(self, model):
        db_name = model._meta.db
        if db_name not in [DEFAULT_DATABASE, MONGO_DATABASE, MEDIA_DATABASE]:
            raise Exception('Database not defined properly')

        return db_name

    def db_for_read(self, model, **hints):
        return self.get_database_name(model)

    def db_for_write(self, model, **hints):
        return self.get_database_name(model)

    def allow_syncdb(self, db, model):
        return db == DEFAULT_DATABASE

    def allow_migrate(self, db, model):
        return db == DEFAULT_DATABASE

