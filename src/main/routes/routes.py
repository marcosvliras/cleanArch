from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.user_finder_composer import user_finder_composer

user_route_bp = Blueprint("user_route", __name__)


@user_route_bp.route("/user/find", methods=["GET"])
def find_user():
    try:
        http_response = request_adapter(request, user_finder_composer())
    except Exception as err:
        http_response = handle_errors(err)

    return jsonify(http_response.body), http_response.status_code
