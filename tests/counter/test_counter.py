from src.pre_built.counter import count_ocurrences


def test_counter():
    count_python = count_ocurrences("data/jobs.csv", "Python")
    count_javascript = count_ocurrences("data/jobs.csv", "Javascript")
    count_python_javascript = count_python + count_javascript
    assert count_python_javascript == 1761
