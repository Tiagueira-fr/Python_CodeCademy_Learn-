# Physics Class

train_mass = 22680
train_acceleration = 10
train_distance = 100
train_mass = 22680


  # 1 , 2
def f_to_c (f_temp):
  c_temp = (f_temp - 32) * 5 / 9
  return c_temp

print (f_to_c(100))

  # 3 , 4
def c_to_f (c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

print (c_to_f(0))

  # 5 , 6
def get_force (train_mass , train_acceleration ):
  #train_mass = 22680
  #train_acceleration = 10
  x = train_mass * train_acceleration
  return  x
print("The GE train supplies X Newtons of force" , get_force(train_mass , train_acceleration))

  # 8 , 9
def get_energy (train_mass , c = 3*10**8): 
  return train_mass * c**2

  # 10 , 11 , 12 ,13
bomb_mass = 1
bomb_energy = get_energy (bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.") 

def get_work(train_mass , train_acceleration , train_distance):
  force = get_force(train_mass , train_acceleration)
  return force * train_distance

train_work = get_work(train_mass , train_acceleration , train_distance) 

print("The GE train does " , train_work , " Joules of work over " , train_distance , " meters.")
