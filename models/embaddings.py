import os 
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import numpy as np 
from sentence_transformers import SentenceTransformer
from torch import embedding
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

HF_ACCESS  = os.getenv('HF_ACCESS')
model = SentenceTransformer('ai-forever/ru-en-RoSBERTa')


client = InferenceClient(token=HF_ACCESS)
response = client.feature_extraction(
    text="ёпа",
    model="ai-forever/ru-en-RoSBERTa"
)

embedding = model.encode('привет я николя')

print(cosine_similarity(embedding))