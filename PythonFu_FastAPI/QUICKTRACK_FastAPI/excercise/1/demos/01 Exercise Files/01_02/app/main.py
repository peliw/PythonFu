from fastapi import FastAPI

app = FastAPI(
    title="Inventory management API",
    description="APIs for managing inventory",
    version="1.0.0"
)

@app.get("/health", tags=["HealthCheck"])
async def health_check():
    '''health check endpoint to moitor api uptime'''
    return {
        "status" : "online",
        "message" : "inventory management api is running"
    }


# # for development environment only
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app",
        host="127.0.0.1", port=8000,
        reload=True)