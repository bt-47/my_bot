import random
import string

def create_passwords(n_len: int, n_count: int) -> None:
    with open('passwords', 'w', encoding='utf-8') as file:
        a = string.ascii_letters + string.digits
        file.writelines(''.join([random.choice(a) for _ in range(n_len)]) + '\n' for _ in range(n_count))

create_passwords(10, 10)
