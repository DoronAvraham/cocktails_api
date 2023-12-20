import os
import psycopg2
from psycopg2 import sql

from cocktails_api.repositories.cocktails_repository import CocktailsRepository

class PostgresqlRepository(CocktailsRepository):

    __DB_HOST_KEY = "DB_HOST"
    __DB_NAME = "my_cocktails_bar"
    __DB_PASSWORD_KEY = "DB_PASSWORD"
    __DB_USER_KEY = "DB_USER"

    def connection(self, database = __DB_NAME, user = None, password = None, host = None):
        return psycopg2.connect(
                            database = database,
                            user = user or os.environ.get(self.__DB_USER_KEY),
                            password = password or os.environ.get(self.__DB_PASSWORD_KEY),
                            host = host or os.environ.get(self.__DB_HOST_KEY))

    def search_cocktail(self, query_string):

        with self.connection() as connection:
            # Construct the SQL query with a parameterized query to avoid SQL injection
            query = sql.SQL("""
                SELECT cocktails.id,
                    cocktails.name,
                    cocktails.instructions,
                    cocktails.thumbnail,
                    cocktails.image,
                    json_agg(ingredients.ingredient) AS ingredients,
                    json_agg(ingredients.measure) AS measures
                FROM cocktails
                LEFT JOIN ingredients ON cocktails.id = ingredients.cocktail_id
                WHERE cocktails.name ILIKE {}
                GROUP BY cocktails.id
            """).format(sql.Literal(f'{query_string}%'))

            try:
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()

                # Create a list of dictionaries representing each row
                cocktails = []
                for row in result:
                    cocktail_data = {
                        'id': row[0],
                        'name': row[1],
                        'instructions': row[2],
                        'thumbnail_url': row[3],
                        'image_url': row[4],
                        'ingredients': row[5] if row[5] is not None else [],  # Handle NULL values
                        'measures': row[6] if row[6] is not None else []  # Handle NULL values
                    }
                    cocktails.append(cocktail_data)

                return cocktails

            except Exception as e:
                print(f"Error: {e}")
                return None
