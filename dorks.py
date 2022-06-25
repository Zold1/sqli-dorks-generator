import random


def read_lines(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines


sites_file = input("Sites file (sites.txt): ")
if sites_file == "":
    sites_file = "sites.txt"
sites = read_lines(sites_file)

keywords_file = input("Keywords file (keywords.txt): ")
if keywords_file == "":
    keywords_file = "keywords.txt"
keywords = read_lines(keywords_file)

page_types_file = input("Page types file (page_types.txt): ")
if page_types_file == "":
    page_types_file = "page_types.txt"
page_types = read_lines(page_types_file)

page_parameters_file = input("Page parameters file (page_parameters.txt): ")
if page_parameters_file == "":
    page_parameters_file = "page_parameters.txt"
page_parameters = read_lines(page_parameters_file)

search_functions_file = input("Search functions file (search_functions.txt): ")
if search_functions_file == "":
    search_functions_file = "search_functions.txt"
search_functions = read_lines(search_functions_file)

patterns_file = input("Patterns file (patterns.txt): ")
if patterns_file == "":
    patterns_file = "patterns.txt"
patterns = read_lines(patterns_file)


dorks = []
print("Dorking...")

for pattern in patterns:
    for site in sites:
        for keyword in keywords:
            for page_type in page_types:
                for page_parameter in page_parameters:
                    for search_function in search_functions:
                        dork = (
                            pattern.replace("{site}", site.strip())
                            .replace("{keyword}", keyword.strip())
                            .replace("{page_type}", page_type.strip())
                            .replace("{page_parameter}", page_parameter.strip())
                            .replace("{search_function}", search_function.strip())
                        )
                        dorks.append(dork.strip())

print("Randomize dorks...")
random.shuffle(dorks)

print("Saving dorks...")
with open("dorks.txt", "w") as f:
    f.write("\n".join(dorks))
