from rules import rules

print("AI Medical Diagnosis System")
print("----------------------------")

# Load symptoms from file
with open("symptoms.txt", "r") as file:
    symptoms_list = [line.strip() for line in file]

user_symptoms = []

# Ask user questions
for symptom in symptoms_list:
    answer = input(f"Do you have {symptom.replace('_', ' ')}? (yes/no): ")
    if answer.lower() == "yes":
        user_symptoms.append(symptom)

print("\nAnalyzing symptoms...\n")

results = {}

# Calculate matching score
for disease, symptoms in rules.items():
    match_count = 0

    for s in symptoms:
        if s in user_symptoms:
            match_count += 1

    score = match_count / len(symptoms)

    if score > 0:
        results[disease] = score

# Sort diseases by score
sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

print("Possible Diseases:\n")

for disease, score in sorted_results[:5]:
    print(f"{disease} : {round(score * 100)}% match")

if not results:
    print("No disease identified. Please consult a doctor.")