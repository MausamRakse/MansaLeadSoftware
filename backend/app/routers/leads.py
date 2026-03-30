import re
import logging
from fastapi import APIRouter
from app.schemas.lead import LeadRequest, AISearchRequest
from app.services.apollo import fetch_apollo_leads

logger = logging.getLogger(__name__)
router = APIRouter(tags=["leads"])


@router.post("/api/leads")
async def get_leads(req: LeadRequest):
    return await fetch_apollo_leads(req.model_dump())


@router.post("/api/ai-search")
async def ai_search(req: AISearchRequest):
    prompt = req.prompt.lower()

    job_titles: list[str] = []
    if "founder"   in prompt: job_titles.append("Founder")
    if "ceo"       in prompt: job_titles.append("CEO")
    if "cto"       in prompt: job_titles.append("CTO")
    if "marketing" in prompt: job_titles.append("Marketing Manager")
    if "product"   in prompt: job_titles.append("Product Manager")

    industry = ""
    if "ai" in prompt or "artificial intelligence" in prompt: industry = "Artificial Intelligence"
    elif "fintech"    in prompt: industry = "FinTech"
    elif "healthcare" in prompt: industry = "Healthcare"
    elif "saas"       in prompt: industry = "SaaS"
    elif "e-commerce" in prompt or "ecommerce" in prompt: industry = "E-Commerce"

    size_match = re.search(r"(\d+)[^\d]*(\d+)", prompt)
    min_s, max_s = (int(size_match.group(1)), int(size_match.group(2))) if size_match else (1, 200)

    filters = {
        "job_titles":       job_titles or ["Founder", "CEO"],
        "industry":         industry,
        "company_size_min": min_s,
        "company_size_max": max_s,
        "page":             1,
    }

    result = await fetch_apollo_leads(filters)
    return {**result, "filters_used": filters}
