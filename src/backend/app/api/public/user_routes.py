from fastapi import APIRouter, HTTPException

from ...db.db_client import db_client
from ...schemas.public.user_schemas import IUserCreate

router = APIRouter()


@router.post("/create")
async def create_user(user: IUserCreate):
    try:
        response = db_client.auth.sign_up(
            {"email": user.email, "password": user.password}
        )
        return {"message": "User created successfully", "data": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
