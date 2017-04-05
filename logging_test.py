import logging

logging.basicConfig(filename='log.log', format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                    datafmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.log(10,'log')

LOG = logging.getLogger(__name__)

LOG.debug('debug')
LOG.info('info')
LOG.warning('warning')
LOG.error('error')
LOG.critical('critical')
LOG.log(10,'log')
