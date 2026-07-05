from loguru import logger

logger.add(
    "logs/ai_system.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO"
)

logger.info("AI Logger Initialized")