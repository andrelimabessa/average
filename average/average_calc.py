import json
from datetime import datetime
from datetime import timedelta

class AverageCalc:

    def __init__(self, window_size):
        self.__window_size = window_size
        self.__timestamp_duration =[]
        self.__delta_increment = timedelta(minutes=1)
        self.__delta_window = timedelta(minutes=10)
        self.__overlap_list = []
    
    def add_tranlation_delivered(self, tranlation_delivered):   
        button = self.__get_time_until_minutes(tranlation_delivered.timestamp) + self.__delta_increment
        top = button + self.__delta_window
        self.__timestamp_duration.append((button, top, tranlation_delivered.duration))
            
    def cal_avg_delivered_time(self):
        if len(self.__timestamp_duration) > 0:

            self.__overlap_list = []
            reference = self.__get_time_until_minutes(self.__timestamp_duration[0][0]) - self.__delta_increment
            
            while len(self.__timestamp_duration) > 0:
            
                self.__update_overlap_list(reference)
                self.__print_overlap_list(reference)                
                self.__update_timestamp_duration()

                reference += self.__delta_increment

    def __update_overlap_list(self, reference):
        self.__remove_element_out_of_range(reference)

        for item in self.__timestamp_duration:
            if item[0] > reference:
                break
            self.__overlap_list.append(item)
    
    def __remove_element_out_of_range(self, reference):
        result = []
        for item in self.__overlap_list:
            if item[1] > reference:
                result.append(item)
        self.__overlap_list = result

    def __update_timestamp_duration(self):
        for item in self.__overlap_list:
            if item in self.__timestamp_duration:
                self.__timestamp_duration.remove(item)

    def __print_overlap_list(self, reference):
        avg = 0
        if len(self.__overlap_list) > 0:
            size = len(self.__overlap_list)
            amount = 0
            for item in self.__overlap_list:
                amount += item[2]
            avg = amount/size

        self.__print(reference, avg)
   
    def __print(self, time, avg):
        print(json.dumps({"date": str(time), "average_delivery_time": avg}))

    def __get_time_until_minutes(self, timestamp):
        return  datetime(year=timestamp.year,
                    month=timestamp.month,
                    day=timestamp.day,
                    hour=timestamp.hour,
                    minute=timestamp.minute)
