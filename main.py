from flask import Flask
from flask_restful import Api

from cocktails_api.api.resources import CocktailResource
from cocktails_api.repositories.postgresql_repository import PostgresqlRepository


app = Flask(__name__)

def main():

    api = Api(app)
    repository = PostgresqlRepository()
    api.add_resource(CocktailResource, '/api', resource_class_kwargs={'repository': repository})

    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
