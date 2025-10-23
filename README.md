# Veteran Nexus & DBQ Services MVP

A modern, full-stack web application for veteran medical documentation services including nexus letters, DBQs, and consultation services.

## 🚀 Tech Stack

- **Frontend**: React 19 + React Router + Tailwind CSS + Shadcn UI
- **Backend**: FastAPI (Python) + Motor (MongoDB async driver)
- **Database**: MongoDB
- **State Management**: React Hooks
- **Form Handling**: React Hook Form + Zod validation
- **UI Components**: Shadcn UI with Radix UI primitives
- **Notifications**: Sonner (toast notifications)

## 📁 Project Structure

```
/app
├── backend/
│   ├── server.py           # FastAPI application with API routes
│   ├── seed_data.py        # Database seeding script
│   ├── requirements.txt    # Python dependencies
│   └── .env                # Backend environment variables
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/         # Shadcn UI components
│   │   │   ├── Header.js
│   │   │   ├── Footer.js
│   │   │   └── Layout.js
│   │   ├── pages/
│   │   │   ├── Home.js
│   │   │   ├── Services.js
│   │   │   ├── ServiceDetail.js
│   │   │   ├── Blog.js
│   │   │   ├── BlogPost.js
│   │   │   ├── About.js
│   │   │   └── Contact.js
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   ├── package.json
│   └── .env                # Frontend environment variables
└── README.md
```

## 🎯 Features Implemented

### Core Pages
- **Home**: Hero section, services preview, trust badges, how it works, blog previews, CTA sections
- **Services**: Grid view of all 6 services with pricing and features
- **Service Detail**: Individual service pages with detailed info, FAQs (using Shadcn Accordion)
- **Blog**: List view with search and category filtering
- **Blog Post**: Individual article pages with formatted content
- **About**: Mission, values, credentials, approach, team info
- **Contact**: Contact form with validation and success state

### Services Offered (6 Total)
1. Nexus Letters - ₹4,999
2. Public DBQs - ₹3,999
3. Aid & Attendance (21-2680) - ₹5,999
4. C&P Coaching - ₹2,499
5. Claim Strategy Consult - ₹3,499
6. Record Review - ₹2,999

### Backend API Endpoints
- `GET /api/services` - List all services
- `GET /api/services/:slug` - Get single service
- `GET /api/blog?category=&q=&limit=` - List blog posts with filters
- `GET /api/blog/:slug` - Get single blog post
- `POST /api/contact` - Submit contact form

### Design Features
- Modern, professional healthcare aesthetic
- Teal/emerald color scheme (avoiding dark gradients)
- Space Grotesk + Manrope typography
- Smooth animations and transitions
- Responsive design (mobile, tablet, desktop)
- Glass-morphism effects
- Hover states and micro-interactions
- Accessible components (Shadcn UI)

## 🛠 Local Development

### Prerequisites
- MongoDB running on `localhost:27017`
- Node.js 18+ and Yarn
- Python 3.11+

### Backend Setup

```bash
cd /app/backend

# Install dependencies
pip install -r requirements.txt

# Seed the database
python seed_data.py

# Start backend (managed by supervisor)
sudo supervisorctl restart backend
```

### Frontend Setup

```bash
cd /app/frontend

# Install dependencies
yarn install

# Start development server (managed by supervisor)
sudo supervisorctl restart frontend
```

### Check Services Status

```bash
sudo supervisorctl status
```

## 🌐 Environment Variables

### Backend (.env)
```
MONGO_URL=mongodb://localhost:27017
DB_NAME=test_database
CORS_ORIGINS=*
```

### Frontend (.env)
```
REACT_APP_BACKEND_URL=https://va-services-hub.preview.emergentagent.com
WDS_SOCKET_PORT=443
```

## 📊 Database Schema

### Services Collection
```json
{
  "id": "string",
  "slug": "string",
  "title": "string",
  "shortDescription": "string",
  "fullDescription": "string",
  "features": ["string"],
  "basePriceInINR": "number",
  "duration": "string",
  "category": "string",
  "icon": "string",
  "faqs": [{"question": "string", "answer": "string"}]
}
```

### Blog Posts Collection
```json
{
  "id": "string",
  "slug": "string",
  "title": "string",
  "excerpt": "string",
  "contentHTML": "string",
  "category": "string",
  "tags": ["string"],
  "authorName": "string",
  "publishedAt": "string",
  "readTime": "string"
}
```

### Contacts Collection
```json
{
  "id": "string",
  "name": "string",
  "email": "string",
  "phone": "string (optional)",
  "subject": "string",
  "message": "string",
  "status": "new|in-progress|resolved",
  "createdAt": "ISO timestamp"
}
```

## 🧪 Testing

### Test Backend API
```bash
# Get all services
curl https://va-services-hub.preview.emergentagent.com/api/services

# Get specific service
curl https://va-services-hub.preview.emergentagent.com/api/services/nexus-letters

# Submit contact form
curl -X POST https://va-services-hub.preview.emergentagent.com/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "subject": "Test Inquiry",
    "message": "This is a test message"
  }'
```

### Check Logs
```bash
# Backend logs
tail -f /var/log/supervisor/backend.*.log

# Frontend logs  
tail -f /var/log/supervisor/frontend.*.log
```

## 📦 Export to GitHub

This project is ready to be exported to GitHub:

```bash
# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "feat: Initial MVP with all core features"

# Add remote
git remote add origin <your-github-repo-url>

# Push
git push -u origin main
```

## 🔄 Future Enhancements (Not in MVP)

Features intentionally left out of MVP that can be added later:

1. **Full Booking Funnel** (6-step wizard with date/time selection, file uploads, mock payment)
2. **Admin Dashboard** (read-only stats, appointments management, contacts CRM)
3. **User Authentication** (JWT-based login/signup)
4. **Real Payment Integration** (Stripe or similar)
5. **File Upload System** (AWS S3 or Cloudinary)
6. **Email Notifications** (SendGrid or similar)
7. **Appointment Scheduling** (calendar integration)
8. **Search Functionality** (full-text search)
9. **SEO Optimization** (meta tags, sitemap, schema markup)
10. **Analytics** (Google Analytics, custom events)

## 🎨 Design Guidelines

- **Typography**: Space Grotesk (headings), Manrope (body)
- **Colors**: 
  - Primary: Teal 600 (#0d9488)
  - Secondary: Emerald 600 (#059669)
  - Background: Slate 50 (#f8fafc)
  - Text: Slate 900 (#0f172a)
- **Spacing**: Generous padding (2-3x normal)
- **Components**: All interactive elements have hover states
- **Accessibility**: WCAG 2.1 AA compliant (via Shadcn)

## 📝 Notes

- All prices are in INR (Indian Rupees) with ₹ symbol
- Mock data includes 6 services and 3 blog posts
- Contact form submissions are stored in MongoDB
- No authentication required for MVP
- All API routes use `/api` prefix for proper routing
- Services are running on supervisor (auto-restart enabled)

## 🤝 Support

For questions or issues, please check the logs or contact support.

---

**Built with ❤️ for Veterans**
