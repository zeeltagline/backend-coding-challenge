from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Planning)
def create_planning(planning: schemas.PlanningCreate, db: Session = Depends(get_db)):
    return crud.create_planning(db=db, planning=planning)


@router.get("/", response_model=List[schemas.Planning])
def read_plannings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    plannings = crud.get_plannings(db, skip=skip, limit=limit)
    return plannings


@router.get("/{planning_id}", response_model=schemas.Planning)
def read_planning(planning_id: int, db: Session = Depends(get_db)):
    db_planning = crud.get_planning(db, planning_id=planning_id)
    if db_planning is None:
        raise HTTPException(status_code=404, detail="Planning not found")
    return db_planning


@router.put("/{planning_id}", response_model=schemas.Planning)
def update_planning(
    planning_id: int, planning: schemas.PlanningUpdate, db: Session = Depends(get_db)
):
    updated_planning = crud.update_planning(
        db, planning_id=planning_id, planning=planning
    )
    if updated_planning is None:
        raise HTTPException(status_code=404, detail="Planning not found")
    return updated_planning


@router.delete("/{planning_id}", response_model=schemas.Planning)
def delete_planning(planning_id: int, db: Session = Depends(get_db)):
    deleted_planning = crud.delete_planning(db, planning_id=planning_id)
    if deleted_planning is None:
        raise HTTPException(status_code=404, detail="Planning not found")
    return deleted_planning
