from typing import Dict, Any, Optional
import logging

class CommunicationManager:
    """Manages communication between nodes in the AAIM network."""

    def __init__(self):
        self.channels = {}
        logging.basicConfig(
            filename="communication_log.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def send_message(self, source_id: str, destination_id: str, message: Dict[str, Any]) -> None:
        """
        Sends a message from one node to another.
        
        Args:
            source_id: ID of the sending node.
            destination_id: ID of the receiving node.
            message: Dictionary containing message data.
            
        Raises:
            ValueError: If destination_id is not registered.
        """
        try:
            if destination_id not in self.channels:
                raise ValueError(f"Destination node {destination_id} not found")
                
            # Simulate message transmission
            logging.info(f"Sending message from {source_id} to {destination_id}: {message}")
            self.channels[destination_id].append(message)
            
        except Exception as e:
            logging.error(f"Communication failure: {str(e)}")
            raise

    def receive_message(self, node_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves incoming messages for a node.
        
        Args:
            node_id: ID of the receiving node.
            
        Returns:
            The next message in the queue or None if empty.
        """
        try:
            if node_id not in self.channels:
                raise ValueError(f"Node {node_id} not registered with communicator")
                
            # Simulate message retrieval
            if len(self.channels[node_id]) > 0:
                message = self.channels[node_id].pop(0)
                logging.info(f"Node {node_id} received message: {message}")
                return message
            else:
                return None
                
        except Exception as e:
            logging.error(f"Message retrieval failed: {str(e)}")
            return None

    def register_node(self, node_id: str) -> None:
        """
        Registers a new node with the communicator.
        
        Args:
            node_id: ID of the node to register.
        """
        try:
            if node_id in self.channels:
                raise ValueError(f"Node {node_id} already registered")
                
            self.channels[node_id] = []
            logging.info(f"Node {node_id} registered with communicator")
            
        except Exception as e:
            logging.error(f"Registration failed: {str(e)}")