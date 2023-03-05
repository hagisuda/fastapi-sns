from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import User, Post, Gender

app = FastAPI()

db_users: List[User] = [
    User(
        id = 1,
        profile_picture = "assets/person/1.jpeg",
        username = "Safak Kocaoglu",
        first_name = "",
        last_name = "",
        gender=Gender.female,
    ),
    User(
        id = 2,
        profile_picture = "assets/person/2.jpeg",
        username = "Janell Shrum",
        first_name = "",
        last_name = "",
        gender=Gender.female,
    ),
    User(
        id = 3,
        profile_picture = "assets/person/3.jpeg",
        username = "Alex Durden",
        first_name = "",
        last_name = "",
        gender=Gender.female,
    ),
    User(
        id = 4,
        profile_picture = "assets/person/4.jpeg",
        username = "Dora Hawks",
        first_name = "",
        last_name = "",
        gender=Gender.female,
    ),
    User(
        id = 5,
        profile_picture = "assets/person/5.jpeg",
        username = "Thomas Holden",
        first_name = "",
        last_name = "",
        gender=Gender.female,
    ),
    User(
        id = 6,
        profile_picture = "assets/person/6.jpeg",
        username = "Shirley Beauchamp",
        first_name = "",
        last_name = "",
        gender=Gender.female,
    ),
    User(
        id = 7,
        profile_picture = "assets/person/7.jpeg",
        username = "Travis Bennett",
        first_name = "",
        last_name = "",
        gender=Gender.female,
    ),
    User(
        id = 8,
        profile_picture = "assets/person/8.jpeg",
        username = "Kristen Thomas",
        first_name = "",
        last_name = "",
        gender=Gender.female,
    ),
    User(
        id = 9,
        profile_picture = "assets/person/9.jpeg",
        username = "Gary Duty",
        first_name = "",
        last_name = "",
        gender=Gender.female,
    ),
    User(
        id = 10,
        profile_picture = "assets/person/10.jpeg",
        username = "Hak Choi",
        first_name = "",
        last_name = "",
        gender=Gender.male,
    ),
]

db_posts: List[Post] = [
    Post(
        id = 1,
        desc = "Love For All, Hatred For None.",
        photo = "assets/post/1.jpeg",
        date = "5 mins ago",
        user_id = 1,
        like = 32,
        comment = 9,
    ),
    Post(
        id = 2,
        photo = "assets/post/2.jpeg",
        date = "15 mins ago",
        user_id = 2,
        like = 2,
        comment = 1,
    ),
    Post(
        id = 3,
        desc = "Every moment is a fresh beginning.",
        photo = "assets/post/3.jpeg",
        date = "1 hour ago",
        user_id = 3,
        like = 61,
        comment = 2,
    ),
    Post(
        id = 4,
        photo = "assets/post/4.jpeg",
        date = "4 hours ago",
        user_id = 4,
        like = 7,
        comment = 3,
    ),
    Post(
        id = 5,
        photo = "assets/post/5.jpeg",
        date = "5 hours ago",
        user_id = 5,
        like = 23,
        comment = 5,
    ),
    Post(
        id = 6,
        photo = "assets/post/6.jpeg",
        date = "1 day ago",
        user_id = 6,
        like = 44,
        comment = 6,
    ),
    Post(
        id = 7,
        desc = "Never regret anything that made you smile.",
        photo = "assets/post/7.jpeg",
        date = "2 days ago",
        user_id = 7,
        like = 52,
        comment = 3,
    ),
    Post(
        id = 8,
        photo = "assets/post/8.jpeg",
        date = "3 days ago",
        user_id = 8,
        like = 15,
        comment = 1,
    ),
    Post(
        id = 9,
        desc = "Change the world by being yourself.",
        photo = "assets/post/9.jpeg",
        date = "5 days ago",
        user_id = 9,
        like = 11,
        comment = 2,
    ),
    Post(
        id = 10,
        photo = "assets/post/10.jpeg",
        date = "1 week ago",
        user_id = 10,
        like = 104,
        comment = 12,
    ),
    
]

@app.get("/")
def roo():
    return {"Hello": "Mundo!"}

@app.get("/api/v1/users")
async def users():
    return db_users;

@app.get("/api/v1/posts")
async def posts():
    return db_posts;
