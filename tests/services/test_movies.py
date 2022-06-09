import pytest
from unittest.mock import MagicMock
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService



@pytest.fixture
def movies_dao():
    dao = MovieDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movies_dao):
        self.movies_service = MovieService(dao=movies_dao)

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

    @pytest.mark.parametrize('mid, movie', parametrize)
    def test_get_one(self, mid, movie):
        self.movies_service.dao.get_one.return_value = movie

        assert self.movies_service.get_one(mid) == movie, "Bad"

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

    @pytest.mark.parametrize('movies', parametrize)
    def test_get_all(self, movies):
        self.movies_service.dao.get_all.return_value = movies

        assert self.movies_service.get_all() == movies, "Bad"

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

    @pytest.mark.parametrize('movie', parametrize)
    def test_create(self, movie):
        self.movies_service.dao.create.return_value = movie

        assert self.movies_service.create(movie) == movie, "Bad"

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

    @pytest.mark.parametrize('movie_original , movie_new', parametrize)
    def test_update(self, movie_original, movie_new):
        self.movies_service.dao.update.return_value = movie_new
        assert self.movies_service.update(movie_new)

    def test_delete(self):
        self.movies_service.delete(1)
        self.movies_service.dao.delete.assert_called_once_with(1)
