from abc import ABC, abstractmethod

class CocktailsRepository(ABC):
    @abstractmethod
    def search_cocktail(self, query_string):
        pass
