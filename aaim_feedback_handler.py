from typing import Dict, Any
import logging

class FeedbackHandler:
    """Handles feedback for nodes in the AAIM network."""

    def __init__(self):
        self.feedback_store = {}
        logging.basicConfig(
            filename="feedback_log.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def store_feedback(self, node_id: str, feedback: Dict[str, Any]) -> None:
        """
        Stores feedback for a node.
        
        Args:
            node_id: ID of the node to store feedback for.
            feedback: Dictionary containing feedback data.
        """
        try:
            self.feedback_store[node_id] = feedback
            logging.info(f