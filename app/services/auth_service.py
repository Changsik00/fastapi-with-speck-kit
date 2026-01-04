from datetime import datetime, timedelta
from typing import Optional, Union, Any
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings
from app.domain.models.user import User

# Password Context
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class AuthService:
    def __init__(self, user_repo: Optional[Any] = None):
        # We might need to inject user_repo here or pass it to methods.
        # However, typical service pattern injects repo in __init__.
        # But for now, let's keep it simple and pass repo to methods or change pattern.
        # Checking ItemService pattern...
        pass

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)

    def create_access_token(self, subject: Union[str, Any], expires_delta: Optional[timedelta] = None) -> str:
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode = {"exp": expire, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    async def login(self, user_repo: Any, form_data: Any) -> Any:
        # Note: We are importing User and Repo interfaces inside methods or at top level if safely possible to avoid circular imports.
        # However, Python handles imports fine mostly.
        # Ideally, Service depends on Repository.
        user = await user_repo.get_by_email(email=form_data.username)
        if not user or not self.verify_password(form_data.password, user.hashed_password):
            return None
        if not user.is_active:
            raise ValueError("Inactive user")
        
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return self.create_access_token(
            subject=user.email, expires_delta=access_token_expires
        )

    async def signup(self, user_repo: Any, user_create_data: Any) -> Any:
        user = await user_repo.get_by_email(email=user_create_data.email)
        if user:
            raise ValueError("User already exists")
        
        hashed_password = self.get_password_hash(user_create_data.password)
        user_in = User(
            email=user_create_data.email,
            hashed_password=hashed_password,
            role=user_create_data.role,
            is_active=True,
        )
        return await user_repo.create(user=user_in)
