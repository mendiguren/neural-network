import numpy

class inputLayer:

	def __init__(self, input_len):
		self.input_len = input_len;
		return
	

	def forward(self, input):
		#Generate random array
		random = numpy.random.rand(self.input_len)

		#Consider a neuron was active if the generated random number
		#Is smaller than the input.

		#This means if the input is close to 1, most of the time it will spiked
		#Otherwise, is unprobable it will spike.

		#We could apply a function to the input, to make it more close to .5
		#This way it would be less determnistic 
		spiked = random < input
		return spiked

	def backward(self, output):
		#Because this layers hasn't have any learnable parameter
		#We don't implement any backward pass
		pass

class fullyConectedLayer:

	def __init__(self, input_len , layer_len ):
		self.input_len = input_len;
		self.layer_len = layer_len;

		##Initialize weights

		#Excitary weights goes from input to the output.
		#Excitatory weights describes the probability that a neuron in this layer will fired
		#given that an input neuron layered fired.
		self.excitatory = numpy.random.uniform(5.0,6.5,size=(self.input_len,self.layer_len))

		#Inhibitory weights connect neurons from within this layers.
		#This inhibitory acts as a competition between neurons in the layer.
		self.inhibitory = numpy.random.uniform(0.5,1.0,size=(self.layer_len,self.layer_len))

		#this atribute is explain in forward method
		self.temperature = 1.0

	def forward(self, input):

		#We allow excitatory weights to be between 0 and 10
		#we then substract 5.0 element wise, make it goes from -5.0 to 5.0
		#after that we apply a sigmoid function so it goes from ~0.0 to ~1.0
		#this is then consider as the probabillity of firing, base on this
		#We randomly make it fired.
		output_ex = numpy.dot(input, self.excitatory - 5.0)

		#Inhibitory weights makes neurons which large output inhibit other neurons.
		#Making them less probable to spike
		output_inh = numpy.dot(output_ex, self.inhibitory - 5.0)

		#We  sum both, the excitatory and inhibitory behaviors to get the final output
		output = output_ex - output_inh

		#Tempeature makes the output smaller, make the probability closer to 0.5
		#being 0.5 the value where the variance is larger.
		#This makes our network have a more random behavior, which is good for 
		#exploring possible solutions. 
		#Temperature should drop to 1.0 as trainning progress.
		probabillity = 1/(1 + numpy.exp(-1 * output_ex/self.temperature))

		#Consider a neuron was active if the generated random number
		#Is smaller than the input.
		random = numpy.random.rand(self.input_len)

		#This means if the input is close to 1, most of the time it will spiked
		#Otherwise, is unprobable it will spike.
		spiked = random < input

		return spiked

	def backward(self, output):
		pass

