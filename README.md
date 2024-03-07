# AppLogger

AppLogger is a highly versatile logging library designed for Python web applications. It seamlessly integrates with various web frameworks like Django and React, providing a robust solution for logging across both frontend and backend components. With support for multiple logging outputs such as files, system logs, databases, and SMTP, AppLogger ensures that your application's logging needs are comprehensively covered. It's built to run on both Linux and Windows platforms, automatically adapting to the underlying system for optimal performance.

## Features

- **Multi-Handler Support**: File, system, database, and SMTP logging.
- **Cross-Platform**: Compatible with Linux and Windows.
- **Contextual Logging**: Enhance logs with request ID, user ID, and more.
- **Integration Friendly**: Easily integrates into any part of your web app.
- **Utility Methods**: Simplify logging patterns, especially for API call error handling.
- **Singleton Pattern**: Ensures a single, global logging instance.

## Installation

```bash
pip install applogger
```

## Quick Start

```python
from applogger import AppLogger

logger = AppLogger.getInstance()
logger.log('info', 'This is an info message')
```

For more detailed usage and configuration options, please visit our [documentation](https://www.webmastersolve.com/).

## Contributing

We welcome contributions from the community! If you'd like to improve AppLogger, please fork the repository and submit a pull request.

---

AppLogger is proudly developed and maintained by the [WebMasterSolve](https://www.webmastersolve.com/) team.