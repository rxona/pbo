print('Pilihan')
options = ['Capucino', 'Teh']
for index, option in enumerate(options):
    print(str(index + 1) + '.', option)

print(str(len(options) + 1) + '.', 'Exit')

try:
    optionIndex = int(input('Masukkan pilihan: ')) - 1
    print('Memilih', options[optionIndex])
    price = int(input('Masukkan harga: '))
    print(price + price /10)
except:
    print('Exit')
