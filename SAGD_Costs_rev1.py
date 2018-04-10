from bokeh.plotting import figure, curdoc
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource
from bokeh.layouts import widgetbox
from bokeh.models import BoxAnnotation
from bokeh.layouts import layout
from bokeh.models import Slider, Label, Select
from bokeh.models.widgets import Div
import numpy as np
import pandas as pd
import pandas_datareader.data as web


# CAPEX GRAPH
####################################
# Get the current slider values
# Engineering
a = 100000000
# Equipment
b = 300000000
# Bulk Materials
c = 280000000
# Indirects
d = 230000000
# Labour
e = 390000000

# Calculate Top & Bottom
ab = 0
at = a
bb = a
bt = a + b
cb = a + b
ct = a + b + c
db = a + b + c
dt = a + b + c + d
eb = a + b + c + d
et = a + b + c + d + e


# New sources
engsource = ColumnDataSource(data=dict(x=[ab], y=[at], desc=['Engineering'],
                             info=[at]))
equipsource = ColumnDataSource(data=dict(x=[bb], y=[bt], desc=['Equipment'],
                               info=[bt-at]))
bulksource = ColumnDataSource(data=dict(x=[cb], y=[ct],
                              desc=['Bulk Materials'], info=[ct-bt]))
indisource = ColumnDataSource(data=dict(x=[db], y=[dt], desc=['Indirects'],
                              info=[dt-ct]))
labsource = ColumnDataSource(data=dict(x=[eb], y=[et], desc=['Labour'],
                             info=[et-dt]))


# HoverTool Label
phover = HoverTool(
                   tooltips=[
                    ('Item', '@desc'),
                    ('Cost', '@info{$ 0.00 a}'),
                     ],
                   )


# Other Tools
TOOLS = 'box_zoom, box_select, resize, reset'


# Figure
p = figure(title="Capital Costs Breakdown", title_location="above",
           plot_width=300, plot_height=300, x_range=(-2, 2),
           tools=[TOOLS, phover])


# Plots
engbar = p.vbar(x=0, width=2, bottom='x',
                top='y', alpha=0.75, color="darkslategrey",
                legend="Engineering", source=engsource)

equipbar = p.vbar(x=0, width=2, bottom='x',
                  top='y', alpha=0.75, color="teal", legend="Equipment",
                  source=equipsource)

bulkbar = p.vbar(x=0, width=2, bottom='x',
                 top='y', alpha=0.75, color="cyan", legend="Bulk Materials",
                 source=bulksource)

indibar = p.vbar(x=0, width=2, bottom='x',
                 top='y', alpha=0.75, color="powderblue", legend="Indirects",
                 source=indisource)

labbar = p.vbar(x=0, width=2, bottom='x',
                top='y', alpha=0.75, color="lavender", legend="Labour",
                source=labsource)


# Format
p.yaxis[0].formatter = NumeralTickFormatter(format="$0,000")
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None


# Set up widgets
eng_slider = Slider(start=0, end=500000000,
                    value=100000000, step=5000000, title="Engineering $")
equip_slider = Slider(start=0, end=500000000,
                      value=300000000, step=5000000, title="Equipment $")
bulk_slider = Slider(start=0, end=500000000,
                     value=280000000, step=5000000, title="Bulk_Materials $")
indi_slider = Slider(start=0, end=500000000,
                     value=230000000, step=5000000, title="Indirects $")
lab_slider = Slider(start=0, end=500000000,
                    value=390000000, step=5000000, title="Labour $")
time_select = Select(title="Years To First Steam:", value='3',
                     options=['2.5', '3', '4'])

# PAYBACK GRAPH
####################################


# Data
facilitysz = 40000
# Exchange = web.get_quote_yahoo('CAD=X')
# Exchangert = Exchange['last'][0]
Oil_Price = 45
# Oil_Price_CAD = Oil_Price * Exchangert
Oil_Price_CAD = Oil_Price
Fuel = 4
Opp_Cost = 10
Sus_Cap = 4
Royalties = 2
Taxes = 3.8
Emission_Comp = 0.3
Transport = 7
# Other = 1
Uptime = 0.95
Construction_time = 3
Net = Uptime * (365 * (facilitysz * (Oil_Price_CAD - (Fuel + Opp_Cost +
                                             Sus_Cap + Royalties + Taxes + Emission_Comp + Transport))))
Year = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Construction Calc
con_var = Construction_time - 1
if Construction_time == 3:
    # Return Calculation
    y0 = -et / 2
    y1 = -et / 2
    y2 = Net * 0.75
    y3 = Net
    y4 = Net
    y5 = Net
elif Construction_time == 4:
    y0 = -et / 2
    y1 = -et / 2
    y2 = Net * 0.25
    y3 = Net * 0.75
    y4 = Net
    y5 = Net
