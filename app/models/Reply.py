from datetime import datetime

from app import db
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import DateTime, Integer, Text


class Reply(db.Model):
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User")
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    vote = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def get_created_at(self):
        import pytz
        import tzlocal
        local_timezone = tzlocal.get_localzone()
        local_time = self.created_at.replace(
            tzinfo=pytz.utc).astimezone(local_timezone)
        return local_time.strftime("%H:%M, %B %d %Y")
