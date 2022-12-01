import accumulator

def test_accumulator_constructor():
	a = accumulator.Accumulator(4.)
	assert a.sum == 4.
	assert a.last == 4.

def test_accumulator_add():
	a = accumulator.Accumulator(4.)
	a.add(12.)
	assert a.sum == 16.
	assert a.last == 12.
