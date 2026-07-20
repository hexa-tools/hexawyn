LLM_PROVIDERS: dict[str, dict[str, str]] = {
    "1": {
        "name": "DeepSeek",
        "base_url": "https://api.deepseek.com",
        "env_key": "DEEPSEEK_API_KEY",
    },
    "2": {"name": "OpenAI", "base_url": "https://api.openai.com/v1", "env_key": "OPENAI_API_KEY"},
    "3": {"name": "Groq", "base_url": "https://api.groq.com/openai/v1", "env_key": "GROQ_API_KEY"},
    "4": {
        "name": "Together AI",
        "base_url": "https://api.together.xyz/v1",
        "env_key": "TOGETHER_API_KEY",
    },
    "5": {"name": "Mistral", "base_url": "https://api.mistral.ai/v1", "env_key": "MISTRAL_API_KEY"},
    "6": {
        "name": "Google (Gemini)",
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
        "env_key": "GEMINI_API_KEY",
    },
    "7": {
        "name": "OpenRouter",
        "base_url": "https://openrouter.ai/api/v1",
        "env_key": "OPENROUTER_API_KEY",
    },
    "8": {"name": "xAI (Grok)", "base_url": "https://api.x.ai/v1", "env_key": "XAI_API_KEY"},
    "0": {"name": "Custom", "base_url": "", "env_key": "LLM_API_KEY"},
}
