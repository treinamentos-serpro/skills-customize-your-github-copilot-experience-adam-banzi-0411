import unittest


def add_numbers(first: int, second: int) -> int:
    return first + second


def is_even(number: int) -> bool:
    return number % 2 == 0


def safe_divide(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    return numerator / denominator


class TestAddNumbers(unittest.TestCase):
    def test_adds_positive_numbers(self):
        # TODO: Replace pass with an assertion.
        pass

    def test_handles_zero_and_negative_numbers(self):
        # TODO: Replace pass with an assertion.
        pass


class TestIsEven(unittest.TestCase):
    def test_returns_true_for_even_numbers(self):
        # TODO: Replace pass with an assertion.
        pass

    def test_returns_false_for_odd_numbers(self):
        # TODO: Replace pass with an assertion.
        pass


class TestSafeDivide(unittest.TestCase):
    def test_divides_nonzero_numbers(self):
        # TODO: Replace pass with an assertion.
        pass

    def test_raises_value_error_when_dividing_by_zero(self):
        # TODO: Replace pass with an assertion.
        pass


if __name__ == "__main__":
    unittest.main()
