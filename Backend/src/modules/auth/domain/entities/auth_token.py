from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str
    role: str


@dataclass
class AuthToken:
    access_token: str
    refresh_token: str
    token_type: str
    user: User