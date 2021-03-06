import os
import random
import sentry_sdk
from bottle import route, run , request
from sentry_sdk.integrations.bottle import BottleIntegration  

sentry_sdk.init(
    dsn="https://10b462f1a4844dcc89ea3bb104d10746@o397103.ingest.sentry.io/5251292",
    integrations=[BottleIntegration()]
)

def generate_message():
    return "ТЕСТ"


@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>D2.10 Домашнее задание</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>{}</p>
    </div>
  </body>
</html>
""".format(
        generate_message()
    )
    return html
@route("/fail")  
def index():  
    raise RuntimeError("There is an error!")  
    return  
@route("/success")  
def hello_world():
    return "Hello world!"


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
