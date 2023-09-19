date=input("What is the month?: , What is the day?: ")

holidays= {
        "Month: 1, Day: 1": "Nieuwjaarsdag",
        "Month: 4, Day: 7": "Goede Vrijdag",
        "Month: 4, Day: 9": "Pasen",
        "Month: 4, Day: 10": "Pasen",
        "Month: 4, Day: 27": "Koningsdag",
        "Month: 5, Day: 4": "Dodenherdenking",
        "Month: 5, Day: 5": "Bevrijdingsdag",
        "Month: 5, Day: 18": "Hemelvaartsdag",
        "Month: 5, Day: 28": "Pinksteren",
        "Month: 5, Day: 29": "Pinksteren",
        "Month: 12, Day: 5": "Sinterklaas",
        "Month: 12, Day: 25": "Kerst",
        "Month: 12, Day: 26": "Kerst",
        "Month: 12, Day: 31": "Oudejaarsavond"
}


if date in holidays: print(holidays[date])
else: print("No holiday found on given input")