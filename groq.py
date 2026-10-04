import config
from openai import OpenAI
GROQ_URL="https://api.groq.com/openai/v1"
MODELS=getattr(config,"GROQ_MODELS",["llama-3.1-8b-instant","mixtral-8x7b-32768","openai/gpt-oss-120b","openai/gpt-oss-20b"])
def generate_response(prompt:str,temperature:float=0.3,max_tokens: int = 512)->str:
    key=getattr(config,"GROQ_API_KEY",None)
    if not key:
        return "ERROR: GROQ_API_KEY not set in config.py"
    c=OpenAI(api_key=key,base_url=GROQ_URL)
    last_err=None
    for m in MODELS:
        try:
            r=c.chat.completions.create(
                model=m,
                messages=[{"role":"user","content":prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return r.choices[0].message.content
        except Exception as e:
            last_err=e
    return(
        "GROQ model failed.\n"
        f"Tried models: {MODELS}\n"
        "Fix.\n"
        "1)Switch to hf by importing hf.py instead of groq.py\n"
        "2)Replace the Groq models in groq.py"
        f"Details:{type(last_err).__name__}:{last_err}"
    )
