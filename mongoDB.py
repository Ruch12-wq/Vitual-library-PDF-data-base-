from pymongo import MongoClient
from gridfs import GridFS
from dotenv import load_dotenv
import os

uri = "mongodb+srv://andreypervak_db_user:xWCvCxOfNj4iSv1o@cluster0.aapccem.mongodb.net/"

client = MongoClient(uri)

db = client["library"]

fs = GridFS(db)

collection = db["books"]

