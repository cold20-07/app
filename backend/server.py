from fastapi import FastAPI, APIRouter, HTTPException, Query
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import List, Optional
import uuid
from datetime import datetime, timezone


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


# ===== MODELS =====
class Service(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    slug: str
    title: str
    shortDescription: str
    fullDescription: str
    features: List[str]
    basePriceInINR: int
    duration: str
    category: str
    icon: str
    faqs: List[dict]


class BlogPost(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    slug: str
    title: str
    excerpt: str
    contentHTML: str
    category: str
    tags: List[str]
    authorName: str
    publishedAt: str
    readTime: str


class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    subject: str
    message: str


class Contact(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    name: str
    email: str
    phone: Optional[str] = None
    subject: str
    message: str
    status: str = "new"
    createdAt: str


# ===== ROUTES =====
@api_router.get("/")
async def root():
    return {"message": "Veteran Nexus API"}


@api_router.get("/services", response_model=List[Service])
async def get_services():
    services = await db.services.find({}, {"_id": 0}).to_list(100)
    return services


@api_router.get("/services/{slug}", response_model=Service)
async def get_service_by_slug(slug: str):
    service = await db.services.find_one({"slug": slug}, {"_id": 0})
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service


@api_router.get("/blog", response_model=List[BlogPost])
async def get_blog_posts(
    category: Optional[str] = Query(None),
    q: Optional[str] = Query(None),
    limit: int = Query(20, le=100)
):
    query = {}
    if category:
        query["category"] = category
    if q:
        query["$or"] = [
            {"title": {"$regex": q, "$options": "i"}},
            {"excerpt": {"$regex": q, "$options": "i"}}
        ]
    
    posts = await db.blog_posts.find(query, {"_id": 0}).to_list(limit)
    return posts


@api_router.get("/blog/{slug}", response_model=BlogPost)
async def get_blog_post(slug: str):
    post = await db.blog_posts.find_one({"slug": slug}, {"_id": 0})
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return post


@api_router.post("/contact", response_model=Contact)
async def create_contact(contact_data: ContactCreate):
    contact_dict = contact_data.model_dump()
    contact_obj = Contact(
        id=str(uuid.uuid4()),
        **contact_dict,
        createdAt=datetime.now(timezone.utc).isoformat()
    )
    
    doc = contact_obj.model_dump()
    await db.contacts.insert_one(doc)
    
    return contact_obj


# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
