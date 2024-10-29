from fpdf import FPDF

# PDF CONTENT
sample_content = """
Welcome to Gourmet Delights!

About Us:
Gourmet Delights is a fine dining restaurant known for its exceptional cuisine and exquisite ambiance. We pride 
ourselves on serving delicious dishes made from the freshest ingredients.

Menu Highlights:
- Appetizers: Caesar Salad, Shrimp Cocktail, Truffle Fries
- Main Courses: Grilled Salmon, Beef Wellington, Vegetarian Lasagna
- Desserts: Chocolate Lava Cake, Creme Brulee, New York Cheesecake
- Drinks: Wine, Cocktails, Fresh Juices, Sparkling Water

Operating Hours:
- Monday to Friday: 11:00 AM - 10:00 PM
- Saturday & Sunday: 9:00 AM - 11:00 PM

Special Services:
- Private Dining: Reserve our private room for exclusive gatherings and events.
- Catering Services: Enjoy Gourmet Delights at home or at your events. Contact us for more details.
- Online Reservations: Book a table through our website or give us a call.

Contact Us:
- Phone: (555) 123-4567
- Email: reservations@gourmetdelights.com
- Address: 123 Culinary Lane, Food City, FC 12345

We look forward to serving you a memorable dining experience at Gourmet Delights!
"""

# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Gourmet Delights Restaurant Information", ln=True, align="C")
pdf.set_font("Arial", "", 12)
pdf.ln(10)
pdf.multi_cell(0, 10, sample_content)

# Save PDF
pdf.output("gourmet_delights_knowledge_base.pdf")
