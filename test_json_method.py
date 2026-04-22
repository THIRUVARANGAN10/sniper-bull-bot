#!/usr/bin/env python3
"""
Test Telegram with JSON method
Different approach to bypass HTTP 400
"""

import urllib.request
import json

TOKEN = "8641975809:AAEi00c0QhsPkuFpPDmuLe7eM8iPynlOsIM"
CHAT_ID = "6408770437"

print("\n" + "="*70)
print("TELEGRAM TEST - JSON METHOD")
print("="*70 + "\n")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Use JSON instead of form data
payload = {
    "chat_id": int(CHAT_ID),
    "text": "Sniper Bull Bot Test"
}

data = json.dumps(payload).encode('utf-8')

print("Sending message with JSON...")
print(f"Chat ID: {CHAT_ID}")
print(f"Message: Sniper Bull Bot Test\n")

try:
    req = urllib.request.Request(
        url,
        data=data,
        headers={'Content-Type': 'application/json'}
    )
    
    with urllib.request.urlopen(req, timeout=10) as response:
        result = json.loads(response.read().decode('utf-8'))
        
        if result.get('ok'):
            print("✅ SUCCESS!")
            print("\nMessage delivered to Telegram!")
            print("Check your Telegram now!")
        else:
            print(f"❌ Telegram error:")
            print(f"   {result.get('description')}")
            
except urllib.error.HTTPError as e:
    print(f"❌ HTTP Error {e.code}")
    try:
        error_data = json.loads(e.read().decode('utf-8'))
        print(f"   {error_data.get('description')}")
    except:
        pass
        
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "="*70)
print("\nPress Enter to close...")
input()
