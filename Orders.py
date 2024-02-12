class Orders:
    count_id = 0
    def __init__(self, flavour, scoops, serving_vessel, remarks):
        Orders.count_id += 1
        self.__order_id = Orders.count_id
        self.__flavour = flavour
        self.__scoops = scoops
        self.__serving_vessel = serving_vessel
        self.__remarks = remarks
    def get_order_id(self):
        return self.__order_id
    def get_flavour(self):
        return self.__flavour
    def get_scoops(self):
        return self.__scoops
    def get_serving_vessel(self):
        return self.__serving_vessel
    def get_remarks(self):
        return self.__remarks

    def set_order_id(self, order_id):
        self.__order_id = order_id
    def set_flavour(self, flavour):
        self.__flavour = flavour
    def set_scoops(self, scoops):
        self.__scoops = scoops
    def set_serving_vessel(self, serving_vessel):
        self.__serving_vessel = serving_vessel
    def set_remarks(self, remarks):
        self.__remarks = remarks