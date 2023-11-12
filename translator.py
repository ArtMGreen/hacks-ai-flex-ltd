from transformers import MarianTokenizer, MarianMTModel
import torch


def ru_en():
    tokenizer = MarianTokenizer.from_pretrained("tokenizers/opus-mt-ru-en")
    model = MarianMTModel.from_pretrained("models/opus-mt-ru-en")
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # model.to(device)
    return tokenizer, model


def en_ru():
    tokenizer = MarianTokenizer.from_pretrained("tokenizers/opus-mt-en-ru")
    model = MarianMTModel.from_pretrained("models/opus-mt-en-ru")
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # model.to(device)
    return tokenizer, model


def translate(input_text, tokenizer, model):
    batch = tokenizer([input_text], return_tensors="pt")
    generated_ids = model.generate(**batch)
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
