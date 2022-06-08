from __future__ import annotations

from flask import Flask, Response, make_response, jsonify


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error) -> Response:
    """404 error handler."""

    return make_response(jsonify({'success': False, 'error': 'Page not found'}), 404)


# Import views
from app import views
