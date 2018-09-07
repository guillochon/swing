"""Interface for gunicorn.

Run a server locally with:
> gunicorn wsgi:app.server
"""
from server import app

if __name__ == "__main__":
    app.run()
