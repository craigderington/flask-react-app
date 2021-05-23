# venv/bin/python
from flask import Flask
from datetime import datetime, timedelta
import uuid

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/api", methods=["GET"])
def index():
    """ Route Index """
    return {
        "_id":str(uuid.uuid4())
    }


@app.route("/api/getdate", methods=["GET"])
def apidatetime():
    """ Get the current date/timestamp route """
    timestamp = get_date()
    return {
        "timestamp": str(timestamp)
    }


def get_date():
    """ Return the current date time as a string. """
    return datetime.now().strftime("%c")


if __name__ == "__main__":
    app.run()
