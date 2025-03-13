import logging

def log_Error(message):
    logging.basicConfig(filename='logs/log_info.log',
                        level=logging.INFO,
                        format='%(asctime)s,%(levelname)s ,%(message)s ')
    return logging.error(f'there is some error:{message} ')

def log_Info(message):
    logging.basicConfig(filename='logs/log_info.log',
                        level=logging.ERROR,
                        format='%(asctime)s ,%(levelname)s ,%(message)s')
    return logging.info(f'{message}')
