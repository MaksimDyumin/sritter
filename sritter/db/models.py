from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    password = Column(String(120))

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r})"

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    title = Column(String(50))
    
    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"Post(id={self.id!r}, text={self.text!r}, title={self.title!r})"