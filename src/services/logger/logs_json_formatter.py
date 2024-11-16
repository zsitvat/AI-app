import logging
import json

class JSONFormatter(logging.Formatter):
    """ Custom JSON Formatter for logging 
    
    Args:
        logging.Formatter: The logging formatter class
    
    Returns:
        JSONFormatter: The JSON formatter object
    """

    def format(self, record):
        log_data = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "function": record.funcName,
        }
        return json.dumps(log_data)