elif Construction_time == 2.5:
    y0 = -et / 2
    y1 = -et / 2
    y2 = Net
    y3 = Net
    y4 = Net
    y5 = Net

y6 = Net
y7 = Net
y8 = Net
y9 = Net
y10 = Net
y11 = Net
y12 = Net
y13 = Net
y14 = Net
y15 = Net
y16 = Net
y17 = Net
y18 = Net
y19 = Net
y20 = Net
y21 = Net
y22 = Net
y23 = Net
y24 = Net
y25 = Net
y26 = Net
y27 = Net
y28 = Net
y29 = Net
y30 = Net
# Payback data list
Payback = [y0, y0 + y1, y0 + y1 + y2, y0 + y1 + y2 + y3, y0 + y1 + y2 + y3 + y4, y0 + y1 + y2 + y3 + y4 + y5, y0 + y1 + y2 + y3 + y4 + y5 + y6,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
           y8 + y9, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 +
           y10, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
           y8 + y9 + y10 + y11 + y12 + y13, y0 + y1 + y2 + y3 + y4 +
           y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 +
           y10 + y11 + y12 + y13 + y14 + y15 + y16, y0 + y1 + y2 + y3 + y4 + y5 +
           y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 +
           y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19, y0 + y1 + y2 + y3 + y4 + y5 + y6 +
           y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21, y0 +
           y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 +
           y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 +
           y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
           y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 +
           y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 +
           y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 +
           y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 +
           y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y30]


# New sources
returnsource = ColumnDataSource(dict(x=Year, y=Payback))


# HoverTool Label
Thover = HoverTool(mode='vline',
                   tooltips=[
                    ('Return', '@y{$ 0.00 a}'),
                   ]
                   )


# Other Tools
TOOLS = 'box_zoom, box_select, resize, reset'


# Plot
T = figure(title="Return On Investment", title_location="above",
           plot_width=300, plot_height=300, tools=[TOOLS, Thover])
T.line(x='x', y='y', color="teal", line_width=4,
       alpha=0.75, source=returnsource)


# Format
T.yaxis[0].formatter = NumeralTickFormatter(format="$0,000")
T.add_layout(BoxAnnotation(bottom=0, fill_alpha=0.2, fill_color='teal'))
T.add_layout(BoxAnnotation(top=0, fill_alpha=0.2, fill_color='red'))
T.xgrid.grid_line_color = None
T.ygrid.grid_line_color = 'whitesmoke'


# Set up widgets
oil_slider = Slider(start=20, end=100,
                    value=45, step=1, title="Realized Bitumen Price CAD/bbl")
fuel_slider = Slider(start=0, end=20,
                     value=4, step=1, title="Fuel Cost $/bbl")
opp_slider = Slider(start=0, end=20,
                    value=10, step=1, title="Operating Cost $/bbl")
sust_slider = Slider(start=0, end=20,
                     value=4, step=1, title="Sustaining Capital Cost $/bbl")
roy_slider = Slider(start=0, end=20,
                    value=2, step=1, title="Royalties $/bbl")
tax_slider = Slider(start=0, end=20,
                    value=3.8, step=0.2, title="Taxes & Other Costs $/bbl")
emiss_slider = Slider(start=0, end=20,
                      value=0.3, step=0.1, title="Emission Compliance $/bbl")
tran_slider = Slider(start=0, end=20,
                     value=7, step=1, title="Transport Cost $/bbl")
#oth_slider = Slider(start=0, end=20,
                    #value=1, step=1, title="Other Cost $/bbl")
upt_slider = Slider(start=0, end=1,
                    value=0.95, step=0.01, title="Uptime")
facil_slider = Slider(start=0, end=100000,
                      value=40000, step=500, title="Facility Size bbl/d")

# IRR GRAPH
####################################
irrval = round(np.irr([y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12,
                       y13, y14, y15, y16, y17, y18, y19, y20, y21, y22, y23,
                       y24, y25, y26, y27, y28, y29,
                       y30]), 3)
npvval = round(np.npv(0.10, [y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11,
                      y12, y13, y14, y15, y16, y17, y18, y19, y20, y21, y22,
                      y23, y24, y25, y26, y27, y28, y29,
                      y30]), 0)
capexperbbl = et / facilitysz

irr = figure(title="IRR", title_location="above", plot_width=400,
             plot_height=400, x_range=(0, 3), y_range=(0, 3))


label = Label(x=0.25, y=1.00, text='IRR: {:.1%}' .format(irrval),
              text_font_size='25pt', text_color='teal')
label2 = Label(x=0.25, y=0.25, text='NPV: {:,.0f}' .format(npvval),
               text_font_size='25pt', text_color='teal')
