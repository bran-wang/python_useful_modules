import random
from retrying import retry


@retry(wait_fixed=600, stop_max_attempt_number=10)
def have_a_try():
    if random.randint(0, 10) != 5:
        print "oh no\n"
        raise Exception('It is not 5!')
    print 'it is 5!'


if __name__ == "__main__":
    have_a_try()
