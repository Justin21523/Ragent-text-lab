"""BGE-M3 嵌入模型封裝模組"""

from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Optional
import pathlib
import os


class BGEEmbedder:
    def __init__(self, model_name="BAAI/bge-m3", normalize=True, max_seq_length=512):
        self.model = SentenceTransformer(model_name)
        self.normalize = normalize
        self.max_seq_length = max_seq_length

    def encode_batch(self, texts: List[str], batch_size: int = 32) -> np.ndarray:
        return self.model.encode(
            texts,
            batch_size=batch_size,
            normalize_embeddings=self.normalize,
            convert_to_numpy=True,
        )
