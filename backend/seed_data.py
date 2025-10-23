import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]


SERVICES = [
    {
        "id": "1",
        "slug": "nexus-letters",
        "title": "Nexus Letters",
        "shortDescription": "Professional medical opinions linking service to condition",
        "fullDescription": "A Nexus Letter is a comprehensive medical opinion that establishes a clear connection between your military service and your current medical condition. Written by qualified medical professionals, these letters provide the crucial evidence needed to support your VA disability claim.",
        "features": [
            "Record review",
            "Direct/secondary/aggravation",
            "Clear rationale"
        ],
        "basePriceInINR": 4999,
        "duration": "7-10 business days",
        "category": "nexus-letter",
        "icon": "file-text",
        "faqs": [
            {
                "question": "What is a nexus letter?",
                "answer": "A nexus letter is a medical document that establishes the connection between your military service and your current disability."
            },
            {
                "question": "How long does it take?",
                "answer": "Typically 7-10 business days from the time we receive all necessary medical records."
            }
        ]
    },
    {
        "id": "2",
        "slug": "public-dbqs",
        "title": "Public DBQs",
        "shortDescription": "Standardized disability questionnaires for VA claims",
        "fullDescription": "Disability Benefits Questionnaires (DBQs) are standardized medical examination forms used by the VA to evaluate disability claims. Our licensed physicians complete these forms based on current VA guidelines and your medical condition.",
        "features": [
            "Latest public VA DBQs",
            "Objective findings",
            "Functional impact"
        ],
        "basePriceInINR": 3999,
        "duration": "5-7 business days",
        "category": "dbq",
        "icon": "clipboard",
        "faqs": [
            {
                "question": "Do you complete VA DBQs?",
                "answer": "Yes, we complete public DBQs that are currently accepted by the VA for various conditions."
            }
        ]
    },
    {
        "id": "3",
        "slug": "aid-attendance",
        "title": "Aid & Attendance (21-2680)",
        "shortDescription": "Enhanced pension benefits for veterans needing assistance",
        "fullDescription": "Aid and Attendance is a benefit available to veterans and surviving spouses who require the regular assistance of another person. We provide comprehensive physician evaluations to support your A&A benefit claim.",
        "features": [
            "Physician evaluation",
            "ADL documentation",
            "When clinically indicated"
        ],
        "basePriceInINR": 5999,
        "duration": "10-14 business days",
        "category": "aid-attendance",
        "icon": "heart-pulse",
        "faqs": [
            {
                "question": "Can you help with Aid & Attendance?",
                "answer": "Yes, we provide complete physician evaluations and documentation for VA Form 21-2680."
            }
        ]
    },
    {
        "id": "4",
        "slug": "cp-coaching",
        "title": "C&P Coaching",
        "shortDescription": "Preparation for compensation and pension examinations",
        "fullDescription": "Prepare for your C&P exam with expert coaching. We help you understand what to expect, how to accurately report your symptoms, and provide tips to ensure your disabilities are properly documented.",
        "features": [
            "What to expect",
            "Accurate symptom reporting",
            "Logbooks & lay tips"
        ],
        "basePriceInINR": 2499,
        "duration": "Same day or next business day",
        "category": "coaching",
        "icon": "users",
        "faqs": [
            {
                "question": "What is C&P coaching?",
                "answer": "C&P coaching prepares you for your Compensation and Pension exam, helping you understand the process and communicate your condition effectively."
            }
        ]
    },
    {
        "id": "5",
        "slug": "claim-strategy",
        "title": "Claim Strategy Consult",
        "shortDescription": "Strategic guidance for complex VA claims",
        "fullDescription": "Get expert strategic guidance for your VA claim. We review your evidence, identify gaps, and provide recommendations on how to strengthen your case for the best possible outcome.",
        "features": [
            "Evidence gap map",
            "Secondary links",
            "Testing/referrals"
        ],
        "basePriceInINR": 3499,
        "duration": "3-5 business days",
        "category": "consulting",
        "icon": "lightbulb",
        "faqs": [
            {
                "question": "What does a strategy consult include?",
                "answer": "A comprehensive review of your claim with specific recommendations on evidence needed and next steps."
            }
        ]
    },
    {
        "id": "6",
        "slug": "record-review",
        "title": "Record Review",
        "shortDescription": "Professional analysis of your medical documentation",
        "fullDescription": "Our medical professionals review your service and medical records to identify conditions eligible for VA compensation, build a comprehensive timeline, and prepare targeted questions for your providers.",
        "features": [
            "Service/med records synthesis",
            "Timeline build",
            "Provider question set"
        ],
        "basePriceInINR": 2999,
        "duration": "5-7 business days",
        "category": "review",
        "icon": "file-search",
        "faqs": [
            {
                "question": "What records should I provide?",
                "answer": "Please provide your service treatment records, VA medical records, and any private medical records related to your conditions."
            }
        ]
    }
]

