from sqlmodel import SQLModel, Field
import uuid
from datetime import datetime

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(unique=True)
    password_hash: str
    tier: str = "free"
    balance: float = 100000.0
    xp: int = 0
    referral_code: str = Field(default_factory=lambda: ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8)))
