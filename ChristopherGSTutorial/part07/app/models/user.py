import sys
sys.path.insert(0, '/home/dayeon/Workspace/ChristopherGSTutorial')
from sqlalchemy import Column, Integer, String, Boolean ForeignKey
from sqlalchemy.orm import relationship

from part07.app.db.base_class import Base



class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(256), nullable=True)
    surname = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
    recipes = relationship(
        "Recipe",
        cascade="all,delete-orphan",
        back_populates="submitter",
        uselist=True,
    )