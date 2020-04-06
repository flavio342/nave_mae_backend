import json
from flask import request, redirect
from flask_restful import Resource

from core import db

from core.dashboard_views.attendances.query import get_all, get_by_id
from core.dashboard_views.attendances.serializer import serialize, serialize_list
from core.common import admin_token_required
from core.models import Attendance


class Attendances(Resource):

    @admin_token_required
    def get(self, user):
        objs = serialize_list(get_all())
        return objs


class DeleteAttendances(Resource):

    @admin_token_required
    def post(self, user):
        objs = request.get_json()['items']
        for obj in objs:
            user = get_by_id(obj['id'])
            db.session.delete(user)

        db.session.commit()
        return {'success': True}
