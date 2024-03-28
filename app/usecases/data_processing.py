from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData


def process_agent_data(
    agent_data: AgentData,
) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    y_value = agent_data.accelerometer.y

    if y_value > 0 and y_value < 80:
        state = "GOOD"
    else:
        state = "REPAIR_REQUIRED"
        
    return ProcessedAgentData(road_state=state, agent_data=agent_data)
