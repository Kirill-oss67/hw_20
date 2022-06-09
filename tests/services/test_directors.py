import pytest
from unittest.mock import MagicMock
from dao.director import DirectorDAO
from service.director import DirectorService



@pytest.fixture
def directors_dao():
    dao = DirectorDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, directors_dao):
        self.directors_service = DirectorService(dao=directors_dao)

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

    @pytest.mark.parametrize('did, director', parametrize)
    def test_get_one(self, did, director):
        self.directors_service.dao.get_one.return_value = director

        assert self.directors_service.get_one(did) == director, "Bad"

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

    @pytest.mark.parametrize('directors', parametrize)
    def test_get_all(self, directors):
        self.directors_service.dao.get_all.return_value = directors

        assert self.directors_service.get_all() == directors, "Bad"

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

    @pytest.mark.parametrize('director', parametrize)
    def test_create(self, director):
        self.directors_service.dao.create.return_value = director

        assert self.directors_service.create(director) == director, "Bad"

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

    @pytest.mark.parametrize('director_original , director_new', parametrize)
    def test_update(self, director_original, director_new):
        self.directors_service.dao.update.return_value = director_new
        assert self.directors_service.update(director_new)

    def test_delete(self):
        self.directors_service.delete(1)
        self.directors_service.dao.delete.assert_called_once_with(1)
