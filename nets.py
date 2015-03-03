from layers import *
import numpy

class simpleNet:

	def __init__(self, architecture):

		self.layers = list()

		#Create the fully conected layers based on the architecture
		for layer_size in architecture:

			if layer_size == architecture[0]:
				#Create the first layers based on dataset size
				self.layers.append(inputLayer(layer_size))
				last_layer_size = layer_size

			else:
				self.layers.append(fullyConectedLayer(last_layer_size, layer_size))


			#For next loop iteration
			last_layer_size = layer_size

		#Create the output layer
		self.layers.append(outputLayer(last_layer_size))


	def forward(self, input):

		for layer in self.layers:
			input = layer.forward(input)
			
			print '--------------------------------------'
			print layer
			print input
		return input


