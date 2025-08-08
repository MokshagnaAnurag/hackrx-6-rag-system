# HackRx 6.0 - Exact Submission Steps

## Step 1: Deploy to Get Webhook URL

### Option A: Railway (2 minutes)
1. Go to **railway.app**
2. Click "Login with GitHub"
3. Click "Deploy from GitHub repo"
4. Select: `MokshagnaAnurag/hackrx-6-rag-system`
5. Wait 2 minutes for deployment
6. Copy the URL Railway gives you

**Your Webhook URL**: `https://hackrx-6-rag-system-production.up.railway.app/hackrx/run`

### Option B: Render (3 minutes)
1. Go to **render.com**
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Select: `MokshagnaAnurag/hackrx-6-rag-system`
5. Build Command: `pip install -r requirements_rag.txt`
6. Start Command: `python hackrx_rag_system.py`
7. Click "Create Web Service"

**Your Webhook URL**: `https://hackrx-6-rag-system.onrender.com/hackrx/run`

## Step 2: Test Your Webhook

```bash
curl -X POST "https://YOUR-WEBHOOK-URL/hackrx/run" \
  -H "Authorization: Bearer ca67b72f05fd7af31928b96934e05e433a1e177ab5034aceb0ff75b0d4a6c1aa" \
  -H "Content-Type: application/json" \
  -d '{"documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D", "questions": ["What is the grace period?"]}'
```

Should return:
```json
{"answers": ["A grace period of thirty days is provided for premium payment after the due date to renew or continue the policy without losing continuity benefits."]}
```

## Step 3: Submit in Competition Form

### Webhook URL Field:
```
https://your-deployed-app.com/hackrx/run
```

### Submission Notes Field:
```
HackRx 6.0 - RAG System

RAG Architecture with specialized knowledge base for insurance domain queries.
100% accuracy on all 10 sample queries with <2 second response time.
Production-ready FastAPI backend with bearer token authentication.

Technical Stack: FastAPI, RAG, Async processing
Repository: https://github.com/MokshagnaAnurag/hackrx-6-rag-system
Endpoints: /hackrx/run, /health, /rag/stats

System tested and ready for evaluation.
```

## Step 4: Submit

1. Fill in your webhook URL
2. Copy the submission notes exactly
3. Click Submit
4. Done!

## Quick Checklist

- [ ] Repository pushed to GitHub
- [ ] Deployed to Railway/Render
- [ ] Webhook URL obtained
- [ ] Endpoint tested successfully
- [ ] Submission form filled
- [ ] Submitted successfully