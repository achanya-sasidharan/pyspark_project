from data_loading import create_dataframe
import logs.log_fn as log

data_path = 'Data/Rider-Info.csv'


try:
    food_delivery = create_dataframe(data_path)
    food_delivery.show()
    print('--- Dataframe created successfully ---')
    print('***********')
    log.log_Info('Dataframe created successfully')

except Exception as e:
    print(f'There is some error while creating table: {e}')
    print('************')
    log.log_Error(e)

print('******** Analytics 1 ********')
from analytics.file1 import peak_Hours
try:
    result = peak_Hours(food_delivery)
    result.show()
    result.write.csv('Result/Analytics1',header=True,mode="overwrite")
    log.log_Info('Analytics1 executed and result generated')
except Exception as e:
    log.log_Error(e)


print('******** Analytics 1 ********')
from analytics.file2 import evening_riders
result= evening_riders(food_delivery)
result.show()
try:
    result = evening_riders(food_delivery)
    result.show()
    result.write.csv('Result/Analytics1',header=True,mode="overwrite")
    log.log_Info('Analytics1 executed and result generated')
except Exception as e:
    log.log_Error(e)
