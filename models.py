from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    activities = db.Column(db.Text, nullable=False)
    participants = db.Column(db.Integer, default=0)  # Number of people gone
    days = db.relationship('ItineraryDay', backref='itinerary', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'location': self.location,
            'duration': self.duration,
            'created_date': self.created_date.isoformat() if self.created_date else None,
            'activities': self.activities,
            'participants': self.participants,
            'days': [day.to_dict() for day in self.days]
        }

class ItineraryDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False)
    day_number = db.Column(db.Integer, nullable=False)
    morning = db.Column(db.String(200))
    afternoon = db.Column(db.String(200))
    evening = db.Column(db.String(200))
    notes = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'itinerary_id': self.itinerary_id,
            'day_number': self.day_number,
            'morning': self.morning,
            'afternoon': self.afternoon,
            'evening': self.evening,
            'notes': self.notes
        }