class India:
    def capital(self):
        print("The Capital of India is New Delhi")

    def language(self):
        print("Hindi and English")

class Usa:
    def capital(self):
        print("The Capital of USA is Washington")

    def language(self):
        print("English")

ind = India()
usa = Usa()
for country in (ind,usa):
    country.capital()
    country.language()
