from flask import jsonify
from datetime import datetime, UTC
from app.config import Config
from app.logger import logger

def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({
            "application": Config.APP_NAME,
            "status": "running",
            "version": Config.VERSION,
            "environment": Config.ENVIRONMENT,
            "timestamp": datetime.now(UTC).isoformat()
        })

    @app.route("/health")
    def health():
        return jsonify({
            "status": "healthy"
        })

    @app.route("/version")
    def version():
        return jsonify({
            "version": Config.VERSION
        })

    @app.route("/info")
    def info():
        return jsonify({
            "project": "DevOps Platform Project",
            "owner": "Orisakwe Michael",
            "stack": [
                "Python",
                "Flask",
                "Docker",
                "GitHub Actions",
                "Terraform",
                "AWS",
                "Kubernetes"
            ]
        })