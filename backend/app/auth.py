from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()
pwd = CryptContext(schemes=["bcrypt"])

@router.post("/signup")
async def signup(email: str, password: str, session):
    hashed = pwd.hash(password)
    user = User(email=email, password_hash=hashed)
    session.add(user)
    await session.commit()
    return {"msg": "User created"}
