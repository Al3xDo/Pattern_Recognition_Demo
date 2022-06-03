import logging 


INFO_LOGGER= "./server/log/app.log"
TEST_LOGGER= "./server/log/test_app.log"

logging.basicConfig(filename="./server/log/app.log")

info_formater= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
test_formater= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -  %(funcName)s(): %(lineno) %(message)s')

info_logger= logging.getLogger("INFO")
info_logger= logging.FileHandler(INFO_LOGGER)
info_logger.setFormatter(info_formater)
info_logger.setLevel(logging.INFO)