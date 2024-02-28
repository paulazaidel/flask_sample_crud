def register_blueprints(app):
    from app.main.apis import blueprint as api_blueprint

    app.register_blueprint(api_blueprint)


def register_namespaces(api):
    from app.main.apis.category_api import ns as ns_category

    api.add_namespace(ns_category)
