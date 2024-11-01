import re
import os
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Domain-specific keywords to help differentiate steps with similar structure but different intent
DOMAIN_KEYWORDS = ["login", "registration", "checkout", "profile"]

# Common phrases that can be ignored in similarity comparisons
COMMON_PHRASES = ["an error message is displayed", "the user is redirected", "the user clicks"]

def calculate_semantic_similarity(step1, step2):
    embeddings1 = model.encode(step1, convert_to_tensor=True)
    embeddings2 = model.encode(step2, convert_to_tensor=True)
    return util.pytorch_cos_sim(embeddings1, embeddings2).item() * 100  

def keyword_adjusted_similarity(step1, step2, base_score):
    keywords1 = [word for word in DOMAIN_KEYWORDS if word in step1]
    keywords2 = [word for word in DOMAIN_KEYWORDS if word in step2]
    if keywords1 != keywords2:
        return base_score * 0.8  # Reduce score if keywords differ
    return base_score

def is_common_phrase(step):
    return any(phrase in step for phrase in COMMON_PHRASES)

def get_threshold_for_step_type(step_type):
    # Adjust similarity threshold based on the step type
    if step_type == "Then":
        return 75  # Require closer similarity for outcome steps
    return 85  # Higher threshold for Given and When steps

def find_similar_steps(steps):
    similar_steps = []
    for i in range(len(steps)):
        for j in range(i + 1, len(steps)):
            step1_text, step1_type, step1_file = steps[i]
            step2_text, step2_type, step2_file = steps[j]

            # Only compare steps of the same type
            if step1_type != step2_type:
                continue

            # Skip comparison if either step is a common phrase
            if is_common_phrase(step1_text) or is_common_phrase(step2_text):
                continue

            base_score = calculate_semantic_similarity(step1_text, step2_text)
            adjusted_score = keyword_adjusted_similarity(step1_text, step2_text, base_score)

            # Apply the similarity threshold based on step type and exclude 100% identical matches
            threshold = get_threshold_for_step_type(step1_type)
            if threshold <= adjusted_score < 100:
                similar_steps.append(((step1_text, step1_type, step1_file), (step2_text, step2_type, step2_file), adjusted_score))
    return similar_steps


def extract_steps_from_feature(file_path):
    steps = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'^\s*(Given|When|Then|And|But)\s+(.*)', line)
            if match:
                step_type = match.group(1)
                step_text = match.group(2).strip()
                steps.append((step_text, step_type, file_path))  # Store step with type and file reference
    return steps

def generate_report(similar_steps, report_path="reports/similar_steps_report.txt"):
    # If the report file exists, append a number to the filename
    if os.path.exists(report_path):
        base, extension = os.path.splitext(report_path)
        counter = 1
        # Find the next available filename
        while os.path.exists(f"{base}_{counter}{extension}"):
            counter += 1
        report_path = f"{base}_{counter}{extension}"

    with open(report_path, "w") as file:
        file.write("Similar Steps Found:\n\n")
        for (step1_text, step1_type, step1_file), (step2_text, step2_type, step2_file), score in similar_steps:
            file.write(f"Step 1: {step1_text} (Type: {step1_type}, File: {step1_file})\n")
            file.write(f"Step 2: {step2_text} (Type: {step2_type}, File: {step2_file})\n")
            file.write(f"Similarity Score: {score:.2f}\n")
            file.write("Note: Based on semantic similarity and domain-specific adjustments.\n\n")
    print(f"Report generated at {report_path}")

