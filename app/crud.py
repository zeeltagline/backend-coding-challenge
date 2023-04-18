from sqlalchemy.orm import Session

from . import models, schemas


def create_planning(db: Session, planning: schemas.PlanningCreate) -> models.Planning:
    db_planning = models.Planning(**planning.dict())
    db.add(db_planning)
    db.commit()
    db.refresh(db_planning)
    return db_planning


def get_planning(db: Session, planning_id: int) -> models.Planning:
    return db.query(models.Planning).filter(models.Planning.id == planning_id).first()


def get_plannings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Planning).offset(skip).limit(limit).all()


def update_planning(
    db: Session, planning: models.Planning, planning_update: schemas.PlanningUpdate
) -> models.Planning:
    for field, value in planning_update.dict(exclude_unset=True).items():
        setattr(planning, field, value)
    db.add(planning)
    db.commit()
    db.refresh(planning)
    return planning


def delete_planning(db: Session, planning_id: int) -> models.Planning:
    planning = (
        db.query(models.Planning).filter(models.Planning.id == planning_id).first()
    )
    db.delete(planning)
    db.commit()
    return planning
