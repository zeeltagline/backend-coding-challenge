from sqlalchemy import JSON, Boolean, Column, DateTime, Float, Integer, String

from .database import Base


class Planning(Base):
    __tablename__ = "planning"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    original_id = Column(String, unique=True, nullable=False)
    talent_id = Column(String)
    talent_name = Column(String)
    talent_grade = Column(String)
    booking_grade = Column(String)
    operating_unit = Column(String, nullable=False)
    office_city = Column(String)
    office_postal_code = Column(String, nullable=False)
    job_manager_name = Column(String)
    job_manager_id = Column(String)
    total_hours = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    client_name = Column(String)
    client_id = Column(String, nullable=False)
    industry = Column(String)
    required_skills = Column(JSON)
    optional_skills = Column(JSON)
    is_unassigned = Column(Boolean)
