# AI Invoice Pro

**Professional Invoice Generator for Cross-Border E-commerce**

Generate professional PDF invoices in seconds. Built for sellers on Shopify, Amazon, AliExpress, eBay, and more.

![PDF](https://img.shields.io/badge/PDF-Generation-success) ![License](https://img.shields.io/badge/License-MIT-blue) ![Python](https://img.shields.io/badge/Python-3.8+-green)

---

## 📦 Versions

| Feature | Free (GitHub) | Pro ($29.99) |
|---------|---------------|--------------|
| PDF Generation | ✅ | ✅ |
| HTML Invoices | ✅ | ✅ |
| Multi-Currency | ✅ | ✅ |
| Basic Templates | 3 | 10+ |
| Shopify API | ❌ | ✅ |
| Amazon API | ❌ | ✅ |
| WooCommerce API | ❌ | ✅ |
| Bulk Generation | ❌ | ✅ |
| Custom Templates | ❌ | ✅ |
| Priority Support | ❌ | ✅ |

---

## 🚀 Free Version (GitHub)

### Installation

```bash
git clone https://github.com/Black-Studio-ia/ai-invoice-pro.git
cd ai-invoice-pro
pip install -r requirements.txt
```

### Quick Start

```python
from generator import InvoiceGenerator

# Create invoice
inv = InvoiceGenerator()

# Your company
inv.set_company(
    name="Your Company",
    email="you@company.com",
    address="123 Business St, City, Country"
)

# Your client
inv.set_client(
    name="Client Name",
    email="client@email.com",
    address="456 Client Ave, City, Country"
)

# Add items
inv.add_item("Product A", 2, 99.99)
inv.add_item("Service B", 1, 199.99)

# Generate
result = inv.save()
print(f"Invoice saved: {result}")
```

### Run Demo

```bash
python generator.py
```

---

## 💰 Pro Version ($29.99)

**Get the full version with API integrations:**

- 🔌 **Shopify Integration** - Auto-generate invoices for orders
- 📦 **Amazon Integration** - FBA invoice automation
- 🛒 **WooCommerce Integration** - WordPress e-commerce
- 📊 **Bulk Generation** - Generate 1000+ invoices at once
- 🎨 **Custom Templates** - Your branding, your style
- 📧 **Priority Support** - Direct email support

### How to Purchase

1. **Pay $29.99 USDT (TRC-20)**
2. **Email:** ia.creative.tn@gmail.com
3. **Receive:** License key + Pro code + Documentation

### Pro API Usage

```python
from ai_invoice_pro import ShopifyIntegration, AmazonIntegration

# Shopify
shopify = ShopifyIntegration(
    shop_url="your-store.myshopify.com",
    api_key="your-api-key"
)

# Auto-generate invoice for order
invoice = shopify.generate_invoice(order_id="12345")
invoice.save()

# Amazon
amazon = AmazonIntegration(
    seller_id="YOUR_SELLER_ID",
    auth_token="YOUR_AUTH_TOKEN"
)

# Bulk generate invoices
invoices = amazon.bulk_generate(
    start_date="2026-01-01",
    end_date="2026-01-31"
)
```

---

## 📖 Documentation

### InvoiceGenerator Class

```python
# Initialize
inv = InvoiceGenerator()

# Company info
inv.set_company(name, email, address, phone="", logo="")

# Client info  
inv.set_client(name, email, address, phone="")

# Invoice details
inv.set_invoice(number, date="", due_date="", notes="", currency="USD")

# Add items
inv.add_item(description, quantity, price)

# Get totals
inv.get_total()                    # Subtotal
inv.get_tax(rate=10)              # Tax amount
inv.get_grand_total(tax_rate=10)  # Total with tax

# Generate
inv.generate_html()           # Returns HTML string
inv.generate_pdf("file.pdf")  # Save as PDF
inv.save()                    # Save both to invoices/ folder
```

---

## 💡 Use Cases

- **E-commerce sellers** - Generate invoices for every order
- **Freelancers** - Bill clients professionally  
- **Dropshipping** - Automate invoice creation
- **SaaS companies** - Recurring billing invoices
- **Cross-border trade** - Multi-currency support

---

## 📞 Contact & Purchase

- 📧 **Email:** ia.creative.tn@gmail.com
- 💰 **Payment:** USDT (TRC-20) only
- 💬 **Support:** Included with Pro version

---

## 📜 License

- **Free version:** MIT License (personal use)
- **Pro version:** Commercial license (after purchase)

---

**© 2026 Black Studio**
