HITL_THRESHOLD = 0.7


def check_hitl_required(verification):

    confidence = verification.get("confidence", 0)

    if confidence < HITL_THRESHOLD:
        return True

    return False