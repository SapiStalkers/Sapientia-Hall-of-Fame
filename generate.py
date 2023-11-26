import json

with open('projects.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

projects_by_alphabet = {}

for project in data:
    name = project['name']
    letter = name[0].lower()

    if letter not in projects_by_alphabet:
        projects_by_alphabet[letter] = []

    projects_by_alphabet[letter].append(project)

lines = []
letters = sorted(projects_by_alphabet.keys())

headers = ['Name', 'Creator', 'GitHub', 'Website', 'Short description']
header_keys = ['name', 'creator', 'github', 'website', 'description']
table_headers = ' | '.join(headers)
header_separators = ' | '.join([':-:' for i in range(len(headers))])

for letter in letters:
    projects = projects_by_alphabet[letter]
    projects.sort(key=lambda x: x['name'])

    lines.append(f'### {letter.upper()}')
    lines.append('')
    lines.append(f'| {table_headers} |')
    lines.append(f'| {header_separators} |')

    for project in projects:
        columns = []

        for header, header_key in zip(headers, header_keys):
            display = f'{header_key}Display'
            value = project[header_key]
            
            if value == None:
                value = '-'

            if not isinstance(value, list):
                value = [value]

            if display in project:
                display_value = project[display]

                if not isinstance(display_value, list):
                    display_value = [display_value]

                columns.append(', '.join(f'[{display_value[i]}]({value})' for i, value in enumerate(value)))
            else:

                columns.append(', '.join(value))

        column_line = ' | '.join(columns)
        lines.append(f'| {column_line} |')
    
    lines.append('')

with open('readme_template.md', 'r', encoding='utf-8') as f:
    template = f.read()

with open('README.md', 'w', encoding='utf-8') as f:
    hallOfFame = '\n'.join(lines)

    f.write(template.replace('{hallOfFame}', hallOfFame))