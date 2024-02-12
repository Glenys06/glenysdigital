class Contact:
  count_id = 0

  def __init__(self, first_name, last_name, gender, email_address, feedback):
      Contact.count_id += 1
      self.__user_id = Contact.count_id
      self.__first_name = first_name
      self.__last_name = last_name
      self.__gender = gender
      self.__email_address = email_address
      self.__feedback = feedback

  def get_contact_id(self):
      return self.__user_id

  def get_first_name(self):
      return self.__first_name

  def get_last_name(self):
      return self.__last_name

  def get_gender(self):
      return self.__gender

  def get_email_address(self):
      return self.__email_address

  def get_feedback(self):
      return self.__feedback


  def set_contact_id (self, user_id):
        self.__user_id = user_id

  def set_first_name(self, first_name):
      self.__first_name = first_name

  def set_last_name(self, last_name):
      self.__last_name = last_name

  def set_gender(self, gender):
      self.__gender = gender

  def set_email_address(self, email_address):
      self.__email_address = email_address

  def set_feedback(self, feedback):
      self.__feedback = feedback



