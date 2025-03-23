import uvicorn
from fastapi import FastAPI

from app.api.v1.routes import auth  # noqa
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

# Register API routes
# app.include_router(auth.router, prefix="/auth", tags=["Auth"])
# app.include_router(users.router, prefix="/users", tags=["Users"])
# app.include_router(documents.router, prefix="/documents", tags=["Documents"])
# app.include_router(chat.router, prefix="/chat", tags=["Chat"])
# app.include_router(search.router, prefix="/search", tags=["Search"])


@app.get("/")
async def root():
    return {"message": "AI Healthcare API is running"}


def main():
    """Entry point for the FastAPI server."""
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
