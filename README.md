# guess-the-color
 Simple flask app, that trying to guess the color

## How does it work?
- Run `python3.9 run.py`
- Send `POST` request to `http://localhost:5000/` with json data:
  > {"num": `num`}
- In json response, you'll see the `result` key containing the chosen color
  > {"result": "Blue", "success": True}
