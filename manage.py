from flask_site import create_app
from flask_site.common.filters import subtract

app = create_app()

app.jinja_env.filters['subtract'] = subtract

if __name__ == '__main__':
    app.run()
