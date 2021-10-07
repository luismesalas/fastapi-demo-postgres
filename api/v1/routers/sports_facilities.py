from fastapi import APIRouter
from sqlmodel import Session, select

from api.model.sports_facilities import Sports_Facilities
from api.utils.db_engine import DBEngine

router = APIRouter()


@router.get("/filter-province-like")
def filter_sports_facilities_by_province_like(province: str):
    with Session(DBEngine().get_db_engine()) as session:
        statement = select(Sports_Facilities) \
            .where(Sports_Facilities.province.like(f"%{province}%"))
        sport_facilities_records = session.exec(statement).all()
        return sport_facilities_records


@router.get("/filter-town-like")
def filter_sports_facilities_by_town_like(town: str):
    with Session(DBEngine().get_db_engine()) as session:
        statement = select(Sports_Facilities) \
            .where(Sports_Facilities.town.like(f"%{town}%"))
        sport_facilities_records = session.exec(statement).all()
        return sport_facilities_records


@router.get("/list-by-province-and-town")
def list_sports_facilities_by_province_and_town(province: str, town: str):
    with Session(DBEngine().get_db_engine()) as session:
        statement = select(Sports_Facilities).where(Sports_Facilities.province == province,
                                                    Sports_Facilities.town == town)
        sport_facilities_records = session.exec(statement).all()
        return sport_facilities_records


@router.get("/list-by-postal-code")
def list_sports_facilities_by_postal_code(postal_code: int):
    with Session(DBEngine().get_db_engine()) as session:
        statement = select(Sports_Facilities).where(Sports_Facilities.postal_code == postal_code)
        sport_facilities_records = session.exec(statement).all()
        return sport_facilities_records


# Order matters. This method should be at the end of the router for avoiding to override sub-path methods
@router.get("/{id}")
def get_details_of_sport_facility(id: int):
    with Session(DBEngine().get_db_engine()) as session:
        statement = select(Sports_Facilities).where(Sports_Facilities.id == id)
        cross_selling_record = session.exec(statement).first()
        return cross_selling_record
