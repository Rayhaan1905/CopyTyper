class AgentState:
    def __init__(self):
        self.last_output = None
        self.is_analyzing = False
        self.is_ready_to_type = False
        self.status = "idle"

state = AgentState()