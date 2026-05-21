from dataclasses import dataclass
from datetime import datetime

@dataclass
class Book:
    author: str
    title: str
    rating: int  
    read_date: str

    def to_dict(self):
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "read_date": self.read_date
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            read_date=data["read_date"]
        )
