rate_as_str = input("Оцените работу оператора от 1 до 5:")
rate_as_namber = int(rate_as_str)


if(rate_as_namber<1):
    rate_as_namber = 1

if(rate_as_namber>5):
    rate_as_namber = 5

print(rate_as_namber)

feetdback = ''

if rate_as_namber == 1:
    feetdback = input("Расскажите, что нам улучшить: ")
elif rate_as_namber == 2:
        feetdback = input("Расскажите, что вас смутило: ")
elif rate_as_namber == 3:
        feetdback = input("Расскажите, как нам стать лучше: ")
elif rate_as_namber == 4:
        feetdback = input("Расскажите, почему не 5: ")
else:
      feetdback =(" Расскажите, за что нам похвалить оператора: ")
print(feetdback)