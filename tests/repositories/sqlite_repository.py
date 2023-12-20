import sqlite3
from cocktails_api.repositories.cocktails_repository import CocktailsRepository


class SqliteRepository(CocktailsRepository):

    def connection(self):
        return sqlite3.connect('tests/fulldb.db')

    def search_cocktail(self, query_string):
        with self.connection() as connection:

            cursor = connection.cursor()
            query = "SELECT * FROM cocktails WHERE name LIKE ? COLLATE NOCASE"
            cursor.execute(query, ('%' + query_string + '%',))
            return cursor.fetchall()
