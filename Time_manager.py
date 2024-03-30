import datetime

class Cur_time:
    now  = datetime.datetime.now()
    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now()
    cur_time = "" 
    
    def set_cur_time():
        Cur_time.now = datetime.datetime.now()

    def get_cur_time():
        return Cur_time.cur_time
    
    def time_to_string(time: datetime.datetime):
        Cur_time.cur_time = time.strftime("%y-%m-%d %H:%M:%S")
        
    def print_time():
        print(Cur_time.cur_time)