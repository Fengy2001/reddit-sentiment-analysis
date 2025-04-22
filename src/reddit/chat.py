import os
import transformers
import torch
print("Is CUDA available?", torch.cuda.is_available())
print("GPU name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU detected")
os.environ['TRANSFORMERS_CACHE'] = 'E:/Huggingface'

model_id = "ProsusAI/finbert"
device = "cuda" if torch.cuda.is_available() else "cpu"

pipeline = transformers.pipeline(
    task="sentiment-analysis",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device=device,
)


context_prompt = "markets are tanking."
outputs = pipeline(context_prompt)
print(outputs)
print("Program Finished.")