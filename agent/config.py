# config.py

# List of Thought Leaders for Research
THOUGHT_LEADERS = [
    # I. The "Big Three" & Legacy Leaders
    {"name": "Yoshua Bengio", "affiliation": "Mila/U. Montreal", "category": "Legacy Leader"},
    {"name": "Geoffrey Hinton", "affiliation": "U. of Toronto", "category": "Legacy Leader"},
    {"name": "Yann LeCun", "affiliation": "Meta", "category": "Legacy Leader"},
    {"name": "Andrew Ng", "affiliation": "Stanford/Landing AI", "category": "Legacy Leader"},
    {"name": "Fei-Fei Li", "affiliation": "Stanford/World Labs", "category": "Legacy Leader"},

    # II. Major Lab Leaders
    {"name": "Sam Altman", "affiliation": "OpenAI", "category": "Lab Leader"},
    {"name": "Demis Hassabis", "affiliation": "Google DeepMind", "category": "Lab Leader"},
    {"name": "Dario Amodei", "affiliation": "Anthropic", "category": "Lab Leader"},
    {"name": "Mark Zuckerberg", "affiliation": "Meta", "category": "Lab Leader"},
    {"name": "Elon Musk", "affiliation": "xAI", "category": "Lab Leader"},
    {"name": "Ilya Sutskever", "affiliation": "SSI", "category": "Lab Leader"},
    {"name": "Mira Murati", "affiliation": "OpenAI (ex-CTO)", "category": "Lab Leader"},
    {"name": "Mustafa Suleyman", "affiliation": "Microsoft AI", "category": "Lab Leader"},
    {"name": "Jakub Pachocki", "affiliation": "OpenAI", "category": "Lab Leader"},
    {"name": "Jared Kaplan", "affiliation": "Anthropic", "category": "Lab Leader"},

    # III. Corporate Research & AWS/Google/Meta Deep Bench
    {"name": "Swami Sivasubramanian", "affiliation": "AWS", "category": "Corporate Research"},
    {"name": "Jeff Dean", "affiliation": "Google", "category": "Corporate Research"},
    {"name": "Quoc Le", "affiliation": "Google DeepMind", "category": "Corporate Research"},
    {"name": "Oriol Vinyals", "affiliation": "Google DeepMind", "category": "Corporate Research"},
    {"name": "Joelle Pineau", "affiliation": "Meta FAIR", "category": "Corporate Research"},
    {"name": "Shane Legg", "affiliation": "Google DeepMind", "category": "Corporate Research"},
    {"name": "Bratin Saha", "affiliation": "AWS", "category": "Corporate Research"},
    {"name": "Josh Woodward", "affiliation": "Google Labs", "category": "Corporate Research"},
    {"name": "Jan Leike", "affiliation": "Anthropic", "category": "Corporate Research"},
    {"name": "Bowen Baker", "affiliation": "OpenAI", "category": "Corporate Research"},

    # IV. Open Source & Hardware Champions
    {"name": "Clement Delangue", "affiliation": "Hugging Face", "category": "Open Source"},
    {"name": "Thomas Wolf", "affiliation": "Hugging Face", "category": "Open Source"},
    {"name": "Arthur Mensch", "affiliation": "Mistral AI", "category": "Open Source"},
    {"name": "Jensen Huang", "affiliation": "Nvidia", "category": "Hardware"},
    {"name": "Tri Dao", "affiliation": "Together AI/Princeton", "category": "Open Source"},
    {"name": "Albert Gu", "affiliation": "CMU/Mamba", "category": "Open Source"},
    {"name": "Liang Wenfeng", "affiliation": "DeepSeek", "category": "Open Source"},
    {"name": "Aiden Gomez", "affiliation": "Cohere", "category": "Open Source"},

    # V. Top Cited Research Authors
    {"name": "Abhimanyu Dubey", "affiliation": "Meta", "category": "Researcher"},
    {"name": "Wei-Lin Chiang", "affiliation": "UC Berkeley/LMSYS", "category": "Researcher"},
    {"name": "Rafail Rafailov", "affiliation": "Stanford", "category": "Researcher"},
    {"name": "Khaled Saab", "affiliation": "Google DeepMind", "category": "Researcher"},
    {"name": "Haoyu Lu", "affiliation": "DeepSeek", "category": "Researcher"},

    # VI. Ethics, Critics, & New Perspectives
    {"name": "Timnit Gebru", "affiliation": "DAIR", "category": "Ethics/Critic"},
    {"name": "Margaret Mitchell", "affiliation": "Hugging Face", "category": "Ethics/Critic"},
    {"name": "Gary Marcus", "affiliation": "NYU", "category": "Ethics/Critic"},
    {"name": "Francois Chollet", "affiliation": "Google", "category": "Ethics/Critic"},
    {"name": "Percy Liang", "affiliation": "Stanford", "category": "Ethics/Critic"},
    {"name": "Eliezer Yudkowsky", "affiliation": "MIRI", "category": "Ethics/Critic"},
    {"name": "Andrej Karpathy", "affiliation": "ex-OpenAI/Tesla", "category": "Educator"},
    {"name": "Chelsea Finn", "affiliation": "Stanford/Google", "category": "Researcher"},
    {"name": "Sergey Levine", "affiliation": "UC Berkeley", "category": "Researcher"},
    {"name": "Karen Hao", "affiliation": "Journalist", "category": "Ethics/Critic"},
    {"name": "Marcelo Calbucci", "affiliation": "Veteran Tech", "category": "Ethics/Critic"},
    {"name": "Dr. Merritt Moore", "affiliation": "NYU Abu Dhabi", "category": "Creative Robotics"},

    # Investors (Notable)
    {"name": "Peter Thiel", "affiliation": "Founders Fund", "category": "Investor"},
    {"name": "Marc Andreessen", "affiliation": "a16z", "category": "Investor"},
    {"name": "Vinod Khosla", "affiliation": "Khosla Ventures", "category": "Investor"},
    {"name": "Reid Hoffman", "affiliation": "Greylock/Inflection", "category": "Investor"},
    {"name": "Nat Friedman", "affiliation": "SSI", "category": "Investor"},
    {"name": "Daniel Gross", "affiliation": "SSI", "category": "Investor"},
    {"name": "Elad Gil", "affiliation": "Independent", "category": "Investor"},
    {"name": "Naval Ravikant", "affiliation": "AngelList", "category": "Investor"},
]

# Criteria for "Unsolved Problems"
CRITERIA = {
    "thought_leader_rank": "Must be mentioned or discussed by at least one person in the list.",
    "novelty": "Problem must not have a generally accepted objective solution.",
    "tam": "Target Addressable Market (TAM) must be significant (or impact unrelated to money is massive).",
    "simplicity": "Problem complexity must be explainable in simple terms."
}

# API Keys (Environment Variables)
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY") # For web search
