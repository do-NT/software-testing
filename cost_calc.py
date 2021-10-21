import numpy as np

class Call:
    """A sample of Call class"""

    rate_per_min = 0.35
    tax = 0.04
    discount_1 = 0.5
    discount_2 = 0.15
    upper_bound = '1800'
    lower_bound = '0800'
    DAY_START = 0
    DAY_END = 23 * 60 + 59 #1439
    
    def __init__(self, hh, mm, duration) -> None:
        self.hh = hh
        self.mm = mm 
        self.start_time = hh*60 + mm
        self.duration = duration
        self.end_time = self.start_time + self.duration

        if isinstance(self.upper_bound, str):
            self.upper_bound = self.to_minute(self.upper_bound)
        if isinstance(self.lower_bound, str):
            self.lower_bound = self.to_minute(self.lower_bound)

        self.gross_cost = self.get_gross_cost()
        self.net_cost = self.get_net_cost()

    def get_gross_cost(self):
        if self.validate_time():
            return round(self.rate_per_min * self.duration, 2)
        else: 
            return "Invalid input"

    def get_net_cost(self):
        gross_cost = self.rate_per_min * self.duration
        if (self.validate_time()): 

            # Discount if the call is in a certain given time of the day
            if (self.start_time >= self.lower_bound and self.start_time <= self.upper_bound):
                net_cost = gross_cost
            else:
                net_cost = gross_cost * self.discount_1

            # Any call longer than 60 minutes receives a 15% discount on its cost
            if (self.duration >= 60):
                net_cost -= net_cost * self.discount_2
            
            # All calls are subject to a 4% Federal tax.
            tax = net_cost * self.tax
            net_cost += tax
            
            return round(net_cost, 2)
        else:
            return "Invalid input"


    # Old code that causes failure:
    # def validate_time(self):
    #     return self.start_time >= self.DAY_START and self.start_time <= self.DAY_END

    # Fixed code:
    def validate_time(self):
        return self.start_time >= self.DAY_START and self.start_time <= self.DAY_END and self.duration >= 0

    def to_minute(self, time):
        if len(time) != 4:
            result = -1
        else:
            hh, mm = time[:2], time[2:]
            result = int(hh) * 60 + int(mm)
        return result

    def __str__(self):
        start = f"Start time: {'%02d' % self.hh}:{'%02d' % self.mm} \n" if self.validate_time() else "Start time: Invalid input \n"
        duration = f"Duration: {self.duration} minutes \n"
        gross = f"Gross cost: ${self.gross_cost} \n"
        net = f"Net cost: ${self.net_cost} \n"
        return start + duration + gross + net

if __name__ == '__main__':
    new_call = Call(9, 20, -1)
    print(new_call)