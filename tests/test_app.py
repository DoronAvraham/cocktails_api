from tests.repositories.sqlite_repository import SqliteRepository


def test_data_deserialized_and_stored():
    repository = SqliteRepository()
    result = repository.search_cocktail("mar")

    assert result