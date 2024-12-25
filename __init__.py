from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from routes import auth, index, profile
from routes.alumni import survey, news, posts
from routes.admin import stats, manage, mod, announce


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect()
    csrf.init_app(app)
    app.config.from_pyfile("config.py")
    app.jinja_env.filters["title"] = lambda x: x.replace("_", " ").title()

    for blueprint in [
        index,
        survey,
        news,
        posts,
        profile,
        stats,
        manage,
        mod,
        announce,
        auth,
    ]:
        app.register_blueprint(blueprint.bp)

    @app.errorhandler(404)
    def not_found(e):
        return render_template("error.jinja", message=str(e))

    # Disable caching
    app.jinja_env.cache = None
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    if app.config["DEBUG"]:
        print(app.config)
        print(app.url_map)
        print(app.url_map._rules)
        print(app.url_map._rules_by_endpoint)

        @app.after_request
        def after_request(response):
            """Ensure responses aren't cached"""
            response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            response.headers["Expires"] = 0
            response.headers["Pragma"] = "no-cache"
            return response

    return app
