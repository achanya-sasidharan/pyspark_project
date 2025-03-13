from data_loading import create_dataframe
import logging

data_path = 'Data/Rider-Info.csv'


try:
    food_delivery = create_dataframe(data_path)
    food_delivery.show()
    print('---data frame created successfully')
    print('*******************************')
    logging.basicConfig(filename='logs/log_info.log',
                        level=logging.INFO,
                        format= '%(asctime)s,%(levelname)s ,%(message)s ')
    logging.info('Data frame created successfully')


except Exception as e:
    print(f'There is some error while creating table:{e}')
    print('***************')

    logging.basicConfig(filename='logs/log_info.log',
                        level=logging.ERROR,
                        format='%(asctime)s ,%(levelname)s ,%(message)s')
    logging.error(f'there is some error while creating table:{e}')



