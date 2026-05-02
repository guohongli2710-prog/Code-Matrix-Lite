```python
"""
Code-Matrix: Abstract Base Agent
Note: Implementation details stripped for open-source compliance.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
import asyncio
import logging

logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    def __init__(self, agent_id: str, model_name: str = "xiaomi-mimo-max"):
        self.agent_id = agent_id
        self.model_name = model_name
        self.memory_buffer: List[Dict[str, str]] = []
        self._max_retries = 5

    @abstractmethod
    async def process_task(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Core reasoning loop. Must be implemented by specific agents (e.g., TestFixAgent).
        """
        pass

    async def _call_llm_gateway(self, prompt: str, temperature: float = 0.2) -> str:
        """
        [REDACTED] Internal routing to LLM API Gateway.
        Handles rate limits and token tracking automatically.
        """
        logger.debug(f"[{self.agent_id}] Routing request to {self.model_name}. Prompt length: {len(prompt)}")
        # Implementation hidden due to internal API security.
        raise NotImplementedError("Gateway routing logic is not included in the Lite version.")

    def perform_self_reflection(self, error_trace: str) -> str:
        """
        Analyzes stack trace and generates prompt for CoderAgent to fix the bug.
        """
        reflection_prompt = f"""
        You are a senior debugging assistant. Analyze the following stack trace and provide a fix:
        {error_trace}
        """
        return reflection_prompt
