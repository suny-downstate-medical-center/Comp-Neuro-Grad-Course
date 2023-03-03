class Animal:
  def __init__(self,animal_name,animal_type):
    self.animal_name = animal_name
    self.animal_type = animal_type

  def rename_my_pet(self,new_name):
    self.animal_name = new_name

  def how_to_pet(self):
    if self.animal_type == 'Dog':
      self.petting = 'rub my belly'
    elif self.animal_type == 'Cat':
      self.petting = 'scratch my back'
    elif self.animal_type == 'Mouse':
      self.petting = 'play with me'
    elif self.animal_type == 'Parrot':
      self.petting = 'teach me a word'
    else:
      self.petting = 'ask for help'
    print(self.petting)