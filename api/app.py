from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import json
import uvicorn
from routers import router
import pathlib


app = FastAPI()
app.include_router(router.router)

if __name__ == "__main__":
    cwd = pathlib.Path(__file__).parent.resolve()
    # add log
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True, log_config=f"{cwd}/log.ini")