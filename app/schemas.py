from typing import List, Optional
from pydantic import BaseModel, validator
from datetime import datetime

class Skill(BaseModel):
    name: str
    level: int

    @validator('level')
    def validate_level(cls, v):
        if not 1 <= v <= 5:
            raise ValueError('level must be between 1 and 5')
        return v


class PlanningBase(BaseModel):
    original_id: str
    operating_unit: str
    office_postal_code: str
    total_hours: float
    start_date: datetime
    end_date: datetime
    client_id: str
    is_unassigned: bool

    class Config:
        orm_mode = True


class PlanningCreate(PlanningBase):
    talent_id: Optional[str] = None
    talent_name: Optional[str] = None
    talent_grade: Optional[str] = None
    booking_grade: Optional[str] = None
    office_city: Optional[str] = None
    job_manager_name: Optional[str] = None
    job_manager_id: Optional[str] = None
    client_name: Optional[str] = None
    industry: Optional[str] = None
    required_skills: Optional[List[Skill]] = None
    optional_skills: Optional[List[Skill]] = None


class PlanningUpdate(PlanningBase):
    talent_id: Optional[str] = None
    talent_name: Optional[str] = None
    talent_grade: Optional[str] = None
    booking_grade: Optional[str] = None
    office_city: Optional[str] = None
    job_manager_name: Optional[str] = None
    job_manager_id: Optional[str] = None
    client_name: Optional[str] = None
    industry: Optional[str] = None
    required_skills: Optional[List[Skill]] = None
    optional_skills: Optional[List[Skill]] = None


class Planning(PlanningBase):
    id: int

    class Config:
        orm_mode = True
