from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Literal
from fastapi.middleware.cors import CORSMiddleware

from . import models
from . import schemas
from .database import engine, get_db

app = FastAPI(title="Campus Lost & Found API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.patch("/lost-items/{item_id}",
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



@app.post(
    "/found-items",
    response_model=schemas.FoundItemResponse,
    status_code=201
)
def create_found_item(
    item: schemas.FoundItemCreate,
    db: Session = Depends(get_db)
):
    new_item = models.FoundItem(**item.model_dump())

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


@app.get(
    "/found-items",
    response_model=list[schemas.FoundItemResponse]
)
def get_found_items(db: Session = Depends(get_db)):
    return db.query(models.FoundItem).all()


@app.get(
    "/found-items/{item_id}",
    response_model=schemas.FoundItemResponse
)
def get_found_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = db.query(models.FoundItem).filter(
        models.FoundItem.id == item_id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Found item not found"
        )

    return item


@app.patch(
    "/found-items/{item_id}",
    response_model=schemas.FoundItemResponse
)
def update_found_item(
    item_id: int,
    item_data: schemas.FoundItemUpdate,
    db: Session = Depends(get_db)
):
    item = db.query(models.FoundItem).filter(
        models.FoundItem.id == item_id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Found item not found"
        )

    update_data = item_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(item, field, value)

    db.commit()
    db.refresh(item)

    return item


@app.delete("/found-items/{item_id}")
def delete_found_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = db.query(models.FoundItem).filter(
        models.FoundItem.id == item_id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Found item not found"
        )

    db.delete(item)
    db.commit()

    return {"message": "Found item deleted successfully"}

@app.get("/search")
def search_items(
    keyword: str | None = None,
    category: str | None = None,
    location: str | None = None,
    item_type: Literal["lost", "found", "all"] = "all",
    db: Session = Depends(get_db)
):
    results = []

    if item_type in ("lost", "all"):
        query = db.query(models.LostItem)

        if keyword:
            query = query.filter(
                or_(
                    models.LostItem.item_name.ilike(
                        f"%{keyword}%"
                    ),
                    models.LostItem.description.ilike(
                        f"%{keyword}%"
                    )
                )
            )

        if category:
            query = query.filter(
                models.LostItem.category.ilike(
                    f"%{category}%"
                )
            )

        if location:
            query = query.filter(
                models.LostItem.location.ilike(
                    f"%{location}%"
                )
            )

        for item in query.all():
            results.append({
                "id": item.id,
                "item_name": item.item_name,
                "description": item.description,
                "category": item.category,
                "location": item.location,
                "date": item.date_lost,
                "item_type": "lost"
            })

    if item_type in ("found", "all"):
        query = db.query(models.FoundItem)

        if keyword:
            query = query.filter(
                or_(
                    models.FoundItem.item_name.ilike(
                        f"%{keyword}%"
                    ),
                    models.FoundItem.description.ilike(
                        f"%{keyword}%"
                    )
                )
            )

        if category:
            query = query.filter(
                models.FoundItem.category.ilike(
                    f"%{category}%"
                )
            )

        if location:
            query = query.filter(
                models.FoundItem.location.ilike(
                    f"%{location}%"
                )
            )

        for item in query.all():
            results.append({
                "id": item.id,
                "item_name": item.item_name,
                "description": item.description,
                "category": item.category,
                "location": item.location,
                "date": item.date_found,
                "item_type": "found"
            })

    return results