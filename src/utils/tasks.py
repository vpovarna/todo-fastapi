import uuid


def generate_task_id() -> str:
    """
    Generate a random task id
    """
    return uuid.uuid4().hex
