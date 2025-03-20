import logging

# Configuración para logs
logging.basicConfig(
    filename=r".\logs\logs.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)
