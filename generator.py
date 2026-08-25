"""
AI Invoice Pro - Main Application
Professional Invoice Generator for Cross-Border E-commerce
"""

import os
import json
from datetime import datetime
from pathlib import Path

# PDF Generation
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False

class InvoiceGenerator:
    """AI-Powered Invoice Generator"""
    
    def __init__(self):
        self.company = {}
        self.client = {}
        self.items = []
        self.invoice_number = ""
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.due_date = ""
        self.notes = ""
        self.currency = "USD"
        self.language = "en"
    
    def set_company(self, name, email, address, phone="", logo=""):
        self.company = {
            "name": name,
            "email": email,
            "address": address,
            "phone": phone,
            "logo": logo
        }
    
    def set_client(self, name, email, address, phone=""):
        self.client = {
            "name": name,
            "email": email,
            "address": address,
            "phone": phone
        }
    
    def set_invoice(self, number, date="", due_date="", notes="", currency="USD"):
        self.invoice_number = number
        self.date = date or self.date
        self.due_date = due_date
        self.notes = notes
        self.currency = currency
    
    def add_item(self, description, quantity, price):
        self.items.append({
            "description": description,
            "quantity": quantity,
            "price": price,
            "total": quantity * price
        })
    
    def get_total(self):
        return sum(item["total"] for item in self.items)
    
    def get_tax(self, rate=0):
        return self.get_total() * (rate / 100)
    
    def get_grand_total(self, tax_rate=0):
        return self.get_total() + self.get_tax(tax_rate)
    
    def generate_html(self):
        """Generate HTML invoice"""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Invoice #{self.invoice_number}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; color: #333; }}
        .header {{ display: flex; justify-content: space-between; margin-bottom: 40px; }}
        .company {{ font-size: 24px; font-weight: bold; color: #2563eb; }}
        .invoice-title {{ font-size: 36px; font-weight: bold; color: #2563eb; }}
        .details {{ display: flex; justify-content: space-between; margin-bottom: 30px; }}
        .details div {{ width: 45%; }}
        .details h3 {{ color: #666; border-bottom: 2px solid #2563eb; padding-bottom: 5px; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 30px; }}
        th {{ background: #2563eb; color: white; padding: 12px; text-align: left; }}
        td {{ padding: 12px; border-bottom: 1px solid #ddd; }}
        .total {{ text-align: right; font-size: 24px; font-weight: bold; color: #2563eb; }}
        .notes {{ margin-top: 40px; padding: 20px; background: #f5f5f5; border-radius: 5px; }}
        .footer {{ margin-top: 40px; text-align: center; color: #666; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="header">
        <div class="company">{self.company.get('name', 'Company')}</div>
        <div class="invoice-title">INVOICE</div>
    </div>
    
    <div class="details">
        <div>
            <h3>FROM</h3>
            <strong>{self.company.get('name', '')}</strong><br>
            {self.company.get('address', '')}<br>
            {self.company.get('email', '')}<br>
            {self.company.get('phone', '')}
        </div>
        <div>
            <h3>BILL TO</h3>
            <strong>{self.client.get('name', '')}</strong><br>
            {self.client.get('address', '')}<br>
            {self.client.get('email', '')}<br>
            {self.client.get('phone', '')}
        </div>
    </div>
    
    <table>
        <thead>
            <tr>
                <th>Description</th>
                <th>Quantity</th>
                <th>Price ({self.currency})</th>
                <th>Total ({self.currency})</th>
            </tr>
        </thead>
        <tbody>
"""
        
        for item in self.items:
            html += f"""
            <tr>
                <td>{item['description']}</td>
                <td>{item['quantity']}</td>
                <td>{item['price']:.2f}</td>
                <td>{item['total']:.2f}</td>
            </tr>
"""
        
        html += f"""
        </tbody>
    </table>
    
    <div class="total">
        Total: {self.currency} {self.get_total():.2f}
    </div>
    
    <div class="notes">
        <strong>Notes:</strong><br>
        {self.notes or 'Thank you for your business!'}
    </div>
    
    <div class="footer">
        Invoice #{self.invoice_number} | Generated on {self.date}
    </div>
</body>
</html>
"""
        return html
    
    def generate_pdf(self, output_path):
        """Generate PDF invoice"""
        if not PDF_SUPPORT:
            return "PDF support not available. Install reportlab: pip install reportlab"
        
        doc = SimpleDocTemplate(output_path, pagesize=A4)
        styles = getSampleStyleSheet()
        elements = []
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=36,
            textColor=colors.HexColor('#2563eb'),
            spaceAfter=30
        )
        elements.append(Paragraph("INVOICE", title_style))
        
        # Company info
        elements.append(Paragraph(f"<b>{self.company.get('name', '')}</b>", styles['Normal']))
        elements.append(Paragraph(self.company.get('address', ''), styles['Normal']))
        elements.append(Spacer(1, 20))
        
        # Client info
        elements.append(Paragraph(f"<b>Bill To:</b> {self.client.get('name', '')}", styles['Normal']))
        elements.append(Paragraph(self.client.get('address', ''), styles['Normal']))
        elements.append(Spacer(1, 20))
        
        # Items table
        data = [['Description', 'Qty', 'Price', 'Total']]
        for item in self.items:
            data.append([
                item['description'],
                str(item['quantity']),
                f"{item['price']:.2f}",
                f"{item['total']:.2f}"
            ])
        
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563eb')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 20))
        
        # Total
        elements.append(Paragraph(
            f"<b>Total: {self.currency} {self.get_total():.2f}</b>",
            styles['Heading2']
        ))
        
        doc.build(elements)
        return f"PDF generated: {output_path}"
    
    def save(self, output_dir="invoices"):
        """Save invoice as HTML and PDF"""
        Path(output_dir).mkdir(exist_ok=True)
        
        # Save HTML
        html_path = os.path.join(output_dir, f"invoice_{self.invoice_number}.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(self.generate_html())
        
        # Save PDF
        pdf_path = os.path.join(output_dir, f"invoice_{self.invoice_number}.pdf")
        result = self.generate_pdf(pdf_path)
        
        return {
            "html": html_path,
            "pdf": pdf_path if PDF_SUPPORT else "N/A",
            "result": result
        }


def demo():
    """Demo invoice generation"""
    inv = InvoiceGenerator()
    
    inv.set_company(
        name="AI Trading Co.",
        email="contact@aitrading.com",
        address="123 Tech Street, Shenzhen, China",
        phone="+86 123 4567 8900"
    )
    
    inv.set_client(
        name="Global Imports LLC",
        email="billing@globalimports.com",
        address="456 Commerce Ave, New York, USA",
        phone="+1 212 555 0123"
    )
    
    inv.set_invoice(
        number="INV-2026-001",
        notes="Payment due within 30 days. Thank you for your business!"
    )
    
    inv.add_item("AI Software License", 1, 999.00)
    add_item("Premium Support (1 year)", 1, 199.00)
    inv.add_item("Custom Integration", 5, 150.00)
    
    result = inv.save()
    print(f"Invoice saved: {result}")


if __name__ == "__main__":
    demo()
