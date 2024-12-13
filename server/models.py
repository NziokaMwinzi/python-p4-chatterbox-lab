from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

# Define naming convention for foreign keys
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Initialize db with the naming convention
db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    # Define the table columns
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)  # Message content
    username = db.Column(db.String, nullable=False)  # User who posted
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow
    )  # Timestamp of creation
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # String representation of a Message object
    def __repr__(self):
        return f'<Message by {self.username}: {self.body[:10]}...>'