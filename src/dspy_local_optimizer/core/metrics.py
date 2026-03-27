"""Metrics tracking for model performance."""

from dataclasses import dataclass


@dataclass
class ModelMetrics:
    """Metrics for tracking model performance.

    Attributes:
        total_api_calls: Total number of API calls made
        total_tokens: Total number of tokens used
        total_time: Total time spent in seconds
    """

    total_api_calls: int = 0
    total_tokens: int = 0
    total_time: float = 0.0
