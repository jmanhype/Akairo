# Akairo

DSPy-based optimizer for LLM responses. Supports local models via Ollama and cloud models via OpenAI.

## Architecture

| Path | Purpose |
|---|---|
| `src/dspy_local_optimizer/core/models.py` | Data models |
| `src/dspy_local_optimizer/core/metrics.py` | Quality scoring |
| `src/dspy_local_optimizer/core/ollama.py` | Ollama client |
| `src/dspy_local_optimizer/core/openai.py` | OpenAI client |
| `src/dspy_local_optimizer/optimizers/guideline_optimizer.py` | Guideline optimization logic |
| `scripts/run_optimization.py` | CLI entry point |
| `tests/test_copro_optimizer.py` | 1 test file |

## Requirements

- Python 3.10+ with Poetry
- Ollama (for local models) or an OpenAI API key

## Setup

```bash
git clone https://github.com/jmanhype/Akairo.git
cd Akairo
poetry install

# For local models:
ollama pull llama2
```

## Usage

```python
from dspy_local_optimizer import BatchOptimizedGuidelineManager

optimizer = BatchOptimizedGuidelineManager(
    model_name="ollama/llama2",  # or "openai/gpt-3.5-turbo"
    use_optimizer=True
)

optimized = optimizer.optimize_guidelines(
    guidelines=your_guidelines,
    examples=training_data,
    batch_size=5
)
```

Or via the script:

```bash
poetry run python scripts/run_optimization.py
```

## Tests

```bash
poetry run pytest
```

1 test file.

## Status

Small utility project. The optimization loop runs but there are no published benchmarks showing improvement over baseline. The codebase is ~6 source files.

## License

MIT
