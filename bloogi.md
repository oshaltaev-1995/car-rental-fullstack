
# 🌟 **WebSovellusKehitys-2025, personal notes**

---

# **Intro**

Over the past few months, I’ve been diving deeper into fullstack development, and this project became an unexpected but very meaningful milestone in my learning path. What started as a simple idea—reusing an old Angular demo from a summer course—turned into a full-scale full-stack deployment journey involving containers, cloud hosting, backend engineering, debugging, and a lot of lessons learned along the way.

---

## **Where It All Started**

My interest in frontend development didn’t appear overnight.
In fact, it goes back almost **15 years**, when I first experimented with HTML and CSS and built simple static pages just for fun.

Fast-forward to last summer — I took additional UI layout courses through LUT/Finntech, and later completed an intensive Angular & TypeScript bootcamp offered by a private Russian company. Those bootcamps usually try to funnel students into paid programs (which can cost around €1200–1500 for a year), but I walked away mainly with a **demo Angular project**—a static car-rental landing page.

It wasn’t much, but it was something. And it was mine.

So when our university fullstack course began, I realized:

> *Why not use this as a foundation?*
> *I could save time, learn more deeply, and practice real-world deployment before starting Project 4.*

And that’s exactly what I did.

---

## **2.5 Weeks of Chaos and Progress**

I worked on this project intensively for about **2.5 weeks**, plus an extra week in summer of pure frontend practice.
During late October and the middle of November, I had a break between jobs and decided to dedicate that time entirely to studying and building.

Here’s how it went:

### **1. Local development**

* I built the frontend and backend separately.
* The backend originally ran in a **separate container** from the frontend.
* I used **docker-compose** with two services.
* Everything worked locally. Life was good.

### **2. The deployment disaster era**

Everything changed when I tried to deploy. My initial goals:

* One URL for both frontend & backend.
* No GitHub Pages (because it only serves static files).
* Try Azure, because we used it in another course.

What happened:

* Azure refused to deploy my container.
* Even a trial subscription with $200 credit didn’t help.
* I configured Nginx, rewrote Dockerfiles, tried multiple images…
  and still no luck.

### **3. Switching to Render**

Eventually, I moved to **Render**, which allowed me to:

* Serve both frontend & backend from one container
* Host the entire application for free
* Get automatic redeploys from GitHub
* Use a single clean Dockerfile

So I scrapped the old architecture and rebuilt the whole thing:

* One Dockerfile at the project root
* Angular production build included
* Flask backend rewritten
* Static assets moved locally
* Hosting on Render → finally stable 🎉

### **4. Adding a real database**

At the end, I upgraded the backend to use **SQLite** instead of a temporary JSON file.
Now the app has a proper relational database, satisfying the course requirements and making the project feel much more “real.”

---

## **The Debugging Marathon**

Let me be honest:
This project involved **countless debugging sessions**.

At various points:

* the container failed to boot
* the API refused to start
* CORS caused trouble
* port mismatches appeared
* frontend couldn’t find the backend
* static files broke after deployment
* images had to be moved from external URLs
* Docker misconfigurations brought the app down
* Render logs became my daily reading

If I had to guess:

* **hundreds** of rebuilds
* **dozens** of redeploys
* and countless attempts before everything worked

But every failure taught me something.

---

## **Why This Project Matters To Me**

This isn’t the most advanced microservice architecture in the world.
It’s not meant to be.

For me, this project was about:

* practicing the full development cycle
* understanding how modern apps are actually deployed
* learning Docker, Angular, Flask, and cloud hosting
* making mistakes and fixing them
* preparing for **Project 4**, where I *will* build a more complex multi-service system

This was my “pre-season training,” so to speak.
A warm-up, but one that pushed me to the limits of what I knew at the time.

And I’m genuinely proud I finished it.

---

## **The Role of AI in This Project**

I didn’t do this alone. AI tools—especially ChatGPT and GitHub Copilot—helped me:

* read and interpret cryptic Render and Docker logs
* fix backend and frontend integration issues
* rewrite broken code
* diagnose problems with ports, CORS, or routing
* understand better how Angular and Flask should interact
* find stable Dockerfile configurations

For a beginner developer like me, AI made the development process **faster, clearer, and much less overwhelming**.

It didn’t build the project for me, but it helped me build it better.

---

## **Looking Ahead**

This project marks the end of one phase of my learning and the beginning of another.

Now that I’ve experienced the struggles and victories of a real full-stack deployment, I feel far more confident approaching **Project 4**, where I plan to:

* implement more microservices
* possibly add authentication
* use a cloud database
* improve the overall system architecture

But most importantly:

I’ll walk into it knowing what it feels like to struggle, fix, learn, and finish.

---