from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a cell
pdf.cell(200, 10, txt="Welcome to FPDF tutorial!", ln=True, align='C')

# Add another cell
pdf.cell(200, 10, txt="This is line number 1.", ln=True, align='L')
pdf.cell(200, 10, txt="This is line number 2.", ln=True, align='L')

# Add a horizontal line
pdf.line(10, 30, 200, 30)

# Output the PDF to a file
pdf.output("example.pdf")

print("PDF created successfully.")
