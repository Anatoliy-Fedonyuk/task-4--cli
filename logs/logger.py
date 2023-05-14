"""test logging"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создаем хендлер для записи сообщений в файл
file_handler = logging.FileHandler('collect_framework.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))

# Добавляем хендлер к логгеру
logger.addHandler(file_handler)

# Тестируем логирование
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')