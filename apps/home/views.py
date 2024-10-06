# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.conf import settings
import pandas as pd
import plotly.express as px
from django.shortcuts import render
import h5netcdf
import matplotlib.pyplot as plt
import io
import base64
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def pages(request):
    context = {}
    # Verifica que la URL termina en .html
    load_template = request.path.split('/')[-1]

    if not load_template.endswith('.html'):
        return HttpResponse("Invalid request", status=400)

    if load_template == 'admin':
        return HttpResponseRedirect(reverse('admin:index'))

    context['segment'] = load_template

    try:
        # Intenta cargar la plantilla
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        # Manejo del error si la plantilla no existe
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        # Manejo de otros errores
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def index(request):
    return render(request, 'home/index.html') 

def map_view(request):
    # Ruta del archivo NC4
    file_path = os.path.join(settings.BASE_DIR, 'static', 'MERRA2_400.tavg1_2d_flx_Nx.20240901.nc4')

    try:
        # Abrir el archivo NC4 usando h5netcdf
        with h5netcdf.File(file_path, 'r') as dataset:
            latitudes = dataset['lat'][:]
            longitudes = dataset['lon'][:]
            temperatures = dataset['TSH'][:]

        # Seleccionar el primer nivel de temperatura si es necesario
        temperatures_2d = temperatures[0, :, :]  # Ajusta según sea necesario

        # Crear el gráfico
        fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': ccrs.Robinson()})

        # Añadir características al mapa
        ax.add_feature(cfeature.LAND.with_scale('50m'), facecolor='#f0e4d3')
        ax.add_feature(cfeature.OCEAN.with_scale('50m'), facecolor='#a2d2ff')
        ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.7)
        ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle='-', linewidth=0.5)
        ax.add_feature(cfeature.LAKES.with_scale('50m'), facecolor='#a2d2ff')
        ax.add_feature(cfeature.RIVERS.with_scale('50m'), edgecolor='#a2d2ff')

        # Visualizar los datos de temperatura
        temperature_plot = ax.contourf(longitudes, latitudes, temperatures_2d, 60,
                                        transform=ccrs.PlateCarree(), cmap='coolwarm', alpha=0.75)

        # Añadir una barra de colores
        plt.colorbar(temperature_plot, label='Temperatura (K)', orientation='horizontal', pad=0.05)

        # Título del gráfico
        plt.title('Distribución de la temperatura del aire', fontsize=15)

        # Guardar la imagen en un objeto BytesIO
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()  # Cierra la figura para liberar memoria

        # Codificar la imagen a base64 para enviarla al HTML
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        image_data = f"data:image/png;base64,{image_base64}"

    except Exception as e:
        return render(request, 'home/error.html', {'error': str(e)})

    # Renderizar el gráfico en la plantilla
    return render(request, 'home/index.html', {'image_data': image_data})