BLOG_POSTS = [
    {
        "id": "1",
        "slug": "what-is-nexus-letter",
        "title": "What is a Nexus Letter?",
        "excerpt": "Plain-English explanation of nexus opinions and what they should include.",
        "contentHTML": "<h2>Understanding Nexus Letters</h2><p>A nexus letter is a medical document that establishes a connection between your military service and your current medical condition. The term 'nexus' means connection or link.</p><h3>Key Components</h3><ul><li>Review of service records</li><li>Review of medical records</li><li>Medical rationale</li><li>Opinion to at least as likely as not standard</li></ul><p>A well-written nexus letter can be the difference between an approved and denied claim.</p>",
        "category": "nexus-letters",
        "tags": ["nexus", "medical opinion"],
        "authorName": "Dr. Sarah Johnson",
        "publishedAt": "SEPT 2025",
        "readTime": "5 min read"
    },
    {
        "id": "2",
        "slug": "how-to-prepare-cp-exam",
        "title": "How to Prepare for a C&P Exam",
        "excerpt": "What to expect at the claim exam and how to communicate symptoms accurately.",
        "contentHTML": "<h2>Preparing for Your C&P Exam</h2><p>The Compensation and Pension (C&P) exam is a critical step in the VA claims process. Here's how to prepare.</p><h3>Before the Exam</h3><ul><li>Gather all relevant medical records</li><li>Keep a symptom diary for at least 2 weeks</li><li>List all medications and treatments</li><li>Note how conditions affect daily life</li></ul><h3>During the Exam</h3><p>Be honest, thorough, and describe your worst days. The examiner needs to understand the full impact of your condition.</p>",
        "category": "exam-prep",
        "tags": ["C&P", "exam prep"],
        "authorName": "Military Disability Team",
        "publishedAt": "SEPT 2025",
        "readTime": "7 min read"
    },
    {
        "id": "3",
        "slug": "aid-attendance-quick-guide",
        "title": "Aid & Attendance (VA Form 21-2680): A Quick Guide",
        "excerpt": "When A&A is appropriate, ADL documentation tips, and physician evaluation basics.",
        "contentHTML": "<h2>Aid & Attendance Benefits</h2><p>Aid and Attendance (A&A) is an additional benefit for veterans who need help with activities of daily living (ADLs).</p><h3>Who Qualifies?</h3><p>Veterans who require assistance with:</p><ul><li>Bathing or dressing</li><li>Eating or using the bathroom</li><li>Adjusting prosthetic devices</li><li>Protection from hazards due to mental conditions</li></ul><h3>Required Documentation</h3><p>VA Form 21-2680 must be completed by a physician who examines the veteran and documents their need for regular aid and attendance.</p>",
        "category": "aid-attendance",
        "tags": ["aid & attendance", "21-2680"],
        "authorName": "Dr. Michael Chen",
        "publishedAt": "SEPT 2025",
        "readTime": "6 min read"
    }
]


async def seed_database():
    print("Starting database seeding...")
    
    # Clear existing data
    await db.services.delete_many({})
    await db.blog_posts.delete_many({})
    
    # Insert services
    if SERVICES:
        await db.services.insert_many(SERVICES)
        print(f"Inserted {len(SERVICES)} services")
    
    # Insert blog posts
    if BLOG_POSTS:
        await db.blog_posts.insert_many(BLOG_POSTS)
        print(f"Inserted {len(BLOG_POSTS)} blog posts")
    
    print("Database seeding completed!")
    client.close()


if __name__ == "__main__":
    asyncio.run(seed_database())
