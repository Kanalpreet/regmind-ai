from backend.llm.conflict_detector import detect_conflict


query = "What are periodic KYC updation requirements?"


result = detect_conflict(query)


print("\n🚀 CONFLICT DETECTION RESULT:\n")

print(result)