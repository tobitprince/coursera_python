def countries(countries_dict):
    result = ""
    for continent, countries in countries_dict.items():
        result += str(countries) + ":\n"
    return result

print(countries({"Europe": ["Sweden", "Norway", "Denmark"], "Asia": ["Japan", "China", "Thailand"]}))
    