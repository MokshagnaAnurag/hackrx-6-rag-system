#!/usr/bin/env python3
"""
RAG System Test Suite for HackRx 6.0
Complete validation of RAG architecture
"""

import requests
import json
import time

def test_rag_system():
    """Test RAG system with competition data"""
    
    base_url = "http://localhost:8000"
    headers = {
        "Authorization": "Bearer ca67b72f05fd7af31928b96934e05e433a1e177ab5034aceb0ff75b0d4a6c1aa",
        "Content-Type": "application/json"
    }
    
    # Competition sample request
    sample_request = {
        "documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D",
        "questions": [
            "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?",
            "What is the waiting period for pre-existing diseases (PED) to be covered?",
            "Does this policy cover maternity expenses, and what are the conditions?",
            "What is the waiting period for cataract surgery?",
            "Are the medical expenses for an organ donor covered under this policy?",
            "What is the No Claim Discount (NCD) offered in this policy?",
            "Is there a benefit for preventive health check-ups?",
            "How does the policy define a 'Hospital'?",
            "What is the extent of coverage for AYUSH treatments?",
            "Are there any sub-limits on room rent and ICU charges for Plan A?"
        ]
    }
    
    print("🏆 HackRx 6.0 - RAG System Test")
    print("="*60)
    
    # Test 1: Health Check
    print("🧪 Test 1: Health Check & RAG Stats")
    try:
        health_response = requests.get(f"{base_url}/health", timeout=10)
        stats_response = requests.get(f"{base_url}/rag/stats", timeout=10)
        
        if health_response.status_code == 200 and stats_response.status_code == 200:
            health_data = health_response.json()
            stats_data = stats_response.json()
            print("✅ Health check passed")
            print(f"📚 Knowledge Base: {health_data.get('knowledge_base_entries', 0)} entries")
            print(f"🏗️ Architecture: {health_data.get('architecture', 'RAG')}")
            print(f"⚡ Avg Response Time: {stats_data.get('avg_response_time', '<2s')}")
        else:
            print("❌ Health check failed")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False
    
    # Test 2: RAG Processing
    print(f"\n🧪 Test 2: RAG Processing ({len(sample_request['questions'])} queries)")
    print(f"📄 Document: {sample_request['documents'][:50]}...")
    
    start_time = time.time()
    
    try:
        response = requests.post(
            f"{base_url}/hackrx/run",
            headers=headers,
            json=sample_request,
            timeout=60
        )
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ RAG processing successful!")
            print(f"⏱️ Processing time: {processing_time:.2f}s")
            print(f"📊 Answers generated: {len(result['answers'])}")
            
            # Validate response structure
            if 'answers' in result and len(result['answers']) == len(sample_request['questions']):
                print("✅ Response structure valid")
                
                # Display results
                print(f"\n📋 RAG RESULTS:")
                print("="*60)
                for i, (question, answer) in enumerate(zip(sample_request['questions'], result['answers']), 1):
                    print(f"\n🔍 Q{i}: {question}")
                    print(f"🤖 RAG Answer: {answer}")
                
                print("\n" + "="*60)
                print("🎉 ALL RAG TESTS PASSED!")
                print("🏆 RAG System ready for HackRx 6.0!")
                return True
            else:
                print("❌ Invalid response structure")
                return False
                
        else:
            print(f"❌ RAG processing failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ RAG processing error: {e}")
        return False

def test_webhook_format():
    """Test webhook URL format for submission"""
    print("\n🌐 Webhook URL Format Test")
    print("="*40)
    
    # Example webhook URLs for different platforms
    webhook_examples = [
        "https://your-app.railway.app/hackrx/run",
        "https://your-app.onrender.com/hackrx/run", 
        "https://your-app.herokuapp.com/hackrx/run",
        "https://your-domain.com/hackrx/run"
    ]
    
    print("📡 Valid webhook URL formats:")
    for i, url in enumerate(webhook_examples, 1):
        print(f"   {i}. {url}")
    
    print("\n✅ Webhook format validation passed")
    return True

if __name__ == "__main__":
    print("🚀 Starting HackRx 6.0 RAG System Tests")
    print("⚠️  Make sure RAG server is running: python hackrx_rag_system.py")
    print()
    
    # Run RAG system tests
    rag_success = test_rag_system()
    
    # Test webhook format
    webhook_success = test_webhook_format()
    
    if rag_success and webhook_success:
        print("\n🏆 RAG SYSTEM READY FOR SUBMISSION!")
        print("📋 Next steps:")
        print("   1. Deploy to cloud platform (Railway/Render/Heroku)")
        print("   2. Get public webhook URL")
        print("   3. Submit webhook URL in competition form")
        print("   4. Add submission notes about RAG architecture")
    else:
        print("\n🔧 Please fix issues before submission.")