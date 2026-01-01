import httpx
import asyncio
from typing import List, Dict
from datetime import datetime
from backend.core.config import settings, config


class JobScraperService:
    def __init__(self):
        self.sources = config.get('scraping', {}).get('targets', [])
    
    async def scrape_usajobs(self) -> List[Dict]:
        if not settings.USAJOBS_API_KEY:
            return []
        
        headers = {
            'Authorization-Key': settings.USAJOBS_API_KEY,
            'User-Agent': settings.USAJOBS_USER_AGENT
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    'https://data.usajobs.gov/api/search',
                    headers=headers,
                    params={'ResultsPerPage': 500}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    return self._parse_usajobs_response(data)
            except Exception as e:
                print(f"Error scraping USAJOBS: {e}")
        
        return []
    
    def _parse_usajobs_response(self, data: Dict) -> List[Dict]:
        jobs = []
        
        for item in data.get('SearchResult', {}).get('SearchResultItems', []):
            job_data = item.get('MatchedObjectDescriptor', {})
            
            jobs.append({
                'external_id': job_data.get('PositionID'),
                'source': 'USAJOBS',
                'title': job_data.get('PositionTitle'),
                'organization': job_data.get('OrganizationName'),
                'description': job_data.get('UserArea', {}).get('Details', {}).get('JobSummary'),
                'location_city': job_data.get('PositionLocationDisplay', '').split(',')[0] if job_data.get('PositionLocationDisplay') else None,
                'location_state': None,
                'location_country': 'US',
                'salary_min': job_data.get('PositionRemuneration', [{}])[0].get('MinimumRange') if job_data.get('PositionRemuneration') else None,
                'salary_max': job_data.get('PositionRemuneration', [{}])[0].get('MaximumRange') if job_data.get('PositionRemuneration') else None,
                'job_category': job_data.get('JobCategory', [{}])[0].get('Name') if job_data.get('JobCategory') else None,
                'application_url': job_data.get('PositionURI'),
                'posted_date': datetime.fromisoformat(job_data.get('PublicationStartDate').replace('Z', '+00:00')) if job_data.get('PublicationStartDate') else None,
                'closing_date': datetime.fromisoformat(job_data.get('ApplicationCloseDate').replace('Z', '+00:00')) if job_data.get('ApplicationCloseDate') else None,
            })
        
        return jobs
    
    async def scrape_all_sources(self) -> List[Dict]:
        all_jobs = []
        
        for source in self.sources:
            if not source.get('enabled'):
                continue
            
            if source['name'] == 'USAJOBS':
                jobs = await self.scrape_usajobs()
                all_jobs.extend(jobs)
            
            await asyncio.sleep(source.get('rate_limit', 1))
        
        return all_jobs
