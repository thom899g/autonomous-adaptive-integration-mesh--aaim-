from typing import Dict, Any
import logging

class NodeError(Exception):
    """Base exception class for Node-related errors."""
    pass

class Node:
    """Represents an autonomous node in the AAIM network."""

    def __init__(self, node_id: str):
        self.id = node_id
        self.task_queue = []
        self.feedback_buffer = {}
        self.status = "idle"
        logging.basicConfig(
            filename=f"node_{self.id}_log.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def process_task(self, task: Dict[str, Any]) -> None:
        """
        Processes a task and updates node state based on feedback.
        
        Args:
            task: Task dictionary containing task details and parameters.
            
        Raises:
            NodeError: If processing fails due to unexpected conditions.
        """
        try:
            # Simulate task processing
            if not task.get("valid", False):
                raise ValueError("Invalid task received")
            
            self.status = "processing"
            logging.info(f"Node {self.id} is processing task: {task}")
            
            # Simulate successful completion
            self.task_queue.pop(0)
            feedback = {"status": "success", "metrics": {"latency": 1.2}}
            self.receive_feedback(feedback)
            self.status = "idle"
            
        except Exception as e:
            logging.error(f"Node {self.id} failed to process task: {str(e)}")
            raise NodeError(f"Task processing failed for node {self.id}") from e

    def receive_feedback(self, feedback: Dict[str, Any]) -> None:
        """
        Handles feedback from completed tasks and updates learning data.
        
        Args:
            feedback: Dictionary containing feedback metrics and status.
        """
        try:
            self.feedback_buffer[self.task_queue[0]["id"]] = feedback
            logging.info(f"Node {self.id} received feedback: {feedback}")
            
            # Simulate learning process
            if feedback["status"] == "success":
                pass  # Apply optimization based on metrics
            else:
                pass  # Handle failure cases
            
        except IndexError:
            raise NodeError("No pending task to receive feedback")