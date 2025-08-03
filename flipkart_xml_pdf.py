from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "B", 14)
        self.cell(0, 10, "XML Assignment - Flipkart Database", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, label):
        self.set_font("DejaVu", "B", 12)
        self.set_text_color(0)
        self.cell(0, 10, label, ln=True)
        self.ln(1)

    def add_code_block(self, text):
        self.set_font("DejaVu", "", 9)
        self.set_fill_color(245, 245, 245)
        for line in text.strip().splitlines():
            self.multi_cell(0, 5, line, border=0, fill=1)
        self.ln(2)

# Initialize PDF
pdf = PDF()
pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
pdf.add_font('DejaVu', 'B', 'DejaVuSans.ttf', uni=True)
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Add Question
pdf.chapter_title("Q) Write an XML program for Flipkart database.")

# Chart
pdf.chapter_title("I) CHART:")
chart = '''
Flipkart
├── Home
│   ├── ForYou
│   │   ├── Item (name, price, brand)
│   ├── TopDeals
│   │   ├── Item (name, price, brand)
│   └── RecentlyViewed
│       ├── Item (name, price, brand)
├── Fashion
│   ├── Men
│   │   ├── Item (name, price, brand)
│   ├── Women
│   │   ├── Item (name, price, brand)
│   └── Kids
│       ├── Item (name, price, brand)
├── Electronics
│   ├── Mobiles
│   │   ├── Item (name, price, brand)
│   ├── Laptops
│   │   ├── Item (name, price, brand)
│   └── Accessories
│       ├── Item (name, price, brand)
└── Groceries
    ├── Vegetables
    │   ├── Item (name, price, brand)
    ├── Snacks
    │   ├── Item (name, price, brand)
    └── Beverages
        ├── Item (name, price, brand)
'''
pdf.add_code_block(chart)

# Input XML
pdf.chapter_title("II) INPUT XML:")
with open("flipkart_input.xml", "r", encoding="utf-8") as f:
    input_xml = f.read()
pdf.add_code_block(input_xml)

# Output XML
pdf.chapter_title("III) OUTPUT XML (Browser View):")

# List of image files showing browser-rendered XML with arrows
image_files = [
    "browser_output_1.png",
    "browser_output_2.png",
    "browser_output_3.png",
    "browser_output_4.png",
    "browser_output_5.png"
]

# Add each image to the PDF
for img in image_files:
    pdf.image(img, x=10, w=190)  # You can adjust x or w if layout breaks
    pdf.ln(5)


# Save PDF
pdf.output("flipkart_assignment_output.pdf")
