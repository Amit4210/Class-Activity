class TipModel:
    def __init__(self, bill_amount=0, tip_percent=0, num_people=1):
        self.__bill_amount = bill_amount
        self.__tip_percent = tip_percent
        # Initialize the private attribute for splitting
        self.__num_people = num_people

    # Getter for bill_amount
    @property
    def bill_amount(self):
        return self.__bill_amount

    # Getter for tip_percent
    @property
    def tip_percent(self):
        return self.__tip_percent

    # Getter for num_people
    @property
    def num_people(self):
        return self.__num_people

    # Calculated property for the tip amount
    @property
    def tip_amount(self):
        return self.__bill_amount * self.__tip_percent

    # Calculated property for total cost divided by number of people
    @property
    def total_per_person(self):
        total = self.__bill_amount + self.tip_amount
        return total / self.__num_people

    # Setter for bill_amount with positive value validation
    @bill_amount.setter
    def bill_amount(self, value):
        if value < 0:
            raise ValueError("Error: \"bill amount\" must be positive.")
        else:
            self.__bill_amount = value
    
    # Setter for tip_percent converting whole numbers to decimals
    @tip_percent.setter
    def tip_percent(self, value):
        if value < 0:
            raise ValueError("Error: \"tip_percent\" must be positive.")
        else:
            self.__tip_percent = value / 100

    # Setter for num_people with a minimum of 1 person validation
    @num_people.setter
    def num_people(self, value):
        if value < 1:
            raise ValueError("Error: \"number of people\" must be at least 1.")
        else:
            self.__num_people = value

    # String representation for debugging and testing
    def __str__(self):
        return (f"Bill: ${self.bill_amount}, {self.tip_percent * 100}% tip. "
                f"Split between {self.num_people}: ${self.total_per_person:.2f} each.")