label3 = Label(x=0.25, y=1.75, text='$/bbl: {:,.0f}' .format(capexperbbl),
               text_font_size='25pt', text_color='teal')
label4 = Label(x=0.25, y=2.50, text='CAPEX $: {:,}' .format(et),
               text_font_size='25pt', text_color='teal')

irr.add_layout(label)
irr.add_layout(label2)
irr.add_layout(label3)
irr.add_layout(label4)

irr.xgrid.grid_line_color = None
irr.ygrid.grid_line_color = None
irr.xaxis.visible = False
irr.yaxis.visible = False
irr.background_fill_color = "aliceblue"


# Intro Para
####################################
#Text
div = Div(text="""<h3 style="text-align: left;"><strong><span style="color: #333333;">David Peabody</span></strong></span></h3>
<h1 style="text-align: left;"><span style="text-decoration: underline;"><strong><span style="color: #333333; text-decoration: underline;">CAPEX &amp; OPEX Dashboard</span></strong></span></h1>
<h2><span style="color: #333333;">Move the sliders to investigate the effects of CAPEX and OPEX on the projects rate of return. For a full list of references and assumption please see the following link.&nbsp;<a title="Link to References" href="https://github.com/Z0m6ie/App_Capex/tree/master" target="_blank">References</a></span></h2>
<h5><span style="color: #333333;">To buy the developer a well deserved coffee please click the following link.&nbsp;<a title="paypal" href="https://www.paypal.me/DPeabody63" target="_blank">paypal</a></span></h5>""", width=400, height=300)
# div = Div(text="""<h1 style="text-align: left;"><strong><span style="color: #333333;"><img src="http://www.snclavalin.com/en/files/images/SNC-Logo_Desktop.png" alt="Logo" width="107" height="47" /></span></strong></h1>
# <h1 style="text-align: left;"><span style="text-decoration: underline;"><strong><span style="color: #333333; text-decoration: underline;">CAPEX &amp; OPEX Dashboard</span></strong></span></h1>
# <h2><span style="color: #333333;">Move the sliders to investigate the effects of CAPEX and OPEX on the projects rate of return. For a full list of references and assumption please see the following link.&nbsp;<a title="Link to References" href="https://github.com/Z0m6ie/App_Capex/tree/master" target="_blank">References</a></span></h2>""", width=400, height=300)



