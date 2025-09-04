"""
Groundedness evaluation utilities
Provides rule-based and semantic groundedness checking for RAG systems
"""

from typing import List, Dict, Tuple
import numpy as np
import re
import jieba
from sentence_transformers import SentenceTransformer

class GroundednessEvaluator:
    """Combined rule-based and semantic groundedness evaluation"""
    
    def __init__(self, rule_weight=0.4, semantic_weight=0.6, threshold=0.6):
        self.rule_weight = rule_weight
        self.semantic_weight = semantic_weight
        self.threshold = threshold
        
    def evaluate(self, answer: str, sources: List[str]) -> Dict:
        """Main evaluation interface"""
        # Implementation details...
        pass

def jaccard_similarity(tokens_a: List[str], tokens_b: List[str]) -> float:
    """Calculate Jaccard similarity between token sets"""
    set_a, set_b = set(tokens_a), set(tokens_b)
    if not set_a and not set_b:
        return 1.0
    if not set_a or not set_b:
        return 0.0
    return len(set_a & set_b) / len(set_a | set_b)
