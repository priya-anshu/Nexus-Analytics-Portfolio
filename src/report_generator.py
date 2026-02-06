"""
Module: report_generator.py
Description: Generates a COMPLETE documentation PDF.
Fixes: Handles Unicode errors by stripping unsupported characters.
"""
from fpdf import FPDF
import os
from datetime import datetime

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        # Use simple text, no emojis
        self.cell(0, 10, 'Nexus Enterprise Analytics - Documentation', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def safe_cell(self, w, h, text, border=0, ln=0, align='', fill=False):
        """Wrapper to sanitize text before writing to cell"""
        # Encode to latin-1, replacing errors with '?'
        sanitized = text.encode('latin-1', 'replace').decode('latin-1')
        self.cell(w, h, sanitized, border, ln, align, fill)

    def safe_multi_cell(self, w, h, text, border=0, align='J', fill=False):
        """Wrapper to sanitize text before writing to multi_cell"""
        sanitized = text.encode('latin-1', 'replace').decode('latin-1')
        self.multi_cell(w, h, sanitized, border, align, fill)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.safe_cell(0, 10, title, 0, 1, 'L', True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.safe_multi_cell(0, 6, body)
        self.ln()

    def add_image(self, image_path, title):
        if os.path.exists(image_path):
            self.set_font('Arial', 'B', 10)
            self.safe_cell(0, 10, title, 0, 1, 'L')
            # Resize image to fit page width (190mm)
            self.image(image_path, x=10, w=190)
            self.ln(5)
        else:
            self.set_text_color(255, 0, 0)
            self.safe_cell(0, 10, f"Image missing: {image_path}", 0, 1)
            self.set_text_color(0, 0, 0)

def generate_pdf_report():
    print("📄 GENERATING COMPREHENSIVE DOCUMENTATION PDF...")
    pdf = PDFReport()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # --- PAGE 1: TITLE & OVERVIEW ---
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 40, '', 0, 1)
    pdf.safe_cell(0, 20, 'Nexus Analytics Portfolio', 0, 1, 'C')
    pdf.set_font('Arial', '', 14)
    pdf.safe_cell(0, 10, 'Full Internship Documentation (Task 2)', 0, 1, 'C')
    pdf.safe_cell(0, 10, f'Date: {datetime.now().strftime("%Y-%m-%d")}', 0, 1, 'C')
    pdf.ln(20)
    
    pdf.chapter_title('Project Overview')
    pdf.chapter_body(
        "The Nexus Retail Analytics System is a production-grade Python application designed to process, analyze, "
        "and visualize data across 5 distinct domains: Retail, Education, Healthcare, Finance, and Weather.\n\n"
        "Unlike basic scripts, this project uses a modular architecture to ensure scalability and reproducibility. "
        "It features automated data pipelines, statistical validation (T-Tests, ANOVA), and Machine Learning forecasting models."
    )

    # --- PAGE 2: TECHNICAL SETUP ---
    pdf.add_page()
    pdf.chapter_title('1. Setup & Installation Instructions')
    pdf.chapter_body(
        "Prerequisites: Python 3.8+, pip, git.\n\n"
        "Step 1: Clone the Repository\n"
        "   git clone https://github.com/priya-anshu/Nexus-Analytics-Portfolio\n"
        "   cd Nexus-Analytics-Portfolio\n\n"
        "Step 2: Install Dependencies\n"
        "   pip install -r requirements.txt\n\n"
        "Step 3: Run the Application\n"
        "   python main.py\n\n"
        "Note: The system automatically generates synthetic data for Projects 2-5 if CSV files are missing."
    )

    pdf.chapter_title('2. Code Structure')
    pdf.chapter_body(
        "The project follows a 'Headless' architecture suitable for production deployment:\n\n"
        "data/raw/             -> Input CSV files (Immutable)\n"
        "reports/figures/      -> Generated Visualization Assets\n"
        "src/                  -> Source Code Modules\n"
        "   data_loader.py    -> Data Ingestion Engine\n"
        "   features.py       -> Feature Engineering Logic\n"
        "   forecasting.py    -> ML Sales Prediction Model\n"
        "   statistics.py     -> Statistical Testing Suite\n"
        "   extended_projects.py -> Logic for Projects 2-5\n"
        "   report_generator.py  -> PDF Documentation Engine\n"
        "main.py               -> Master Execution Script\n"
        "README.md             -> GitHub Documentation"
    )

    pdf.chapter_title('3. Technical Requirements Met')
    pdf.chapter_body(
        "- [x] 5 Distinct Projects: Retail, Education, Healthcare, Finance, Weather.\n"
        "- [x] Data Manipulation: Used Pandas for cleaning, merging, and pivoting.\n"
        "- [x] Visualizations: Generated 15+ Charts (Heatmaps, Regressions, Area Plots).\n"
        "- [x] Business Insights: Derived actionable metrics (Volatilty, Recovery Rates, P-Values).\n"
        "- [x] Professional Packaging: Auto-generated PDF documentation and organized GitHub repo."
    )

    # --- PAGE 3+: VISUAL EVIDENCE ---
    pdf.add_page()
    pdf.chapter_title('4. Project 1: Retail Analytics (Flagship)')
    pdf.chapter_body("Objective: Forecast revenue and analyze customer behavior using AI and Statistics.")
    pdf.add_image('reports/figures/01_retail_heatmap.png', 'Fig 1.1: Peak Traffic Analysis')
    pdf.add_image('reports/figures/01_retail_forecast.png', 'Fig 1.2: AI Sales Forecast (Linear Regression)')

    pdf.add_page()
    pdf.chapter_title('5. Project 2: Education Analytics')
    pdf.chapter_body("Objective: Identify factors influencing student exam performance.")
    pdf.add_image('reports/figures/02_edu_regression.png', 'Fig 2.1: Study Hours vs Score')
    pdf.add_image('reports/figures/02_edu_method_perf.png', 'Fig 2.2: Performance by Study Method')

    pdf.add_page()
    pdf.chapter_title('6. Project 3: Healthcare Epidemiology')
    pdf.chapter_body("Objective: Visualize epidemic spread, recovery, and mortality rates.")
    pdf.add_image('reports/figures/03_health_curve.png', 'Fig 3.1: Infection vs Recovery Curve')
    pdf.add_image('reports/figures/03_health_cumulative.png', 'Fig 3.2: Cumulative Caseload')

    pdf.add_page()
    pdf.chapter_title('7. Project 4: Financial Analysis')
    pdf.chapter_body("Objective: Assess market risk and asset volatility.")
    pdf.add_image('reports/figures/04_fin_price_trend.png', 'Fig 4.1: Asset Price History')
    pdf.add_image('reports/figures/04_fin_risk_dist.png', 'Fig 4.2: Risk Distribution Profile')

    pdf.add_page()
    pdf.chapter_title('8. Project 5: Weather Patterns')
    pdf.chapter_body("Objective: Track seasonal climatic changes and correlations.")
    pdf.add_image('reports/figures/05_weath_temp_cycle.png', 'Fig 5.1: Annual Temperature Cycle')
    pdf.add_image('reports/figures/05_weath_correlation.png', 'Fig 5.2: Climatic Variable Correlation')

    # Save
    out_path = 'Nexus_Portfolio_Report.pdf'
    pdf.output(out_path)
    print(f"✅ DOCUMENTATION READY: {out_path}")

if __name__ == "__main__":
    generate_pdf_report()