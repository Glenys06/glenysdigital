class Review:
    count_id = 0
    def __init__(self, first_name, last_name, remarks, date_of_review):
        Review.count_id += 1
        self.__review_id = Review.count_id
        self.__date_of_review = date_of_review
        self.__first_name = first_name
        self.__last_name = last_name
        self.__remarks = remarks
    def get_review_id(self):
        return self.__review_id
    def get_date_of_review(self):
        return self.__date_of_review
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_remarks(self):
        return self.__remarks
    def set_review_id(self, review_id):
        self.__review_id = review_id
    def set_date_of_review(self, date_of_review):
        self.__date_of_review = date_of_review
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_remarks(self, remarks):
        self.__remarks = remarks