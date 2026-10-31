"""Flask application for TrainWithUmashankar."""

import os

from flask import Flask, abort, render_template, send_from_directory

from config import SITE_CONTENT
from data.resources import get_resource_by_slug, get_resources


def create_app(test_config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-only-change-this"),
        SITE_CONTENT=SITE_CONTENT,
    )

    if test_config:
        app.config.update(test_config)

    @app.context_processor
    def inject_site_content():
        return {"site": app.config["SITE_CONTENT"]}

    @app.route("/")
    def home():
        resources = get_resources()
        return render_template("index.html", featured_resources=resources[:3])

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/tech")
    def tech():
        return render_template("tech.html", resources=get_resources())

    @app.route("/tech/<slug>")
    def resource_detail(slug):
        resource = get_resource_by_slug(slug)
        if resource is None:
            abort(404)
        return render_template("resource_detail.html", resource=resource)

    @app.route("/fitness")
    def fitness():
        return render_template("fitness.html")

    @app.route("/robots.txt")
    def robots():
        return send_from_directory(app.static_folder, "robots.txt")

    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template("500.html"), 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
