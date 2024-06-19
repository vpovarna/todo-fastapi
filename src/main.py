import uvicorn

from config.config import get_app_config

if __name__ == '__main__':
    app_config = get_app_config()
    server_config = app_config.server

    uvicorn.run(
        host=server_config.server_host,
        port=server_config.server_port,
        app="app:app",
        reload=True
    )
