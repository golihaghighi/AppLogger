import logging
import logging.handlers
from platform import platform
from singleton_decorator import singleton

@singleton
class AppLogger:
    def __init__(self):
        self.configure_logger()

    def configure_logger(self):
        self.logger = logging.getLogger("AppLogger")
        self.logger.setLevel(logging.DEBUG)
        self.add_file_handler()
        self.add_syslog_handler()
        # Add more handlers as needed

    def add_file_handler(self):
        file_handler = logging.FileHandler('app.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def add_syslog_handler(self):
        if platform.system() == 'Linux':
            handler = logging.handlers.SysLogHandler(address='/dev/log')
            self.logger.addHandler(handler)
        elif platform.system() == 'Windows':
            # Configure Windows Event Log handler
            pass

    # Define other handlers (SMTP, Database, etc.) here

    def log(self, level, msg, *args, **kwargs):
        if hasattr(self.logger, level):
            getattr(self.logger, level)(msg, *args, **kwargs)

    # Contextual logging method
    def log_with_context(self, level, msg, context=None):
        if context:
            msg = f"{msg} | Context: {context}"
        self.log(level, msg)

    # # Utility method for API call logging
    # def log_api_call(func):
    #     @wraps(func)
    #     def wrapper(*args, **kwargs):
    #         try:
    #             return func(*args, **kwargs)
    #         except Exception as e:
    #             self.log('error', f"API call failed: {str(e)}")
    #             raise e
    #     return wrapper
