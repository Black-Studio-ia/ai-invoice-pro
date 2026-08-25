# AI Invoice Pro

**AI-Powered Invoice Generator for Cross-Border E-commerce**

Generate professional PDF invoices in seconds. Built for sellers on Shopify, Amazon, AliExpress, eBay, and more.

![Invoice Demo](https://img.shields.io/badge/PDF-Generation-success) ![License](https://img.shields.io/badge/License-MIT-blue)

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/Black-Studio-ia/ai-invoice-pro.git
cd ai-invoice-pro
pip install -r requirements.txt
```

### Basic Usage

```python
from generator import InvoiceGenerator

# Create invoice
inv = InvoiceGenerator()

# Set your company info
inv.set_company(
    name="Your Company Name",
    email="you@company.com",
    address="123 Business St, City, Country",
    phone="+1 234 567 8900"
)

# Set client info
inv.set_client(
    name="Client Company",
    email="client@email.com",
    address="456 Client Ave, City, Country"
)

# Add items
inv.add_item("Product A", 2, 99.99)
inv.add_item("Service B", 1, 199.99)
inv.add_item("Shipping", 1, 15.00)

# Generate & Save
result = inv.save()
print(f"Invoice saved: {result}")
```

### Run Demo

```bash
python generator.py
```

This creates a sample invoice in the `invoices/` folder.

---

## 📖 Full Documentation

### InvoiceGenerator Class

#### Company & Client

```python
inv.set_company(name, email, address, phone="", logo="")
inv.set_client(name, email, address, phone="")
```

#### Invoice Details

```python
inv.set_invoice(
    number="INV-001",        # Invoice number
    date="2026-01-01",       # Issue date (default: today)
    due_date="2026-02-01",   # Due date
    notes="Payment terms",   # Notes
    currency="USD"           # Currency code
)
```

#### Add Items

```python
inv.add_item(description, quantity, price)
```

#### Get Totals

```python
inv.get_total()                    # Subtotal
inv.get_tax(rate=10)              # Tax amount
inv.get_grand_total(tax_rate=10)   # Total with tax
```

#### Generate Output

```python
inv.generate_html()           # Returns HTML string
inv.generate_pdf("file.pdf")  # Save as PDF
inv.save()                    # Save both HTML and PDF
```

---

## 🌐 Web App (Flask)

Run the web interface:

```bash
python app.py
```

Open `http://localhost:5000` in your browser.

---

## 💡 Use Cases

- **E-commerce sellers** - Generate invoices for orders
- **Freelancers** - Bill clients professionally
- **Dropshipping** - Automate invoice creation
- **SaaS companies** - Recurring billing invoices

---

## 💰 Pricing & Support

This is the **open-source version** (free, MIT License).

**Need more features?**

| Feature | Free | Pro |
|---------|------|-----|
| PDF Generation | ✅ | ✅ |
| HTML Invoices | ✅ | ✅ |
| Multi-Currency | ✅ | ✅ |
| Bulk Generation | ❌ | ✅ |
| API Access | ❌ | ✅ |
| Custom Templates | ❌ | ✅ |
| Priority Support | ❌ | ✅ |

**Contact for Pro version:**
- 📧 Email: ia.creative.tn@gmail.com

---

## 📜 License

MIT License - Free for personal and commercial use.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first.

---

**Made with ❤️ by Black Studio**
