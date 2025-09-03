# Third-party
from transformers import CLIPTokenizer


def get_token_count(prompt: str):
    tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14")

    return len(tokenizer(prompt).input_ids)
