from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Index

db = SQLAlchemy()

# class Card_image(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     NAME = db.Column(db.Text)
#     DESCRIPTION = db.Column(db.Text)
#     CLASS = db.Column(db.Text)
#     EFFECT = db.Column(db.Text)
#     VISUAL_DESCRIPTION = db.Column(db.Text)
#     ATK = db.Column(db.Text)
#     DEF = db.Column(db.Text)
#     TYPE = db.Column(db.Text)
#     CATEGORY = db.Column(db.Text)
#     COST = db.Column(db.Text)
#     COST_TYPE = db.Column(db.Text)
#     IMAGE_APROVED = db.Column(db.Text)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


# class GeneratedImage(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     image_prompt = db.Column(db.Text)
#     image_card = db.Column(db.Text)
#     image_url = db.Column(db.Text)
#     valid = db.Column(db.Integer)
#     status = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
