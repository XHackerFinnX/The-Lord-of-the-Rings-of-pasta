macaron = 'abcdefghijklmnopqrstuvwxyz'
sum_macaron = [27, 28, 29, 26, 32, 31, 28, 26, 28, 30, 39, 32,
               27, 25, 441, 35, 26, 37, 30, 31, 28, 25, 31, 28, 26, 36]
sum_vlastelin = [188541, 36626, 37183, 117858, 281428, 56138, 55505, 148537, 140997, 1143, 20055, 99603,
                 55075, 158776, 177409, 29115, 1219, 137327, 137400, 200233, 58451, 18115, 59893, 1254, 42201, 999]
price = 295.59  # 295.59 руб. за 1 штуку
mass = 800  # 800 грамм.
sum_pack = 1  # Количество пакетов макарон
sum_macaron_vlastelin = []
surplus_macaron_vlastelin = []

print(f"Буквы    %total    Кол-во букв")
for i in range(26):
    if macaron[i] in macaron:
        print(
            f"{macaron[i]}        {round((sum_macaron[i]*100)/sum(sum_macaron), 2)}        {sum_macaron[i]}")
print('\n')
print(f"Сумма всех букв в одном пакете {sum(sum_macaron)}")
print('\n')

print(f"Буквы    %total    Кол-во букв")
for i in range(26):
    if macaron[i] in macaron:
        print(
            f"{macaron[i]}        {round((sum_vlastelin[i]*100)/sum(sum_vlastelin), 2)}        {sum_vlastelin[i]}")
print('\n')
print(f"Сумма всех букв в книге {sum(sum_vlastelin)}")
print('\n')

for i in range(26):
    if macaron[i] in macaron:
        sum_macaron_vlastelin.append(int(sum_vlastelin[i] / sum_macaron[i]))

for i in range(26):
    if macaron[i] in macaron:
        surplus_macaron_vlastelin.append(
            ((max(sum_macaron_vlastelin)+1) * sum_macaron[i]) - sum_vlastelin[i])

print(f"Всего понадобится: {max(sum_macaron_vlastelin)+1} пакетов макарон")
print(
    f"Общая стоимость пакетов макарон: {round((max(sum_macaron_vlastelin)+1) * price, 2)} рублей")
print(f"Осталось: {sum(surplus_macaron_vlastelin)} буквы макарон")
print(
    f"Масса пакетов макарон: {int(((max(sum_macaron_vlastelin)+1)*0.8) // 1000)} тонн и {int(((max(sum_macaron_vlastelin)+1)*0.8) % 1000)} килограмм")
