import pytest
from unittest.mock import MagicMock
from dao.genre import GenreDAO
from service.genre import GenreService



@pytest.fixture
def genres_dao():
    dao = GenreDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genres_dao):
        self.genres_service = GenreService(dao=genres_dao)

    parametrize = (
        (
            1,
            {
                'id': 1,
                'title': 'NoName'
            }
        ),
        (
            2,
            {
                'id': 2,
                'title': 'TestName'
            }
        )
    )

    @pytest.mark.parametrize('gid, genre', parametrize)
    def test_get_one(self, gid, genre):
        self.genres_service.dao.get_one.return_value = genre

        assert self.genres_service.get_one(gid) == genre, "Bad"

    parametrize = (
        (
            [
                {
                    'id': 1,
                    'title': 'NoName'
                },
                {
                    'id': 2,
                    'title': 'TestName'
                }
            ]
        ),
    )

    @pytest.mark.parametrize('genres', parametrize)
    def test_get_all(self, genres):
        self.genres_service.dao.get_all.return_value = genres

        assert self.genres_service.get_all() == genres, "Bad"

    parametrize = (
        (
            {
                'id': 1,
                'title': 'NoName'
            }
        ),
        (

            {
                'id': 2,
                'title': 'TestName'
            }
        )
    )

    @pytest.mark.parametrize('genre', parametrize)
    def test_create(self, genre):
        self.genres_service.dao.create.return_value = genre

        assert self.genres_service.create(genre) == genre, "Bad"

    parametrize = (
        (
            {
                'id': 1,
                'title': 'NoName'
            }
            ,
            {
                'id': 1,
                'title': 'TestName'
            }
        )
    )

    @pytest.mark.parametrize('genre_original , genre_new', parametrize)
    def test_update(self, genre_original, genre_new):
        self.genres_service.dao.update.return_value = genre_new
        assert self.genres_service.update(genre_new)

    def test_delete(self):
        self.genres_service.delete(1)
        self.genres_service.dao.delete.assert_called_once_with(1)
