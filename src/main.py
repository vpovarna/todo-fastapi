import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        host="0.0.0.0",
        port=18081,
        app="app:app",
        reload=True
    )
