plug-in Architecture 

class CustomTransformer:
    def transform(self, prompt):
        ...


CLI Interface

$ sbp "Explain quantum computing simply."



      
core.py



from .negation import negate
from .interrogation import interrogate
from .affirmation import affirm

class ThreeStepReflective:
    def transform(self, prompt: str) -> dict:
        neg = negate(prompt)
        question = interrogate(prompt)
        aff = affirm(prompt)

        return {
            "original": prompt,
            "negation": neg,
            "interrogation": question,
            "affirmation": aff
        }


negation.py
def negate(prompt: str) -> str:
    return f"Do not respond to the following superficially or without critical depth: {prompt}"

interrogation.py

def interrogate(prompt: str) -> str:
    return f"What assumptions underlie this prompt, and under what conditions would it fail: {prompt}?"

affirmation.py
def affirm(prompt: str) -> str:
    return (
        f"Provide a structured, well-reasoned, and balanced response to: {prompt}. "
        "Include explanation, implications, and counterpoints."
    )


types.py

from typing import TypedDict

class TransformationResult(TypedDict):
    original: str
    negation: str
    interrogation: str
    affirmation: str


Example Usage


from three_step_reflective import ThreeStepReflective

engine = ThreeStepReflective()

result = engine.transform("Explain quantum computing simply.")

print(result["interrogation"])


test_core.py

from three_step_reflective.core import ThreeStepReflective

def test_transform_structure():
    engine = ThreeStepReflective()
    result = engine.transform("Test prompt")

    assert "negation" in result
    assert "interrogation" in result
    assert "affirmation" in result
