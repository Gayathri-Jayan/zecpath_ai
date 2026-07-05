from screening_ai.conversation_flow import conversation_step

answer = {

    "question_id": "Q3",

    "is_vague": True,

    "off_topic": False,

    "confidence_score": 50
}

result = conversation_step(answer)

print(result)

assert result["state"] == "FOLLOW_UP"