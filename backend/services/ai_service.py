from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
from typing import Dict, List
import asyncio


class AIService:
    def __init__(self):
        self.resume_model = None
        self.resume_tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
    async def load_models(self):
        await asyncio.to_thread(self._load_models_sync)
    
    def _load_models_sync(self):
        model_name = "mistralai/Mistral-7B-Instruct-v0.3"
        self.resume_tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.resume_model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.bfloat16 if self.device == "cuda" else torch.float32,
            device_map="auto"
        )
    
    async def generate_resume(self, job_description: str, user_profile: Dict, format_type: str = "federal") -> str:
        prompt = self._create_resume_prompt(job_description, user_profile, format_type)
        resume = await asyncio.to_thread(self._generate_text, prompt, max_length=2048)
        return resume
    
    async def generate_cover_letter(self, job_description: str, user_profile: Dict, company_name: str) -> str:
        prompt = self._create_cover_letter_prompt(job_description, user_profile, company_name)
        cover_letter = await asyncio.to_thread(self._generate_text, prompt, max_length=1024)
        return cover_letter
    
    async def generate_exam_questions(self, exam_type: str, topic: str, difficulty: str, num_questions: int) -> List[Dict]:
        prompt = f"""Generate {num_questions} multiple choice questions for {exam_type} exam on topic: {topic}
Difficulty: {difficulty}
Format each question as:
Q: [question]
A) [option]
B) [option]
C) [option]
D) [option]
Correct: [letter]
Explanation: [brief explanation]"""
        
        result = await asyncio.to_thread(self._generate_text, prompt, max_length=2048)
        questions = self._parse_questions(result)
        return questions
    
    async def generate_interview_questions(self, job_category: str) -> List[Dict]:
        prompt = f"""Generate 10 common interview questions for {job_category} government positions.
Include behavioral, technical, and situational questions with sample STAR method answers."""
        
        result = await asyncio.to_thread(self._generate_text, prompt, max_length=2048)
        questions = self._parse_interview_questions(result)
        return questions
    
    async def analyze_skill_match(self, user_id: int, job_id: int) -> Dict:
        return {
            "match_score": 0.85,
            "matching_skills": ["Python", "Data Analysis", "Project Management"],
            "missing_skills": ["Cloud Computing", "Machine Learning"],
            "recommendations": [
                {"skill": "Cloud Computing", "resources": ["AWS Certification", "Azure Fundamentals"]},
                {"skill": "Machine Learning", "resources": ["Coursera ML Course", "FastAI"]}
            ]
        }
    
    def _generate_text(self, prompt: str, max_length: int = 1024) -> str:
        inputs = self.resume_tokenizer(prompt, return_tensors="pt").to(self.device)
        
        outputs = self.resume_model.generate(
            inputs.input_ids,
            max_new_tokens=max_length,
            temperature=0.7,
            do_sample=True,
            top_p=0.95
        )
        
        result = self.resume_tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result.replace(prompt, "").strip()
    
    def _create_resume_prompt(self, job_description: str, user_profile: Dict, format_type: str) -> str:
        return f"""Create a professional {format_type} format resume for the following job:

Job Description:
{job_description}

Candidate Profile:
Education: {user_profile.get('education', [])}
Experience: {user_profile.get('experience', [])}
Skills: {user_profile.get('skills', [])}

Generate a keyword-optimized, 2-page resume following federal resume guidelines with quantified achievements."""
    
    def _create_cover_letter_prompt(self, job_description: str, user_profile: Dict, company_name: str) -> str:
        return f"""Write a compelling cover letter for {company_name} for the following position:

Job Description:
{job_description}

Candidate Background:
{user_profile.get('experience', [])}

Use STAR method to highlight relevant achievements. Keep it under 400 words."""
    
    def _parse_questions(self, text: str) -> List[Dict]:
        questions = []
        lines = text.split('\n')
        current_q = {}
        
        for line in lines:
            if line.startswith('Q:'):
                if current_q:
                    questions.append(current_q)
                current_q = {'question': line[2:].strip(), 'options': []}
            elif line.startswith(('A)', 'B)', 'C)', 'D)')):
                current_q['options'].append(line.strip())
            elif line.startswith('Correct:'):
                current_q['correct'] = line[8:].strip()
            elif line.startswith('Explanation:'):
                current_q['explanation'] = line[12:].strip()
        
        if current_q:
            questions.append(current_q)
        
        return questions[:10]
    
    def _parse_interview_questions(self, text: str) -> List[Dict]:
        questions = []
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            if line.strip() and not line.startswith(('Answer:', 'Sample:')):
                questions.append({
                    'question': line.strip(),
                    'type': 'behavioral',
                    'tips': 'Use STAR method in your response'
                })
        
        return questions[:10]
