# import itertools

# # Condition and action stubs
# CONDITION_STUBS = ["DGS & D", "Agent", "Retailer", "Order > 50,000", "Order ≥ 20000 to < 50,000", "Order < 20,000", "Furniture"]
# ACTION_STUBS = ["Discount of 5%", "Discount of 8%", "Discount of 10%", "Discount of 12%", "Discount of 15%"]

# # Generate all possible combinations of conditions
# condition_combinations = list(itertools.product([True, False], repeat=len(CONDITION_STUBS)))

# # Generate rules based on condition combinations and actions
# rules = []
# for conditions in condition_combinations:
#     rule = {"conditions": [], "action": None}
#     for condition, condition_stub in zip(conditions, CONDITION_STUBS):
#         if condition:
#             rule["conditions"].append(condition_stub)
#     for action, action_stub in enumerate(ACTION_STUBS, start=1):
#         if conditions[action - 1]:
#             rule["action"] = f"A{action}: {action_stub}"
#             break
#     rules.append(rule)

# # Print generated rules
# for i, rule in enumerate(rules, start=1):
#     print(f"R{i} - Conditions: {', '.join(rule['conditions'])}, Action: {rule['action']}")

import spacy

# Load English tokenizer, POS tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Input sentence
input_sentence = "For orders of more than Rs 50,000, agents get a discount of 15% and the retailer gets a discount of 10%."

# Process the input sentence using spaCy
doc = nlp(input_sentence)

# Initialize condition and action stubs
conditions = []
actions = []

# Extract conditions and actions
for token in doc:
    if token.dep_ in ["nummod", "amod"] and token.head.dep_ == "npadvmod":
        conditions.append(f"C{len(conditions) + 1}: {token.head.text} > {token.text}")
    elif token.text.lower() in ["agents", "retailer"]:
        actions.append(f"A{len(actions) + 1}: Discount of {token.head.text.strip('%')}%")

# Output condition and action stubs
print("Condition Stub:")
for condition in conditions:
    print(condition)

print("\nAction Stub:")
for action in actions:
    print(action)
