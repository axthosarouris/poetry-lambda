from assertpy import assert_that


class HelloTest:

    def should_return_hello(self):
        assert_that(1).is_equal_to(1)
