# 42Nexus - Project Overview

## 🚀 Platform Name: **42Nexus**

A collaborative platform for 42 students navigating the new Python common core.

---

## ⏱️ Total Time Budget: <40 Hours

| Developer | Role | Time |
|-----------|------|------|
| **Frontend** | UI/UX, React pages | 13-16h |
| **Backend 1** | Auth, Users, Voting, Disputes | 11-16h |
| **Backend 2** | Resources, Tests | 9-12h |
| **Backend 3** | Database setup (MariaDB + phpMyAdmin) | 6-8h |

**Working in parallel = ~16-18 hours total!**

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | React + Vite + TailwindCSS |
| **Backend** | FastAPI (Python) |
| **Database** | PostgreSQL (Supabase) |
| **DB Admin** | Supabase Dashboard |
| **Auth** | 42 OAuth API |

---

## 📁 Project Files

| File | Description |
|------|-------------|
| [TODO_FRONTEND.md](TODO_FRONTEND.md) | Frontend developer tasks |
| [TODO_BACKEND_1.md](TODO_BACKEND_1.md) | Auth, Users, Voting, Disputes |
| [TODO_BACKEND_2.md](TODO_BACKEND_2.md) | Resources & Tests features |
| [TODO_BACKEND_3.md](TODO_BACKEND_3.md) | Database setup (MariaDB) |

---

## 🎯 Core Features

### 1. 🔐 Authentication
- Login with 42 OAuth
- Student vs Staff roles

### 2. 📚 Resources Hub
- Share learning materials
- Upvote/downvote system

### 3. 🗳️ Subject Votes
- Ask clarification questions
- Community votes on answers
- **Staff Override**: Staff decision is FINAL

### 4. ⚡ Live Disputes
- Real-time correction disagreements
- Vote for corrector or corrected
- **Staff Override**: Staff decision is FINAL

### 5. 🧪 Tests Repository
- Share test cases
- Download counter
- Staff approval system

---

## 🔄 Development Order

```
1. Backend Dev 3: Database Setup (FIRST - others depend on this!)
   ↓
2. Backend Dev 1: Auth & Users (needs DB)
   ↓
3. Backend Dev 1: Voting & Disputes (after auth)
   Backend Dev 2: Resources & Tests (parallel)
   ↓
4. Frontend: Can start with mock data, integrate when APIs ready
```

---

## 🗄️ Database Tables (10 total)

1. `users` - 42 user accounts
2. `projects` - Python common core projects
3. `resources` - Learning materials
4. `resource_votes` - Upvotes/downvotes
5. `tests` - Test cases
6. `subject_votes` - Clarification questions
7. `vote_options` - Answer options
8. `user_votes` - User's answers
9. `disputes` - Correction disagreements
10. `dispute_votes` - Dispute votes

---

## 🔑 Key Feature: Staff Override

When a **staff member** makes a decision on any vote or dispute:
- The vote/dispute is **immediately closed**
- Staff's decision is **FINAL**
- Even if 100 people voted differently, staff wins

This is the unique value proposition of 42Nexus!

---

## 🚦 Quick Start

### Backend Dev 3 (Database) - START FIRST!
```bash
# Go to https://supabase.com
# Create new project "42nexus"
# Run SQL script in SQL Editor
# Share connection string with team
```

### Backend Dev 1 & 2
```bash
cd backend
pip install -r requirements.txt
# Wait for DB credentials from Dev 3
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

---

Good luck with the hackathon! 🏆
