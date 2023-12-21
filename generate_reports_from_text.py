def generate_report(data):
    report = "Report:\n"
    for line in data:
        # Customize this part based on the structure of your data
        report += f"Line: {line['line_number']}, Content: {line['content']}\n"

    with open('report.txt', 'w') as f:
        f.write(report)

text_data = [{'line_number': 1, 'content': 'Hi'},
             {'line_number': 2, 'content': 'Hello'},
             {'line_number': 3, 'content': 'Welcome'}]

generate_report(text_data)


