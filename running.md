# Running the SBP tests with your own LLM

`sbp.py` is a single file. It needs **Python 3.10+** and nothing else: no `pip install`.

```
git clone https://github.com/YasirFarooq76/Shakeela-Begum-Protocol-SBP-.git
cd Shakeela-Begum-Protocol-SBP-
python sbp.py "Explain quantum computing simply."
```

That first command is offline. It only rewrites your prompt with fixed templates; no model is called.

## 1. Check the plumbing for free

```
python sbp.py bench --provider mock --judge
python -m unittest discover -v
```

The mock model returns placeholder text. Its scores mean nothing; this only proves the harness works.

## 2. Use a real model

The benchmark runs the README's three conditions (CoT only, SBP -> CoT, CoT -> SBP) on one question.
One run makes 7 model calls, or 10 with `--judge`. Results are saved in `sbp_runs/`.

**Anthropic**
```
export ANTHROPIC_API_KEY=...            # never pass keys as command-line arguments
python sbp.py bench --provider anthropic --judge
```
The default model is `claude-sonnet-5`. The README's results came from Claude Sonnet 4.6, so to match
that setup add `--model claude-sonnet-4-6`.

**A local model with Ollama** (no key, nothing leaves your machine)
```
python sbp.py bench --provider openai-compatible \
    --base-url http://localhost:11434/v1 --model <a model you have pulled> --judge
```

**OpenAI**
```
export SBP_API_KEY=...
python sbp.py bench --provider openai-compatible \
    --base-url https://api.openai.com/v1 --model <model name> \
    --token-param max_completion_tokens
```
Newer OpenAI models reject `max_tokens`; if you see an error mentioning it, use `--token-param
max_completion_tokens` (or `none`). Older models and most local servers want the default, `max_tokens`.

**Any other server** that accepts `POST {base-url}/chat/completions` in the OpenAI format: look up
its base URL and model name in its documentation and use the same command.
Plain `http://` is accepted only for `localhost`; everything else must be `https://`.

**Anything else (your own API, a CLI tool, a research model)**: write a small provider.
```python
import sbp

class MyProvider(sbp.Provider):
    name = "mine"
    def complete(self, prompt: str) -> str:
        self._spend()                      # keeps the call budget honest
        return call_my_model(prompt)       # your code here; return the reply text

report = sbp.run_benchmark(MyProvider(max_calls=20), sbp.DEFAULT_QUERY, judge=False)
print(sbp.render_markdown(report))
```

## Settings

| Setting | Meaning |
|---|---|
| `ANTHROPIC_API_KEY` | key for `--provider anthropic` |
| `SBP_API_KEY` | key for `--provider openai-compatible` (optional for local servers) |
| `SBP_BASE_URL`, `SBP_MODEL` | defaults for `--base-url` and `--model` |
| `--max-calls N` | hard cap on model calls, retries included (default 20) |
| `--max-tokens N` | output limit per call (default 4096). Some models spend part of it on hidden reasoning; if answers are cut off or empty, raise it |

## Reading the results honestly

- `--judge` asks the **same model** to score the three transcripts. The judge can see step labels such as
  `[negation]`, so it is not blind to the method, and a model can favour its own style. Treat the scores as a
  smoke test, not as proof.
- One question, one run. Different models give different numbers; results from different models are not comparable.
- The README's own figures came from a single session, and it does not state how "Overall" is computed.
  It is not the plain mean of the README's table rows, so this script's averages are a different statistic.
- Some servers always report a normal finish, so a cut-off answer may go unflagged. If an answer ends abruptly, raise `--max-tokens`.

## Safety

- No network unless you choose a real provider. There is no telemetry.
- Keys are read only from environment variables, never printed, and removed from error messages.
- Redirects are refused and only `http(s)` is used, so a key cannot be forwarded elsewhere and `file://`
  addresses cannot be read.
- Prompt text is length-limited and cleaned. Text handed to a model is wrapped in tags and marked as material, not instructions. This lowers prompt-injection risk; it cannot remove it.
- Model output is never executed or imported. Plug-ins are registered in code only.
- `sbp_runs/` and `.env` files are git-ignored so results and keys are not committed by accident.

## Running it on GitHub

`.github/workflows/ci.yml` runs the tests automatically on every push, offline.
For a live run: add a repository secret (`ANTHROPIC_API_KEY`, or `SBP_API_KEY` plus a repository *variable*
`SBP_BASE_URL`), then Actions -> "SBP benchmark (manual, live model)" -> Run workflow.
GitHub's servers cannot reach your local Ollama; run local models on your own machine.
In a public repository the job log is public, so do not benchmark private text there.
