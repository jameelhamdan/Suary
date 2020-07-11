from django.conf import settings

DEFAULT_DATABASE = 'default'
MEDIA_DATABASE = 'media'


class Router:
    def get_database_name(self, model):
        db_name = model._meta.db
        if db_name not in [DEFAULT_DATABASE, MEDIA_DATABASE]:
            raise Exception('Database not defined properly')

        return db_name

    def db_for_read(self, model, **hints):
        return self.get_database_name(model)

    def db_for_write(self, model, **hints):
        return self.get_database_name(model)

    def allow_relation(self, obj1, obj2, **hints):
        return self.get_database_name(obj1) == self.get_database_name(obj2)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
