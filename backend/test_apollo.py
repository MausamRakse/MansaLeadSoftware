import httpx
import json
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("APOLLO_API_KEY")

async def test_payload(client, url, headers, payload, name):
    print(f"\nTesting {name}...")
    r = await client.post(url, headers=headers, json=payload, timeout=10.0)
    print(f"Status: {r.status_code}, Response: {r.text[:200]}")

async def main():
    async with httpx.AsyncClient() as client:
        url = "https://api.apollo.io/v1/mixed_people/api_search"
        headers = {
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "X-Api-Key": api_key
        }
        
        await test_payload(client, url, headers, {"page": 1, "per_page": 1, "person_titles": ["CEO"]}, "person_titles")
        await test_payload(client, url, headers, {"page": 1, "per_page": 1, "person_locations": ["United States"]}, "person_locations")
        await test_payload(client, url, headers, {"page": 1, "per_page": 1, "organization_num_employees_ranges": ["1,100"]}, "company_size")
        await test_payload(client, url, headers, {"page": 1, "per_page": 1, "q_organization_keyword_tags": ["AI"]}, "keywords")

asyncio.run(main())
