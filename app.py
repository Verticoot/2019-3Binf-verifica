from flask import Flask
from verticelli import catalog
import json

app = Flask("marconi")

@app.route("/")
def data_book():
    return json.dumps(
        [book.__dict__ for book in catalog]
        )