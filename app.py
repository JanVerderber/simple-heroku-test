from flask import Flask
from handlers.public import main as public_main
from utils.environment import is_local

app = Flask(__name__)

# PUBLIC URLS

# HOME PAGE
app.add_url_rule(rule="/", endpoint="public.main.home_page", view_func=public_main.home_page, methods=["GET", "POST"])

# ABOUT ME
app.add_url_rule(rule="/about-me", endpoint="public.main.about_me", view_func=public_main.about_me, methods=["GET"])


# FOR RUNNING

if __name__ == '__main__':
    if is_local():
        app.run(port=8080, host="localhost", debug=True)  # localhost
    else:
        app.run(debug=False)  # production
