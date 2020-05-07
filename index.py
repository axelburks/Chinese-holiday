from flask import Flask, Response, request
from chinese_holiday import is_holiday
import datetime
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    date = request.args.get("date") or str(datetime.date.today())
    # refresh = request.args.get("force") or "false"
    # force = True if refresh == "true" else False
    status = "0"
    try:
        # if is_holiday(date, force):
        if is_holiday(date):
            status = "1"
        return Response(
            status, mimetype="text/plain"
        )
    except:
        return Response(
            "Wrong Date Format. Only support fmt as '2020-10-10'", mimetype="text/plain"
        )
    


if __name__ == '__main__':
    app.debug = True
    app.run()
