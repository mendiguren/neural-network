from tqdm import *
import numpy

import dataset
from nets import simpleNet
from ma import movingAverage

data = dataset.load_dictionary()[0:4]
nn = simpleNet(architecture=numpy.array([15 , data.shape[0]]))

success_rate = dict()
for epoch in tqdm(range(40000)):
	scored  = 0.0
	for example in range(data.shape[0]):

		input = data[example][1]
		target = data[example][0]

		output = nn.forward(input)

		if example not in success_rate:
			success_rate[example] = movingAverage(100)
		else:
			success_rate[example].append(float(output == target))

		reward = -0.5 *  success_rate[example].mean 
		if output == target:
		 	reward = 1.0 * (1 - success_rate[example].mean)
		 	scored += 1.0

		#print output, target
		nn.backward(reward)

	if epoch % 1000 == 0:
		print scored / data.shape[0] 
