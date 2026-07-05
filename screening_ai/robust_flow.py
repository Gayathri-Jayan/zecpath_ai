from screening_ai.edge_case_handler import detect_edge_case
from screening_ai.safety_fallback import get_fallback_response

MAX_RETRIES = 2 

def process_candidate_response(answer):

    issue = detect_edge_case(answer)

    if issue == "valid":

        return {

            "status": "processed",

            "message": "Response accepted."
        }

    return {

        "status": issue,

        "message": get_fallback_response(issue)
    }

MAX_RETRIES = 2


def retry_allowed(retry_count):

    return retry_count < MAX_RETRIES