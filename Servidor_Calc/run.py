#!/usr/bin/python3.5
"""Run API module."""

from app import app


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
