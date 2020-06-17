import logging
import time

logger = logging.Logger(__name__)
# default is stderr
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s : - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

errorLogger = logging.Logger(__name__)
errorHandler = logging.FileHandler("logs/"+time.strftime("%Y%m%d-%H%M%S")+".txt","a", encoding="utf8")
errorHandler.setLevel(logging.DEBUG)
errorFormatter = logging.Formatter("%(asctime)s - %(name)s : - %(levelname)s - %(message)s")

errorHandler.setFormatter(errorFormatter)
errorLogger.addHandler(errorHandler)
