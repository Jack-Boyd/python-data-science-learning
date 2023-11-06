import numpy as np
#Vectors

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])
scalar = 2

v_add = v1 + v2
v_subtract = v1 - v2
v_scalar = v1 * scalar
v_sum = np.sum([v1, v2, v3], axis=0)
v_mean = np.mean([v1, v2, v3], axis=0)
dot_product = v1.dot(v2) 
sum_of_squares = np.sum(v1**2)
magnitude = np.linalg.norm(v1)
distance = np.linalg.norm(v1-v2)

#Matrices

m1 = np.mat('4 3; 2 1')
m2 = np.mat('1 2; 3 4')

identity = np.eye(3)
m_shape = m1.shape
m_row = m1[0,:]
m_col = m1[:,0]
m_multiply = np.matmul(m1, m2)

#Numpy functions
#Array creation
range_one_to_ten = np.arange(1, 11)
range_of_numers_with_bigger_step = np.arange(1, 11, 2)
array_of_zeros = np.zeros(3)
array_of_ones = np.ones(3)
evenly_spaced_array_in_interval = np.linspace(0,10,3)

one_dimensional_uniform_dist_random_array = np.random.rand(2)
two_dimensional_uniform_dist_random_array = np.random.rand(3, 3)
one_dimensional_std_normal_dist_random_array = np.random.randn(2)
two_dimensional_std_normal_dist_random_array = np.random.randn(4, 4)
random_array_within_range = np.random.randint(1,100)

#Array Indexing
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
rangearr = np.arange(0, 11)
val = 5

change_arr_shape = arr.reshape(5,5)
randarr_max_value = ranarr.max()
randarr_max_index = ranarr.argmax()
randarr_min_value = ranarr.min()
randarr_min_index = ranarr.argmin()

#With numpy array, you can broadcast value into range
rangearr[0:5] = 100
#Can make a copy with .copy, assignment only assigns pointer under new variable name
arr_copy = rangearr.copy()
#Setup 10x10 array, each value is the positions row index
arr2d = np.zeros((10,10))
arr_length = arr2d.shape[1]
for i in range(arr_length):
    arr2d[i] = i

fancy_indexed_values_in_any_order = arr2d[[6,4,2,7]]
index_with_condition = arr[arr > 4]
index_with_condition_containing_variables = arr[arr < val]

#Array Operations
op = np.arange(1, 10)
add = op + op
multiply = op * op
subtract = op - op
divide = op / op
power_of_negative_one = 1 / op
exponent = op**3
square_root = np.sqrt(op)
exponential = np.exp(op)
sine = np.sin(op)
logirithm = np.log(op)
