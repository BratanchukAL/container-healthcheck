from fastapi import status

from bootstrap import app


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def healthcheck() -> None:
    pass


__all__ = []
