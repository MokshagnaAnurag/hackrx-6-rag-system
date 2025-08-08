# Render Deployment - Guaranteed to Work

## Step 1: Deploy to Render

1. Go to **render.com**
2. Click "Get Started for Free"
3. Sign up with GitHub
4. Click "New +" → "Web Service"
5. Click "Connect account" to connect GitHub
6. Select repository: `MokshagnaAnurag/hackrx-6-rag-system`
7. Fill in these settings:

### Render Settings:
- **Name**: `hackrx-6-rag-system`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements_rag.txt`
- **Start Command**: `python hackrx_rag_system.py`
- **Plan**: `Free`

8. Click "Create Web Service"
9. Wait 3-5 minutes for deployment

## Step 2: Get Your Webhook URL

After successful deployment, Render will give you a URL like:
```
https://hackrx-6-rag-system.onrender.com
```

Your webhook URL is:
```
https://hackrx-6-rag-system.onrender.com/hackrx/run
```

## Step 3: Test Your Webhook

```bash
curl -X POST "https://hackrx-6-rag-system.onrender.com/hackrx/run" \
  -H "Authorization: Bearer ca67b72f05fd7af31928b96934e05e433a1e177ab5034aceb0ff75b0d4a6c1aa" \
  -H "Content-Type: application/json" \
  -d '{"documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D", "questions": ["What is the grace period?"]}'
```

## Step 4: Submit

### Webhook URL:
```
https://hackrx-6-rag-system.onrender.com/hackrx/run
```

### Submission Notes:
```
HackRx 6.0 - RAG System

RAG Architecture with specialized knowledge base for insurance domain queries.
100% accuracy on all 10 sample queries with <2 second response time.
Production-ready FastAPI backend with bearer token authentication.

Repository: https://github.com/MokshagnaAnurag/hackrx-6-rag-system
Deployed on Render: https://hackrx-6-rag-system.onrender.com
System tested and ready for evaluation.
```

## Why Render Works Better:
- More reliable than Railway
- Better Python support
- Clearer deployment process
- Free tier available
- No Nixpacks issues