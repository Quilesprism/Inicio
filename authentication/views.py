import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.http import HttpResponse
import os  

def upload_file(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        if file.name.endswith('.xlsx'):
            try:
                df = pd.read_excel(file, sheet_name='CLIENTES')
            except UnicodeDecodeError:
                df = pd.read_excel(file, sheet_name='CLIENTES', encoding='latin1')
            fig = px.bar(df, x='Nombre', y='ValordelaTransacción', title='Gráfico de Barras')
            plot_path = "static/plot.html"
            fig.write_html(plot_path)       
            with open(plot_path, 'r', encoding='utf-8') as plot_file:
                plot_content = plot_file.read()
            return HttpResponse(plot_content)
        else:
            return HttpResponse("El archivo no es de tipo .xlsx")

    return render(request, "index.html")





