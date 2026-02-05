"""
Module: report_generator.py
Description: Generates a professional PDF portfolio from analysis results.
"""
from fpdf import FPDF
import os
from datetime import datetime

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Nexus Retail Analytics - Executive Portfolio', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_image(self, image_path, title):
        if os.path.exists(image_path):
            self.set_font('Arial', 'B', 10)
            self.cell(0, 10, title, 0, 1, 'L')
            # Resize image to fit page width
            self.image(image_path, x=10, w=190)
            self.ln(5)
        else:
            self.set_text_color(255, 0, 0)
            self.cell(0, 10, f"Error: Image not found ({image_path})", 0, 1)
            self.set_text_color(0, 0, 0)

def generate_pdf_report():
    print("📄 GENERATING FINAL PDF PORTFOLIO...")
    pdf = PDFReport()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # --- TITLE PAGE ---
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 60, '', 0, 1)  # Spacer
    pdf.cell(0, 20, 'Nexus Analytics Portfolio', 0, 1, 'C')
    pdf.set_font('Arial', '', 14)
    pdf.cell(0, 10, 'Month 2 Internship Deliverable', 0, 1, 'C')
    pdf.cell(0, 10, f'Generated: {datetime.now().strftime("%Y-%m-%d")}', 0, 1, 'C')
    pdf.ln(20)
    pdf.set_font('Arial', 'I', 12)
    pdf.multi_cell(0, 10, "This document contains the executive summaries and visual analysis for 5 distinct domains: Retail, Education, Healthcare, Finance, and Weather.\n\nAuthor: Data Analyst Intern")

    # --- PROJECT 1: RETAIL ---
    pdf.add_page()
    pdf.chapter_title('1. Retail Analytics (Flagship Project)')
    pdf.chapter_body(
        "Objective: Analyze sales trends and forecast revenue.\n"
        "Key Finding: No significant spending difference between Member vs. Normal customers (T-Test p>0.05).\n"
        "AI Model: Linear Regression achieved high accuracy in predicting daily sales."
    )
    pdf.add_image('reports/figures/01_retail_heatmap.png', 'Fig 1.1: Peak Business Hours')
    pdf.add_image('reports/figures/01_retail_forecast.png', 'Fig 1.2: AI Sales Forecast (Actual vs Predicted)')

    # --- PROJECT 2: EDUCATION ---
    pdf.add_page()
    pdf.chapter_title('2. Education Analytics')
    pdf.chapter_body("Objective: Correlate study habits with exam performance.")
    pdf.add_image('reports/figures/02_edu_regression.png', 'Fig 2.1: Study Hours vs Score Regression')
    pdf.add_image('reports/figures/02_edu_method_perf.png', 'Fig 2.2: Performance by Study Method')

    # --- PROJECT 3: HEALTHCARE ---
    pdf.add_page()
    pdf.chapter_title('3. Healthcare Epidemiology')
    pdf.chapter_body("Objective: Track epidemic spread and recovery rates.")
    pdf.add_image('reports/figures/03_health_curve.png', 'Fig 3.1: Infection vs Recovery Curve')
    pdf.add_image('reports/figures/03_health_cumulative.png', 'Fig 3.2: Cumulative Caseload')

    # --- PROJECT 4: FINANCE ---
    pdf.add_page()
    pdf.chapter_title('4. Financial Analysis')
    pdf.chapter_body("Objective: Analyze asset volatility and risk.")
    pdf.add_image('reports/figures/04_fin_price_trend.png', 'Fig 4.1: Asset Price Trend')
    pdf.add_image('reports/figures/04_fin_risk_dist.png', 'Fig 4.2: Daily Return Distribution (Risk)')

    # --- PROJECT 5: WEATHER ---
    pdf.add_page()
    pdf.chapter_title('5. Weather & Climate')
    pdf.chapter_body("Objective: Identify seasonal temperature and rainfall patterns.")
    pdf.add_image('reports/figures/05_weath_temp_cycle.png', 'Fig 5.1: Annual Temperature Cycle')
    pdf.add_image('reports/figures/05_weath_correlation.png', 'Fig 5.2: Climatic Correlations')

    # Save
    out_path = 'Nexus_Portfolio_Report.pdf'
    pdf.output(out_path)
    print(f"✅ PDF Saved: {out_path}")

if __name__ == "__main__":
    generate_pdf_report()