# app.py
from flask import Flask
from routes.index import index_bp
from routes.false_position import false_position_bp
from routes.secant import secant_bp


def create_app():
    app = Flask(__name__)

    # Registrar blueprints
    app.register_blueprint(index_bp)
    app.register_blueprint(false_position_bp, url_prefix='/false-position')
    app.register_blueprint(secant_bp, url_prefix='/secant')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
