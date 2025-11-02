# TODO: JWT auth (register/login/me)
from fastapi import APIRouter
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(): raise NotImplementedError
@router.post("/login")
def login(): raise NotImplementedError
@router.get("/me")
def me(): raise NotImplementedError
