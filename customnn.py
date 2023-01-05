import numpy
from numpy import random
start=random.rand(10)
class Neuron:
    def __init__(self, input_shape):
        weights=random.rand(input_shape)
        bias=random.random()
    def calculate(self, inputs):
        return sum(weights*inputs)+bias
    def randomize(self):
        weights=weights+random.rand(weights.shape)
        bias+=random.random()
class Layer:
    def __init__(self, input_shape, size):
        layer_neurons=numpy.array([Neuron(input_shape) for i in range(size)])
    def calculate(self, inputs):
        return numpy.array([i.calculate(inputs) for i in layer_neurons])
    def randomize(self):
        for i in layer_neurons:
            i.randomize()
layer1=Layer(10, 5)
layer2=Layer(5, 5)
