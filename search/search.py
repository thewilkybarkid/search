from flask import Blueprint, Response


def get_search_blueprint() -> Blueprint:
    search = Blueprint('search', __name__)

    @search.route('/search', methods=['GET'])
    def search_endpoint() -> Response:  # pylint: disable=unused-variable
        return Response(
            response='<?xml version="1.0" encoding="UTF-8"?>'
                     '<item-list xmlns="http://libero.pub"/>',
            status=200,
            mimetype='application/xml')

    return search
