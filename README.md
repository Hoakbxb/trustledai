# TrustLed AI Website — Flask Project (v2)

## Pages

| Route | Page | Content |
|-------|------|---------|
| `/` | Homepage | Hero, philosophy, newsletter, services, audience, team, CTA |
| `/ai-agent-services` | AI Agent Services | Full service detail, 5-step process, pricing (4 tiers) |
| `/academy` | Academy | Bootcamp (3 tracks, 8 weeks), business workshop, career outcomes, instructors, FAQ |
| `/pricing` | Pricing | All pricing across all services in one place |
| `/about` | About | Philosophy, story, team bios, values |
| `/contact` | Contact | Contact form, email, common enquiries guide |

## Run Locally

```bash
pip install -r requirements.txt
python app.py
# Open http://localhost:5000
```

## Deploy

```bash
# Render / Railway / Fly.io
gunicorn app:app --bind 0.0.0.0:$PORT

# Docker
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
```

## Structure

```
trustled-flask-v2/
├── app.py
├── requirements.txt
├── static/
│   ├── style.css
│   └── favicon.svg
└── templates/
    ├── base.html       (nav, footer, shared head)
    ├── index.html      (homepage)
    ├── agents.html     (AI agent services)
    ├── academy.html    (academy)
    ├── pricing.html    (all pricing)
    ├── about.html      (about/team)
    └── contact.html    (contact form)
```
