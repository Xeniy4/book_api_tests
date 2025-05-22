from __future__ import annotations

from pydantic import BaseModel


class BookingdatesModel(BaseModel):
    checkin: str
    checkout: str


class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingdatesModel
    additionalneeds: str


class CreateModel(BaseModel):
    bookingid: int
    booking: BookingModel
