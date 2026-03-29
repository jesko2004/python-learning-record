"""

from loguru import logger


logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning")
logger.error("This is an error")
"""

from loguru import logger

# 添加文件输出
logger.add("app.log", rotation="500 MB", retention="10 days", compression="zip")

logger.info("This will be written to app.log")
