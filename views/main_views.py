from flask import Blueprint, request
from flask_json import as_json
from .error_handler import error_handler
from .create_query_string import create_query_string

def main_view_endpoints_constructor(get_connection):

    main_view_endpoints = Blueprint("main_view",__name__)

    @main_view_endpoints.route('/trips_by_week', methods=['GET'])
    @as_json
    @error_handler
    def trips_by_week():

        ##Create Query String
        query_string = create_query_string(request.args)

        with get_connection().cursor() as cur:
            cur.execute(query_string)
            results = cur.fetchall()
            ret = list(map(lambda x: {"week":int(x[0]), "count":x[1]}, results))

        return ret

    return main_view_endpoints