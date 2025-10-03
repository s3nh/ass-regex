tests = [
    "ul. Jana Pawła II 12/7, 00-175 Warszawa, woj. mazowieckie",
    "Al. 3 Maja 5 lok. 12 31-001 Kraków",
    "rondo ONZ 1 00-124 Warszawa",
    "Wieś Lipowa 4 12-345 Olsztyn",
    "60-001 Poznań skrytka pocztowa 45",
    "ul Kwiatowa 5 m. 7 00-001 Warszawa",
    "Rynek Główny 1 31-042 Kraków",
    "Bulwar Filadelfijski 10-12 87-100 Toruń",
]
for t in tests:
    print(t, extract_addresses(t))
