
all:
	python3 -m unittest

one:
	python3 tests.py TestSolutions.test_solution_a1

clean:
	rm -rf __pycache__/
	rm -rf solutions/__pycache__/
	rm -rf ./*pyc
