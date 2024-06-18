def generate_password(n):
    pass_= ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_

for n in range(3, 21):
    pass_ = generate_password(n)
    print(f"{n} - {pass_}")