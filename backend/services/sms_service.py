from backend.agents.dispatch_agent import make_sms

def send_mock_sms(task: dict, destination: str):
    return {
        "status": "mock_sent",
        "destination": destination,
        "message": make_sms(task),
    }
