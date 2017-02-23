from .routes import routes

from .services.app import app

# REGISTER ROUTES
app.register_blueprint(routes)


