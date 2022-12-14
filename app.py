from flask import Flask, Response, render_template, request

app = Flask('_name_',template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create_msg', methods=['GET', 'POST'])
def create_msg():
    n="""    URC NCC GP HQ {new}
    MADURAI{new}

    DAILY REPORT AS ON {}{new}

    DATE  {}{new}
    *********************{new}
    OPENING STOCK {new}
    LIQ  {}{new}
    GRO  {}{new}
    ***********************{new}
    DAILY SALE   {}{new}

    LIQ  {}{new}
    GRO  {}{new}
    ***********************{new}
    MONTHLY SALE {new}
    TOTAL {}{new}
    ********************{new}
    CLOSING STOCK {new}

    LIQ  {}{new}
    GRO  {}{new}
    ***********************{new}
    DIGITAL TRANSACTION  {} %{new}
    CASH TRANSACTION   {} %{new}

    *********************{new}
    BANK BALANCE {new}

    QD A/C  IOB{new}
    Rs {}{new}
    URC A/C {}{new}
    ***********************{new}
    BRONZE CARD  {}{new}
    LIQ  {}{new}
    GRO  {}{new}
    **********************{new}
    WARM REGARDS{new}

    UNIT RUN CANTEEN {new}

    GR HQ{new}"""
    # data=n.format('13.12.22','12.12.22','587271.56','7265824.29','12.12.22','43,835.00','2,58,559.00','12,67,901.00','547422.49','7018286.91','100','0','13,11,720.00','62,56,530.14','12.12.22','0','0',new="\n")
    
    # global dailyreport
    # global date 
    # global  oliq
    # global  ogro
    # global  dliq
    # global  dgro
    # global total 
    # global  cliq
    # global  cgro
    # global   dt 
    # global   ct 
    # global   rs 
    # global  urc 
    # global   bc 
    # global  liq 
    # global  gro 
    # global ds

    dailyreport=str(request.args.get('dailyreport'))
    date = str(request.args.get('date'))
    oliq = str(request.args.get('oliq'))
    ogro = str(request.args.get('ogro'))
    ds = str(request.args.get('ds'))
    dliq = str(request.args.get('dliq'))
    dgro = str(request.args.get('dgro'))
    total = str(request.args.get('total'))
    cliq = str(request.args.get('cliq'))
    cgro = str(request.args.get('cgro'))
    dt = str(request.args.get('dt'))
    ct = str(request.args.get('ct'))
    rs = str(request.args.get('rs'))
    urc = str(request.args.get('urc'))
    bc = str(request.args.get('bc'))
    liq = str(request.args.get('liq'))
    gro = str(request.args.get('gro'))
    
    data=n.format(dailyreport,date,oliq,ogro,ds,dliq,dgro,total,cliq,cgro,dt,ct,rs,urc,bc,liq,gro,new='\n')
    return Response(data,mimetype='text/plain')

app.run(debug=True)