TEST_DIR = tests/


typing:
	mypy PDE/


test: $(TEST_DIR)/*.py
	python $^