# UPDATE FUNCTION
####################################
def update_data(attrname, old, new):
    # capex function
    ################################

    # Get the current slider values
    a = eng_slider.value
    b = equip_slider.value
    c = bulk_slider.value
    d = indi_slider.value
    e = lab_slider.value
    # opex function
    ################################
    # Data - Get current slider value
    Oil_Price_CAD = oil_slider.value
    #Oil_Price_CAD = Oil_Price * Exchangert
    Fuel = fuel_slider.value
    Opp_Cost = opp_slider.value
    Sus_Cap = sust_slider.value
    Royalties = roy_slider.value
    Taxes = tax_slider.value
    Emission_Comp = emiss_slider.value
    Transport = tran_slider.value
    #Other = oth_slider.value
    Uptime = upt_slider.value
    facilitysz = facil_slider.value
    Construction_time_str = time_select.value
    Construction_time = float(Construction_time_str)
    Net = Uptime * (365 * (facilitysz * (Oil_Price_CAD - (Fuel + Opp_Cost +
                                                 Sus_Cap + Royalties + Taxes + Emission_Comp + Transport))))
    Year = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    if Construction_time == 2.5:
        # Calculate Top & Bottom
        ab = 0
        at = a
        bt = (a) + b
        ct = (a) + b + c
        dt = ((a) + b + c + (d))
        et = ((a) + b + c + (d) + (e))
    elif Construction_time == 4:
        ab = 0
        at = a
        bt = (a) + b
        ct = (a) + b + c
        dt = ((a) + b + c + (d))
        et = ((a) + b + c + (d) + (e))
    else:
        ab = 0
        at = a
        bt = a + b
        ct = a + b + c
        dt = a + b + c + d
        et = a + b + c + d + e

    # if Construction_time == 2.5:
    #     # Calculate Top & Bottom
    #     ab = 0
    #     at = a*0.75
    #     bt = (a*0.75) + b
    #     ct = (a*0.75) + b + c
    #     dt = ((a*0.75) + b + c + (d*0.8))
    #     et = ((a*0.75) + b + c + (d*0.8) + (e*0.75))
    # elif Construction_time == 4:
    #     ab = 0
    #     at = a*1.25
    #     bt = (a*1.25) + b
    #     ct = (a*1.25) + b + c
    #     dt = ((a*1.25) + b + c + (d*1.25))
    #     et = ((a*1.25) + b + c + (d*1.25) + (e*1.25))
    # else:
    #     ab = 0
    #     at = a
    #     bt = a + b
    #     ct = a + b + c
    #     dt = a + b + c + d
    #     et = a + b + c + d + e
    # New sources
    engsource.data = dict(x=[ab], y=[at], desc=['Engineering'], info=[at])
    equipsource.data = dict(x=[at], y=[bt], desc=['Equipment'], info=[bt-at])
    bulksource.data = dict(x=[bt], y=[ct], desc=['Bulk Materials'],
                           info=[ct-bt])
    indisource.data = dict(x=[ct], y=[dt], desc=['Indirects'], info=[dt-ct])
    labsource.data = dict(x=[dt], y=[et], desc=['Labour'], info=[et-dt])
    # Return Calculation
    con_var = Construction_time - 1
    if Construction_time == 3:
        # Return Calculation
        y0 = -et / 2
        y1 = -et / 2
        y2 = Net * 0.75
        y3 = Net
        y4 = Net
        y5 = Net
    elif Construction_time == 4:
        y0 = -et / 2
        y1 = -et / 2
        y2 = Net * 0.25
        y3 = Net * 0.75
        y4 = Net
        y5 = Net
    elif Construction_time == 2.5:
        y0 = -et / 2
        y1 = -et / 2
        y2 = Net
        y3 = Net
        y4 = Net
        y5 = Net

    y6 = Net
    y7 = Net
    y8 = Net
    y9 = Net
    y10 = Net
    y11 = Net
    y12 = Net
    y13 = Net
    y14 = Net
    y15 = Net
    y16 = Net
    y17 = Net
    y18 = Net
    y19 = Net
    y20 = Net
    y21 = Net
    y22 = Net
    y23 = Net
    y24 = Net
    y25 = Net
    y26 = Net
    y27 = Net
    y28 = Net
    y29 = Net
    y30 = Net

    # Payback data list
    Payback = [y0, y0 + y1, y0 + y1 + y2, y0 + y1 + y2 + y3, y0 + y1 + y2 + y3 + y4, y0 + y1 + y2 + y3 + y4 + y5, y0 + y1 + y2 + y3 + y4 + y5 + y6,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
               y8 + y9, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 +
               y10, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
               y8 + y9 + y10 + y11 + y12 + y13, y0 + y1 + y2 + y3 + y4 +
               y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 +
               y10 + y11 + y12 + y13 + y14 + y15 + y16, y0 + y1 + y2 + y3 + y4 + y5 +
               y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 +
               y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19, y0 + y1 + y2 + y3 + y4 + y5 + y6 +
               y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21, y0 +
               y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 +
               y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 +
               y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
               y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 +
               y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 +
               y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 +
               y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 +
               y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y30]

    # New sources
    returnsource.data = dict(x=Year, y=Payback)

    # IRR Graph Update
    irrval = round(np.irr([y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12,
                           y13, y14, y15, y16, y17, y18, y19, y20, y21, y22, y23,
                           y24, y25, y26, y27, y28, y29,
                           y30]), 3)
    label.text = 'IRR: {:.1%}' .format(irrval)
    npvval = round(np.npv(0.10, [y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11,
                          y12, y13, y14, y15, y16, y17, y18, y19, y20, y21, y22,
                          y23, y24, y25, y26, y27, y28, y29,
                          y30]), 0)
    label2.text = 'NPV: {:,.0f}' .format(npvval)
    capexperbbl = et / facilitysz
    label3.text = '$/bbl: {:,.0f}' .format(capexperbbl)
    label4.text = 'CAPEX $: {:,}' .format(et)


for w in [eng_slider, equip_slider, bulk_slider, indi_slider, lab_slider,
          oil_slider, fuel_slider, opp_slider, sust_slider, roy_slider,
          tax_slider, emiss_slider, tran_slider, upt_slider, facil_slider,
          time_select]:
    w.on_change('value', update_data)

#  CAPEX Set up layouts and add to document
inputs = widgetbox(facil_slider, eng_slider, equip_slider,
                   bulk_slider, indi_slider, lab_slider,
                   sizing_mode='scale_width')


# PAYBACK Set up layouts and add to document
Tinputs1 = widgetbox(oil_slider, fuel_slider,
                     opp_slider, sust_slider, roy_slider,
                     sizing_mode='scale_width')

Tinputs2 = widgetbox(time_select, upt_slider, tax_slider, emiss_slider,
                     tran_slider, sizing_mode='scale_width')

para = widgetbox(div, sizing_mode='scale_width')

l = layout([
           [para, inputs, Tinputs1, Tinputs2],
           [p, irr],
           [T],
           ], sizing_mode='scale_width')


# Show!
curdoc().add_root(l)
curdoc().title = "SAGD CAPEX"
