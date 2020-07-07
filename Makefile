
testLookup:
	make swapInit
	-python3 -m unittest
	make swapFinal

swapInit:
	mv solutions solutions2
	mv lookup solutions

swapFinal:
	mv solutions lookup
	mv solutions2 solutions

testSolutions:
	python3 -m unittest

testSingleSolution:
	python3 tests.py TestSolutions.test_solution_a1

clean:
	rm -rf __pycache__/
	rm -rf solutions/__pycache__/
	rm -rf lookup/__pycache__/
	rm -rf ./*pyc
