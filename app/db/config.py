DATABASE_CONFIG = {
    "connections": {
        "default": f'postgres://admin:'
                   f'admin@'
                   f'127.0.0.1:'
                   f'5433/'
                   f'admin'},
    "apps": {
        "models": {
            "models": ["app.db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
