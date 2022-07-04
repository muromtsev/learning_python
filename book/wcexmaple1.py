import wizcoin

purse = wizcoin.WizCoin(2, 5, 99)
print(purse)
print(f"G: {purse.galleons}, S: {purse.sickles}, K: {purse.knuts}")
print(f"Total value: {purse.value()}")
print(f"Wight: {purse.weightInGrams()} grams")
print()

coinJar = wizcoin.WizCoin(13, 0, 0)
print(coinJar)
print(f"G: {coinJar.galleons}, S: {coinJar.sickles}, K: {coinJar.knuts}")
print(f"Total value: {coinJar.value()}")
print(f"Wight: {coinJar.weightInGrams()} grams")