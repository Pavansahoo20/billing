from flask import Flask, render_template, request

app = Flask(__name__)

# Available menu items with prices
MENU = {
    "CR": 60, "VSC": 60, "TS": 50, "MS": 70, "MCS": 80, "CS": 60, "MBS": 90, "CSC": 90, "HS": 90, "CM": 90,
    "CP": 200, "CDS": 250, "CK": 120, "CC": 180, "DC": 200, "C65": 120, "CL": 150, "CT5": 200, "CMA": 230, "CT": 200,
    "PB": 220, "MB": 200, "CDB": 120, "CF": 120, "BC": 200, "MKB": 250, "MUB": 300, "FB": 250, "PRB": 250, "MLA": 300,
    "R": 30, "RR": 40, "BR": 50, "BN": 40, "N": 40, "K": 50, "BK": 50, "AK": 50, "C": 30, "P": 20,
    "CO": 40, "TH": 40, "S": 40, "VM": 70, "BC": 70, "WB": 20
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        customer_name = request.form['name']
        order_type = request.form['order_type']
        items = request.form.getlist('items')
        quantities = request.form.getlist('quantities')

        bill_items = []
        total_price = 0
        for item, qty in zip(items, quantities):
            qty = int(qty)
            price = MENU.get(item, 0) * qty
            total_price += price
            bill_items.append((item, qty, price))
        
        gst = total_price * 0.18
        final_amount = total_price + gst
        
        return render_template('bill.html', name=customer_name, order_type=order_type, bill_items=bill_items, total_price=total_price, gst=gst, final_amount=final_amount)
    
    return render_template('index.html', menu=MENU)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
 
