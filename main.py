from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db

app = FastAPI(title="Campus Lost & Found API")

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Campus Lost & Found API is running"}


@app.post("/lost-items", response_model=schemas.LostItemResponse,
          status_code=201)
def create_lost_item(
    item: schemas.LostItemCreate,
    db: Session = Depends(get_db)
):
    new_item = models.LostItem(**item.model_dump())

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


@app.get("/lost-items", response_model=list[schemas.LostItemResponse])
def get_lost_items(db: Session = Depends(get_db)):
    items = db.query(models.LostItem).all()
    return items


@app.get("/lost-items/{item_id}",
         response_model=schemas.LostItemResponse)
def get_lost_item(item_id: int, db: Session = Depends(get_db)):
    item = (
        db.query(models.LostItem)
        .filter(models.LostItem.id == item_id)
        .first()
    )

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Lost item not found"
        )

    return item


@app.put("/lost-items/{item_id}",
         response_model=schemas.LostItemResponse)
def update_lost_item(
    item_id: int,
    item_data: schemas.LostItemUpdate,
    db: Session = Depends(get_db)
):
    item = (
        db.query(models.LostItem)
        .filter(models.LostItem.id == item_id)
        .first()
    )

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Lost item not found"
        )

    update_data = item_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(item, field, value)

    db.commit()
    db.refresh(item)

    return item


@app.delete("/lost-items/{item_id}")
def delete_lost_item(item_id: int, db: Session = Depends(get_db)):
    item = (
        db.query(models.LostItem)
        .filter(models.LostItem.id == item_id)
        .first()
    )

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Lost item not found"
        )

    db.delete(item)
    db.commit()

    return {"message": "Lost item deleted successfully"}