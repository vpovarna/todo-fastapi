from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from db.session import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    completed = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=None, nullable=True)
    completed_at = Column(DateTime, server_default=None, nullable=True)

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, completed={self.completed})>"
