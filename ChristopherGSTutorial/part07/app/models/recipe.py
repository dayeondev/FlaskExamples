import sys
sys.path.insert(0, '/home/dayeon/Workspace/ChristopherGSTutorial')
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from part07.app.db.base_class import Base


class Recipe(Base):  # 1
    id = Column(Integer, primary_key=True, index=True)  # 2
    label = Column(String(256), nullable=False)
    url = Column(String(256), index=True, nullable=True)
    source = Column(String(256), nullable=True)
    submitter_id = Column(String(10), ForeignKey("user.id"), nullable=True)  # 3
    submitter = relationship("User", back_populates="recipes")  # 4