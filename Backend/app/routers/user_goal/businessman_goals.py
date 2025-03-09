from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ...controllers.UserGoalsController.businessman_goals import UserGoalsController

router = APIRouter(
    prefix="/user_goals",
    tags=["User_goals"]
)

class UpdateUserGoalsRequest(BaseModel):
    goal: float
    frecuency_goal: str

@router.put("/update/{user_id}")
def update_user_goals(user_id: int, request: UpdateUserGoalsRequest):
    user_goals_controller = UserGoalsController()
    response = user_goals_controller.update_user_goals(user_id, request.goal, request.frecuency_goal)
    return {"message": "User goals updated successfully"}

@router.get("/check_goal/{user_id}")
def check_goal(user_id: int):
    user_goals_controller = UserGoalsController()
    result = user_goals_controller.check_goal_achieved(user_id)
    
    return result