from typing import Optional

from sqlmodel import Field, SQLModel


class Sports_Facilities(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    ida_code: Optional[int] = None
    facility_name: Optional[str] = None
    province: Optional[str] = None
    town: Optional[str] = None
    street_name: Optional[str] = None
    postal_code: Optional[int] = None
    sport_area: Optional[str] = None
