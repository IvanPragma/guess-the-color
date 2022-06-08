from __future__ import annotations

import random

from app import app
from flask import request


@app.route('/', methods=['POST'])
def main_route() -> dict:
    """Main and only route, that trying to guess item's color."""

    data = request.json
    if not data:
        return {'success': False, 'detail': 'Request must content json data'}

    item_num = data.get('num')
    if item_num is None:
        return {'success': False, 'detail': 'Request must content attr: "num"'}

    del item_num  # xd

    result = random.choices(['Blue', 'Green', 'Red'], [60, 30, 10])[0]

    return {'success': True, 'result': result}
