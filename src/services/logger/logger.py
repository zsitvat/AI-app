import logging
import sys

from .logs_json_formatter import JSONFormatter
    
class LoggerService:

    def _get_log_level(self,log_level: str = "DEBUG"):
        """ Get the log level based on the log level string 
        
        Args:
            log_level (str): The log level string

        Returns:
            int: The log level integer
        """

        if (log_level == "DEBUG"):
            return logging.DEBUG
        elif (log_level == "INFO"):
            return logging.INFO
        elif (log_level == "WARNING"):
            return logging.WARNING
        elif (log_level == "ERROR"):
            return logging.ERROR
        elif (log_level == "CRITICAL"):
            return logging.CRITICAL
        elif (log_level == "FATAL"):
            return logging.FATAL
        elif (log_level == "NOTSET"):
            return logging.NOTSET
        else:
            return logging.DEBUG


    def setup_logger(self,log_level: str = "DEBUG"):
        """ Setup the logger

        Args:
            log_level (str): The log level string 
        
        Returns:
            logger (logging.Logger): The logger object
        """

        logger = logging.getLogger("logger")
        logger.setLevel(self._get_log_level(log_level))

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)

        formatter = JSONFormatter()
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        return logger
