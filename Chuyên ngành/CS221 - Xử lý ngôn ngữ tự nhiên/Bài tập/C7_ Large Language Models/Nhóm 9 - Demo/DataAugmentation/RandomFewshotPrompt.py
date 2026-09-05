def build_conspiracy_augmentation_prompt(example_1, example_2, example_3):
    return [
        {
            "role": "system",
            "content": (
                "You are an expert in linguistics, NLP, and the study of conspiracy narratives. "
                "You understand how conspiracy beliefs are expressed in natural language, "
                "including themes of hidden power, secret agendas, manipulation, and distrust of authorities."
            )
        },
        {
            "role": "user",
            "content": (
                "Task:\n"
                "Given three example sentences related to conspiracy theories, generate ONE new sentence that:\n"
                "- Clearly reflects a conspiracy belief\n"
                "- Is semantically different from the examples\n"
                "- Does NOT reuse entities, phrases, or structures from the examples\n"
                "- Sounds natural and realistic, like real-world discourse\n"
                "- Mentions hidden control, secret coordination, or powerful unseen actors\n"
                "- Has a length (number of words) roughly comparable to the examples "
                "(do not make it significantly shorter or longer)\n\n"
                "Examples:\n"
                f"1. {example_1}\n"
                f"2. {example_2}\n"
                f"3. {example_3}\n\n"
                "Output requirements:\n"
                "- Output ONLY one sentence\n"
                "- Match the approximate length of the example sentences\n"
                "- No explanations\n"
                "- No quotation marks"
            )
        }
    ]

def build_non_conspiracy_augmentation_prompt(example_1, example_2, example_3):
    return [
        {
            "role": "system",
            "content": (
                "You are an expert in linguistics and NLP, specializing in factual, neutral, "
                "and evidence-based discourse. You are skilled at identifying and producing "
                "statements that do NOT involve conspiracy theories, hidden agendas, or secret coordination."
            )
        },
        {
            "role": "user",
            "content": (
                "Task:\n"
                "Given three example sentences that are NOT related to conspiracy theories, "
                "generate ONE new sentence that:\n"
                "- Is clearly non-conspiratorial\n"
                "- Does NOT suggest secret plots, hidden control, or powerful unseen actors\n"
                "- Is semantically different from the examples\n"
                "- Does NOT reuse entities, phrases, or sentence structures from the examples\n"
                "- Sounds natural and realistic in everyday or informational discourse\n"
                "- Has a length (number of words) roughly comparable to the examples "
                "(do not make it significantly shorter or longer)\n\n"
                "Examples:\n"
                f"1. {example_1}\n"
                f"2. {example_2}\n"
                f"3. {example_3}\n\n"
                "Output requirements:\n"
                "- Output ONLY one sentence\n"
                "- Match the approximate length of the example sentences\n"
                "- No explanations\n"
                "- No quotation marks"
            )
        }
    ]



import json
import random


def load_jsonl(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def build_augmentation_messages_from_jsonl(
    jsonl_path,
    target_label="conspiracy",   # "conspiracy" or "non_conspiracy"
    seed=None
):
    """
    target_label:
        - "conspiracy"       -> sample from conspiracy == "Yes"
        - "non_conspiracy"   -> sample from conspiracy == "No"
    """

    if seed is not None:
        random.seed(seed)

    data = load_jsonl(jsonl_path)

    if target_label == "Yes":
        candidates = [x["text"] for x in data if x.get("conspiracy") == "Yes"]
        if len(candidates) < 3:
            raise ValueError("Not enough conspiracy samples to draw 3 examples.")
        examples = random.sample(candidates, 3)
        return build_conspiracy_augmentation_prompt(*examples)

    elif target_label == "No":
        candidates = [x["text"] for x in data if x.get("conspiracy") == "No"]
        if len(candidates) < 3:
            raise ValueError("Not enough non-conspiracy samples to draw 3 examples.")
        examples = random.sample(candidates, 3)
        return build_non_conspiracy_augmentation_prompt(*examples)

    else:
        raise ValueError("target_label must be 'conspiracy' or 'non_conspiracy'")
