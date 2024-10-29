# config.py - Файл конфигурации

# Конфигурация базы данных
DATABASE_NAME = "data/library.db"

# Конфигурация приложения
APP_NAME = "Library Management System"
APP_VERSION = "1.0.0"
APP_DEBUG = True  # Установите в False для продакшн-версии

# Конфигурация логирования
LOGGING_ENABLED = True
LOG_FILE = "logs/app.log"
LOG_LEVEL = "DEBUG"  # Уровни: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Конфигурация пользователя
DEFAULT_ADMIN_USERNAME = "admin"
DEFAULT_ADMIN_PASSWORD = "password"  # Используйте безопасные пароли в продакшн-среде

# Конфигурация SMTP для отправки электронной почты
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_email_password"
EMAIL_FROM = "your_email@example.com"

# Дополнительные параметры
MAX_CONNECTIONS = 5  # Максимальное количество соединений с базой данных
TIMEOUT = 30  # Таймаут для соединений (в секундах)