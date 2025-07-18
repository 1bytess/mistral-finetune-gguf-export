from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import os
import torch
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str)
    parser.add_argument("--lora", type=str)
    parser.add_argument("--out_dir", type=str, default="./model") # leave this
    args = parser.parse_args()

    print(f"Loading base model: {args.model}")
    base_model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=torch.float16, device_map="auto")

    print(f"Loading PEFT: {args.lora}")
    model = PeftModel.from_pretrained(base_model, args.lora)
    print(f"Running merge_and_unload")
    model = model.merge_and_unload()
    tokenizer = AutoTokenizer.from_pretrained(args.model)

    model.save_pretrained(f"{args.out_dir}")
    tokenizer.save_pretrained(f"{args.out_dir}")
    print(f"Model saved to {args.out_dir}")

if __name__ == "__main__" :
    main()
