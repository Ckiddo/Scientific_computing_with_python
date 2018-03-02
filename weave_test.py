import weave as weave
import numpy as np 
import time

def my_sum(a):
	n = int(len(a))
	code = """
	int i;
	double counter;
	counter = 0;
	for(i = 0;i < n;i++){
		counter = counter + a(i);
	}
	return_val = counter;
	"""
	err = weave.inline(
		code,
		['a','n'],
		type_converters = weave.converters.blitz,
		compiler = "gcc"
	)
	return err

a = np.arange(0,10000000,1.0)
my_sum(a)

start = time.clock()
for i in xrange(100):
	my_sum(a)
print "my_sum",(time.clock() - start) / 100.0
start = time.clock()
for i in xrange(100):
	np.sum(a)
print "np.sum",(time.clock() - start) / 100.0
start = time.clock()
sum(a)
print "sum",time.clock() - start