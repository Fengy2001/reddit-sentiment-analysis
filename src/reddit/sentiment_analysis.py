import os, torch, transformers
from transformers import BertTokenizer, BertForSequenceClassification

class sentiment_analysis:
    def __init__(self):
        os.environ['TRANSFORMERS_CACHE'] = 'E:/Huggingface'
        self.model = None
        self.model_name = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
        self.tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
        if torch.cuda.is_available():
            self.device = "cuda"
        else:
            self.device = "cpu"
        self.init_model()
    
    def init_model(self):
        self.model = transformers.pipeline(
            task="sentiment-analysis",
            model=self.model_name,
            tokenizer=self.tokenizer,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device=self.device,
        )

    def analyze(self, comment):
        if (len(self.tokenizer.encode(comment)) > 512):
            return "Comment needs to be chunked."
        sentiment = self.model(comment)[0]["label"]
        if (sentiment.lower() == "negative"):
            return -1
        elif (sentiment.lower() == "neutral"):
            return 0
        elif (sentiment.lower() == "positive"):
            return 1
        return None
