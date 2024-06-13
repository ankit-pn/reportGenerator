from io import BytesIO
from fpdf import FPDF
from generate_plots import generate_plots
from generate_tables import generate_table,generate_increase_table
from datetime import datetime
import os


def put_plot(pdf,plot,txt):
    pdf.cell(200, 5, txt="", ln=True, align='L')
    pdf.cell(200, 10, txt=f"{txt}", ln=True, align='L')
    w = 190
    h = 100
    plot.seek(0)
    pdf.image(plot, w=w, h=h,x=5)


def generate_pdf(n=None):
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Arial","B", size=20)

    # Add a title
    pdf.cell(200, 10, txt="Data-Indexer Report", ln=True, align='C')

    pdf.set_font("Arial", size=10)
    # Add introduction
    pdf.cell(200, 10, txt="This report contains visualizations of indexed data over time.", ln=True, align='L')
    pdf.set_font("Arial","B", size=10)
    # pdf.cell(200, 10, txt="The following plots show the trends for different metrics.", ln=True, align='L')
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Text with timestamp
    text = f"Report Generated: This report was generated on {current_datetime}"

    pdf.cell(200, 10, txt=text, ln=True, align='L')
    # Add a horizontal line
    pdf.line(10, 28, 200, 30)

    pdf.set_font("Arial","B", size=14)
    pdf.cell(200, 5, txt="", ln=True, align='C')
    pdf.cell(200, 10, txt="Tabulated Results of Recent Process Runs (Last 10 Runs)", ln=True, align='C')
    # Generate plots
    # plots = generate_plots(n)

    # put_plot(pdf,plots[0],"Image PLot",5,50)
    # put_plot(pdf,plots[1],"Image PLot",5,160)

    # pdf.add_page()

    TABLE_DATA = generate_table(n=10)

    print("Table Data",TABLE_DATA)
    pdf.set_font("Arial", size=8)
    with pdf.table() as table:
        for data_row in TABLE_DATA:
            row = table.row()
            for datum in data_row:
                row.cell(str(datum))

    pdf.cell(200, 15, txt="", ln=True, align='C')
    pdf.set_font("Arial","B", size=14)
    pdf.cell(200, 10, txt="Delta Analysis of Recent Process Runs (Differences over Last 10 Runs)", ln=True, align='C')
    # pdf.line(10, 300, 200, 30)
    # pdf.cell(200, 2, txt="", ln=True, align='C')
    TABLE_DATA = generate_increase_table(n=10)

    print("Table Data",TABLE_DATA)
    pdf.set_font("Arial", size=8)
    with pdf.table() as table:
        for data_row in TABLE_DATA:
            row = table.row()
            for datum in data_row:
                row.cell(str(datum))

########################################
    plots = generate_plots(n)

    pdf.set_font("Arial","B", size=16)

    pdf.cell(200, 10, txt="", ln=True, align='C')
    pdf.cell(200, 20, txt="Trend Analysis of Data Indexed from Recent Process Runs", ln=True, align='C')

    # pdf.cell(200, 15, txt="", ln=True, align='C')
    pdf.set_font("Arial","B", size=14)
    # pdf.cell(200, 10, txt="Trend in Total Documents Processed Across All Process Runs", ln=True, align='C')
    put_plot(pdf, plots[5],"1.   Trend in Total Documents Processed Across All Process Runs")

    pdf.add_page()
    put_plot(pdf, plots[4],"2.   Trend in Text Messages Across All Process Runs")
    put_plot(pdf, plots[3],"3.   Trend in Forwarded Messages Count Across All Process Runs")
    pdf.add_page()
    put_plot(pdf, plots[1],"4.   Trend in Images Processed Across All Process Runs")
    put_plot(pdf, plots[6],"5.   Trend in Videos Processed Across All Process Runs")
    pdf.add_page()
    put_plot(pdf, plots[0],"6.   Trend in Audio Count Across All Process Runs")
    put_plot(pdf, plots[2],"7.   Trend in Links Processed Across All Process Runs")


        # Directory path
    directory = "generated_reports"

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    path = f"{directory}/Report_DI_{current_datetime}.pdf"
    pdf.output(path)

    print(f"PDF created successfully and saved as {path}")
    return path





generate_pdf()