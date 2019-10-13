from datetime import datetime
from datetime import timedelta

class AverageCalc:

    def __init__(self, window_size):
        self.window_size = window_size
        self.timestamp_duration =[]
        self.delta_increment = timedelta(minutes=1)
        self.delta_window = timedelta(minutes=10)
        self.overlap_list = []
    
    def add_tranlation_delivered(self, tranlation_delivered):   
        button = self.__get_time_until_minutes(tranlation_delivered.timestamp) + self.delta_increment
        top = button + self.delta_window
        self.timestamp_duration.append((button, top, tranlation_delivered.duration))
            
    def cal_avg_delivered_time(self):

        if len(self.timestamp_duration) > 0:

            self.overlap_list = []
            reference = self.__get_time_until_minutes(self.timestamp_duration[0][0]) - self.delta_increment
            
            while len(self.timestamp_duration) > 0:
            
                self.__update_overlap_list(reference)
                self.__print_overlap_list(reference)                
                self.__update_timestamp_duration()

                reference += self.delta_increment

    def __update_overlap_list(self, reference):
        
        self.__remove_element_out_of_range(reference)

        for item in self.timestamp_duration:
            if item[0] > reference:
                break
            self.overlap_list.append(item)
    
    def __remove_element_out_of_range(self, reference):
        result = []
        for item in self.overlap_list:
            if item[1] > reference:
                result.append(item)
        self.overlap_list = result

    def __update_timestamp_duration(self):
        for item in self.overlap_list:
            if item in self.timestamp_duration:
                self.timestamp_duration.remove(item)

    def __print_overlap_list(self, reference):
        avg = 0
        if len(self.overlap_list) > 0:
            size = len(self.overlap_list)
            amount = 0
            for item in self.overlap_list:
                amount += item[2]
            avg = amount/size

        self.__print(reference, avg)
   
    def __print(self, time, avg):
        print("{0}, {1}".format(time, avg))

    def __get_time_until_minutes(self, timestamp):
        
        return  datetime(year=timestamp.year,
                    month=timestamp.month,
                    day=timestamp.day,
                    hour=timestamp.hour,
                    minute=timestamp.minute)
