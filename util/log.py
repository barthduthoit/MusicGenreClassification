import logging

logging.basicConfig(filename='logfile.log', level=logging.DEBUG,
                    format='%(asctime)s %(name)-3s %(filename)-3s %(levelname)-3s: %(message)s')
logger = logging.getLogger(__name__)
