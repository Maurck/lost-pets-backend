import os

from app.config.config import create_app
from app import blueprint

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')


app.register_blueprint(blueprint)
app.app_context().push()

if __name__ == '__main__':
    app.run()