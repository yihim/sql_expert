from unsloth import FastLanguageModel
from constants.models import LOAD_IN_4BIT, MAX_SEQ_LENGTH, DTYPE, SYSTEM_PROMPT
from transformers import TextStreamer
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

if __name__ == "__main__":
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name="./notebooks/unsloth-qwen2.5-7b-instruct-text-to-sql-v1",
        load_in_4bit=LOAD_IN_4BIT,
        max_seq_length=MAX_SEQ_LENGTH,
        dtype=DTYPE
    )
    FastLanguageModel.for_inference(model)

    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    model.generation_config.pad_token_id = tokenizer.pad_token_id

    text_streamer = TextStreamer(skip_prompt=True, tokenizer=tokenizer, skip_special_tokens=True)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": """sql_context: CREATE TABLE dapp_ranking (dapp_id INT, dapp_name VARCHAR(50), dapp_category VARCHAR(30), dapp_rating DECIMAL(3,2), dapp_downloads INT, dapp_region VARCHAR(30)); INSERT INTO dapp_ranking (dapp_id, dapp_name, dapp_category, dapp_rating, dapp_downloads, dapp_region) VALUES (1, 'AsiaPacificDapp', 'Social', 4.3, 2000000, 'Asia-Pacific');
        
        sql_prompt: How many decentralized applications have been downloaded from the 'Asia-Pacific' region?
        """}
    ]

    applied_template = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    input_ids = tokenizer([applied_template], return_tensors="pt").to(device)

    _ = model.generate(**input_ids, streamer=text_streamer, max_new_tokens=1024, pad_token_id=tokenizer.eos_token_id)