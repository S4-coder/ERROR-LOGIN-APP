from datetime import datetime
from src.utils.db_utils import db

class ErrorLog(db.Model):
    __tablename__ = 'error_logs'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1024), nullable=False)
    category = db.Column(db.String(255), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    metadata = db.Column(db.JSON, nullable=True)

    def __repr__(self):
        return f"<ErrorLog id={self.id} category={self.category} timestamp={self.timestamp}>"
