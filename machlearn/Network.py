'''
	Network - Neural Networks - Neilsen
	22 August 2020
	William Cliff
'''
import numpy as np

class Network(object):

	def __init__(self, sizes):
		''' Random Weights and Biases
		'''
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y, 1)
							 for y in sizes[1:]]
		self.weights = [np.random.randn(y, x)
							 for x, y in zip(sizes[:-1], sizes[1:])]

# Network with 2-3-1 layers
net = Network([2, 3, 1])
