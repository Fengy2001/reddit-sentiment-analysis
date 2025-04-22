from transformers import AutoModel, AutoTokenizer
import os 
os.environ['TRANSFORMERS_CACHE'] = 'E:/Huggingface'
model_name = "ProsusAI/finbert"  # Replace with the model you want
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save the model locally
model.save_pretrained("E:/Huggingface/finbert")
tokenizer.save_pretrained("E:/Huggingface/finbert")