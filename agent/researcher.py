import google.generativeai as genai
from config import GOOGLE_API_KEY
import json
import random
import time
from tenacity import retry, stop_after_attempt, wait_exponential

class Researcher:
    def __init__(self):
        if GOOGLE_API_KEY:
            genai.configure(api_key=GOOGLE_API_KEY)
            self.model = genai.GenerativeModel('gemini-2.0-flash-lite-001')
        else:
            self.model = None

    @retry(wait=wait_exponential(multiplier=1, min=4, max=60), stop=stop_after_attempt(5))
    def verify_topic(self, topic_data):
        print(f"🔬 Researcher: Verifying '{topic_data['topic']}'...")
        
        if not self.model:
            raise ValueError("Google API Key not configured")

        # Real verification using Gemini
        prompt = f"""
        Verify this potential 'Unsolved AI Problem':
        Topic: {topic_data['topic']}
        Statement: {topic_data.get('problem_statement', '')}
        
        Task:
        1. Is this truly unsolvable/unsolved as of 2024/2025? (Yes/No)
        2. Estimate Total Addressable Market (TAM) if solved (e.g., $100B).
        3. Who are the leading labs working on this?
        4. Rate technical complexity (1-10).
        
        Output JSON:
        {{
            "is_novel": boolean,
            "tam_estimate": "string (e.g. $50B)",
            "leading_labs": ["Lab1", "Lab2"],
            "complexity_score": int
        }}
        """
        
        try:
            response = self.model.generate_content(prompt)
            text = response.text.replace("```json", "").replace("```", "").strip()
            verification_data = json.loads(text)
            
            # Merge with original data
            report = {
                "topic": topic_data['topic'],
                "problem_statement": topic_data.get('problem_statement'),
                "source": topic_data['source'],
                "importance_justification": topic_data.get('importance_justification'),
                "importance_score": topic_data.get('importance_score'),
                "verification": verification_data,
                "date": topic_data.get("date") # Preserve if exists
            }
            return report
            
        except Exception as e:
            print(f"Error in verification: {e}")
            raise e

import time

def run_research_campaign(candidates):
    researcher = Researcher()
    verified_reports = []
    
    for candidate in candidates:
        report = researcher.verify_topic(candidate)
        verified_reports.append(report)
        time.sleep(2) # Rate limit protection
        
    return verified_reports
