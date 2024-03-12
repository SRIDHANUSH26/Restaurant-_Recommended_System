import pandas as pd

# Your pandas Series object
data = pd.Series(['Vadavalli', 'Vadivelampalayam', 'Kalampalayam', 'Siruvani', 'Iruttupallam',
                  'Alanthurai', 'alandurai', 'Siruvani', 'Karunyanagar', 'Alandurai',
                  'Pooluvapatti', 'Siruvani', 'Boluvampatti', 'Boluvampatti', 'Nadhagounden Pudur',
                  'Boluvampatti', 'Boluvampatti', 'Boluvampatti', 'Madawarayapuram', 'Vcv',
                  'Thenkarai', 'Karunya Nagar', 'Karunya Nagar', 'Vellimalaipattinam',
                  'Karunyanagar', 'Semmedu', 'Karunyanagar', 'Thenkarai', 'Siruvani',
                  'Vellimalaipattinam', 'Semmedu', 'Karunyanagar', 'Thondamuthur',
                  'Narasipuram', 'Mathampatti', 'Karunyanagar', 'Thondamuthur', 'Karunyanagar',
                  'Madhampatti', 'Karunyanagar', 'Booluvampatti', 'Narasipuram', 'Karunyanagar',
                  'Viraliyur', 'Thondamuthur', 'Thondamuthur', 'Narasipuram', 'Vellimalaipattinam',
                  'Karunyanagar', 'Thondamuthur'])

# Get unique values from the Series
unique_values = data.unique()

# Generate HTML options
html_options = ''.join([f'<option value="{value}">{value}</option>\n' for value in unique_values])

# Print or use html_options in your HTML document
print(html_options)
