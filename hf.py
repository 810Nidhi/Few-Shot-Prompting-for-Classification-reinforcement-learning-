import config
from huggingface_hub import InferenceClient
MODELS=getattr(config,"HF_MODELS",["openai/gpt-oss-120b","deepseek-ai/DeepSeek-V3","MiniMaxAI/MiniMax-M1-80k","Qwen/Qwen2.5-7B-Instruct","meta-llama/Llama-3.1-8B"])
def generate_response(prompt:str,temperature:float=0.3,max_tokens: int = 512)->str:
    key=getattr(config,"HF_API_KEY",None)
    if not key:
        return "ERROR: HF_API_KEY not set in config.py"
    last_err=None
    for m in MODELS:
        try:
            c=InferenceClient(model=m,token=key)
            r=c.chat_completion(
                messages=[{"role":"user","content":prompt}],
                temperature=temperature,
                max_new_tokens=max_tokens
            )
            return r.choices[0].message.content
        except Exception as e:
            last_err=e
    return(
        "HF model failed.\n"
        f"Tried models: {MODELS}\n"
        "Fix.\n"
        "1)Switch to groq by importing groq.py instead of hf.py\n"
        "2)Replace the HF models in hf.py"
        f"Details:{type(last_err).__name__}:{last_err}"
    )
