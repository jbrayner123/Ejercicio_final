from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth import router as auth_router
from .routers import graph as graph_router
from .routers import algorithms as algo_router
import os

app = FastAPI(title="PathFinder Minimal API")
origins = [os.getenv("CORS_ORIGINS","http://localhost:5173")]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(auth_router)
app.include_router(graph_router.router)
app.include_router(algo_router.router)
