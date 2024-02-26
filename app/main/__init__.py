def register_blueprints(app):
    from app.main.apis import blueprint as api_blueprint

    app.register_blueprint(api_blueprint)
