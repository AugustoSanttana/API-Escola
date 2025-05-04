SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "API Escola",
        "description": "Endpoints API",
    },
    "components": {
        "securityDefinitions": {"basicAuth": {"type": "http", "shema": "basic"}},
    },
    "security": {"basicAuth": []},
}

SWAGGER_CONFIG = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "description": "API Version 1",
            "name": "v1",
            "rule_filter": lambda rule: rule.rule.startswith(""),
        },
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/api",
}