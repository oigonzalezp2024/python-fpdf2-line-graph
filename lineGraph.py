from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_line_width(0.5)
pdf.set_draw_color(r=92, g=172, b=247)
pdf.set_line_width(0.5)
pdf.set_fill_color(r=0, g=0, b=255)

coords = (
    (50, 100),
    (50, 90),
    (60, 90),
    (70, 90),
    (80, 90),
    (90, 90),
    (100, 90),
    (110, 90),
    (120, 90),
    (130, 90),
    (140, 90),
    (150, 90),
    (160, 90),
    (170, 90),
    (170, 100)
)
pdf.set_fill_color(r=0, g=0, b=255)
pdf.polygon(coords, style="DF")

pdf.line(x1=45, y1=50, x2=170, y2=50)
pdf.line(x1=45, y1=60, x2=170, y2=60)
pdf.line(x1=45, y1=70, x2=170, y2=70)
pdf.line(x1=45, y1=80, x2=170, y2=80)
pdf.line(x1=45, y1=90, x2=170, y2=90)
pdf.line(x1=45, y1=100, x2=170, y2=100)

pdf.line(x1=50, y1=50, x2=50, y2=105)
pdf.line(x1=60, y1=50, x2=60, y2=105)
pdf.line(x1=70, y1=50, x2=70, y2=105)
pdf.line(x1=80, y1=50, x2=80, y2=105)
pdf.line(x1=90, y1=50, x2=90, y2=105)

pdf.line(x1=100, y1=50, x2=100, y2=105)
pdf.line(x1=110, y1=50, x2=110, y2=105)
pdf.line(x1=120, y1=50, x2=120, y2=105)
pdf.line(x1=130, y1=50, x2=130, y2=105)
pdf.line(x1=140, y1=50, x2=140, y2=105)
pdf.line(x1=150, y1=50, x2=150, y2=105)
pdf.line(x1=160, y1=50, x2=160, y2=105)
pdf.line(x1=160, y1=50, x2=160, y2=105)
pdf.line(x1=170, y1=50, x2=170, y2=105)

pdf.set_font(
    family='Times',
    style='B',
    size=9
)


pdf.text(x=38,y=100,text='0')
pdf.text(x=38,y=100,text='0000')
pdf.text(x=38,y=90,text='1000')
pdf.text(x=38,y=80,text='2000')
pdf.text(x=38,y=70,text='3000')
pdf.text(x=38,y=60,text='4000')
pdf.text(x=38,y=50,text='5000')

pdf.text(x=52,y=105,text='ENE')
pdf.text(x=62,y=105,text='FEB')
pdf.text(x=72,y=105,text='MAR')
pdf.text(x=82,y=105,text='ABR')
pdf.text(x=92,y=105,text='MAY')
pdf.text(x=102,y=105,text='JUN')
pdf.text(x=112,y=105,text='JUL')
pdf.text(x=122,y=105,text='AGO')
pdf.text(x=132,y=105,text='SEP')
pdf.text(x=142,y=105,text='OCT')
pdf.text(x=152,y=105,text='NOV')
pdf.text(x=162,y=105,text='DIC')

pdf.output("./reports/lineGraph.pdf")