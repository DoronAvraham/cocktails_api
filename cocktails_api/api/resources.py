from flask import request
from flask_restful import Resource

class CocktailResource(Resource):

    def __init__(self, repository):
        self.repository = repository

    __API_SEARCH = "search"

    def get(self):
        # Get the query parameter from the request
        query_string = request.args.get(self.__API_SEARCH)
        if query_string:
            # Call your existing method that retrieves data based on the query string
            return self.repository.search_cocktail(query_string)
        else:
            return {"error": "Search query parameter 'search' is required for searching cocktails."},400
