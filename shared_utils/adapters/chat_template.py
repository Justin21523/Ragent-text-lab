from dataclasses import dataclass
from typing import List, Dict, Optional
from opencc import OpenCC
import re


@dataclass
class Message:
    role: str
    content: str


class ChatTemplate:
    def __init__(self, model_name: str = "qwen", convert_zh: str = None):  # type: ignore
        self.model_name = model_name.lower()
        self.cc = OpenCC(convert_zh) if convert_zh else None
        # ... (copy full implementation)

    # ... (copy all methods)


class ChinesePromptEngine:
    # ... (copy implementation)
    pass


class PromptSafetyGuard:
    # ... (copy implementation)
    pass
