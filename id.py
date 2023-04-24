import random
import string


def random_sample(count, start, stop, step=1):
    def gen_random():
        while True:
            yield random.randrange(start, stop, step)

    def gen_n_unique(source, n):
        seen = set()
        seenadd = seen.add
        for i in (i for i in source() if i not in seen and not seenadd(i)):
            yield i
            if len(seen) == n:
                break
    return [i for i in gen_n_unique(gen_random,
                                    min(count, int(abs(stop - start) / abs(step))))]


def transact_id():
    random_int = random.randint(100000, 999999)

    # Generate a random string of uppercase letters
    random_string = ''.join(random.choices(string.ascii_uppercase, k=5))

    # Combine the integer and string to create the transaction ID
    transaction_id = str(random_int) + random_string

    return (transaction_id)
