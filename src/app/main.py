"""Main entry point for the test writer service.

This script initializes logging and consumes messages to validate and display output behavior.
"""

import os
import sys

# Add 'src/' to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import config_shared
from app.queue_handler import consume_messages
from app.utils.setup_logger import setup_logger

# Use structured logging if enabled
logger = setup_logger(
    __name__,
    structured=config_shared.get_config_bool("STRUCTURED_LOGGING", False),
)


def test_output_callback(message: dict) -> None:
    """Callback that logs the received message for testing purposes."""
    logger.info("📥 Received test message: %s", message)


def main() -> None:
    """Start the test output consumer."""
    logger.info("🚀 Starting test writer service...")
    consume_messages(test_output_callback)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception("❌ Unhandled exception: %s", e)
        sys.exit(1)
