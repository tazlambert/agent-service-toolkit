from enum import StrEnum, auto
from typing import TypeAlias


class Provider(StrEnum):
    OPENAI = auto()
    OCI = auto()
    AZURE_OPENAI = auto()
    DEEPSEEK = auto()
    ANTHROPIC = auto()
    GOOGLE = auto()
    GROQ = auto()
    AWS = auto()
    OLLAMA = auto()
    FAKE = auto()


class OpenAIModelName(StrEnum):
    """https://platform.openai.com/docs/models/gpt-4o"""

    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4O = "gpt-4o"


class OCIAIModelName(StrEnum):
    """Oracle Cloud Infrastructure AI model names"""

    OCI_LLAMA_33 = "meta.llama-3.3-70b-instruct"
    OCI_LLAMA_31 = "meta.llama-3.1-405b-instruct"
    OCI_COHERE_R = "cohere.command-r-08-2024"
    OCI_COHERE_RPLUS = "cohere.command-r-plus-08-2024"


class AzureOpenAIModelName(StrEnum):
    """Azure OpenAI model names"""

    AZURE_GPT_4O = "azure-gpt-4o"
    AZURE_GPT_4O_MINI = "azure-gpt-4o-mini"


class DeepseekModelName(StrEnum):
    """https://api-docs.deepseek.com/quick_start/pricing"""

    DEEPSEEK_CHAT = "deepseek-chat"


class AnthropicModelName(StrEnum):
    """https://docs.anthropic.com/en/docs/about-claude/models#model-names"""

    HAIKU_3 = "claude-3-haiku"
    HAIKU_35 = "claude-3.5-haiku"
    SONNET_35 = "claude-3.5-sonnet"


class GoogleModelName(StrEnum):
    """https://ai.google.dev/gemini-api/docs/models/gemini"""

    GEMINI_15_FLASH = "gemini-1.5-flash"


class GroqModelName(StrEnum):
    """https://console.groq.com/docs/models"""

    LLAMA_31_8B = "groq-llama-3.1-8b"
    LLAMA_33_70B = "groq-llama-3.3-70b"

    LLAMA_GUARD_3_8B = "groq-llama-guard-3-8b"


class AWSModelName(StrEnum):
    """https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html"""

    BEDROCK_HAIKU = "bedrock-3.5-haiku"


class OllamaModelName(StrEnum):
    """https://ollama.com/search"""

    OLLAMA_GENERIC = "ollama"


class FakeModelName(StrEnum):
    """Fake model for testing."""

    FAKE = "fake"


AllModelEnum: TypeAlias = (
    OpenAIModelName
    | OCIAIModelName
    | AzureOpenAIModelName
    | DeepseekModelName
    | AnthropicModelName
    | GoogleModelName
    | GroqModelName
    | AWSModelName
    | OllamaModelName
    | FakeModelName
)
