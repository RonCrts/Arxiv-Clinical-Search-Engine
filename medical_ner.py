import random
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
import pandas as pd
from matplotlib.colors import rgb2hex

class MedicalNER:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("medical-ner-proj/bert-medical-ner-proj")
        self.model = AutoModelForTokenClassification.from_pretrained("medical-ner-proj/bert-medical-ner-proj")
        self.labels = self.model.config.id2label
        self.entity_colors = {}

    def predict(self, sequence):
        tokens = self.tokenizer.tokenize(self.tokenizer.decode(self.tokenizer.encode(sequence)))
        inputs = self.tokenizer.encode(sequence, return_tensors="pt")
        outputs = self.model(inputs)[0]
        predictions = torch.argmax(outputs, dim=2)

        entities = []
        for token, prediction in zip(tokens, predictions[0].detach().numpy()):
            entity = self.labels[prediction]
            if entity != "O":
                if entity not in self.entity_colors:
                    self.entity_colors[entity] = rgb2hex((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
                entities.append((token, entity, self.entity_colors[entity]))

        df = pd.DataFrame(entities, columns=['Token', 'Entity', 'Color'])
        return df

        
