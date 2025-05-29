from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from enum import Enum

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    children: Mapped[List["Comments"]] = relationship(back_populates="parent")


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            # do not serialize the password, its a security breach
        }




class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))


class Comments(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(500), unique=False, nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    #post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))

    #def serialize(self):
        #return {
            #"id": self.id,
            #"comment_text": self.comment_text,
            #"author_id": self.author_id,
            #"post_id": self.post_id,
        #}


class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    #type: Mapped[Enum] = mapped_column()
    url: Mapped[str] = mapped_column(String(300),  nullable=False)
    #post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    #post: Mapped["Post"] = relationship(back_populates="media")



class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

