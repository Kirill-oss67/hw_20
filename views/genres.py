from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return GenreSchema(many=True).dump(genres), 200

    def post(self):
        req_json = request.json
        ent = genre_service.create(req_json)
        return "", 201, {"location": f"/genres/{ent.id}"}


@genre_ns.route('/<int:bid>')
class GenreView(Resource):
    def get(self, bid):
        genre = genre_service.get_one(bid)
        return GenreSchema().dump(genre), 200

    def put(self, bid):
        req_json = request.json
        req_json["id"] = bid
        genre_service.update(req_json)
        return "", 204

    def patch(self, bid):
        req_json = request.json
        req_json["id"] = bid
        genre_service.partially_update(req_json)
        return "", 204

    def delete(self, bid):
        genre_service.delete(bid)
        return "", 204
