from django.shortcuts import render
from .forms import CSVUploadForm


# Se importan las clases generadas para ejecutar la 
# optimización
from utils.resultshandler import ResultsHandler
from models.model import OptimizationModel
from databases.dataloader import ParametersData


def load_and_optimize(request):
    """
    Calculates the area of a rectangle.

    Args:
        django request: request para carga de archivo.

    Returns:
        render: Renderiza htmls de la carpeta templates
                según el resultado de la optimización.
    """

    # POST da acceso a que se suba data al servidor 
    if request.method == "POST":

        # Garantizando que el tipo de archivo sea valido
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Acceso y lectura de csv para DataLoader
            csv_file = request.FILES.get('file')
            dataset = ParametersData(csv_file=csv_file)
            # Se accede a los datos en la primera línea
            data = dataset[0]

            # Se construye el optimizador incorporándole la 
            # data del csv y se ejecuta la optimización
            optimizador = OptimizationModel(data)
            resultado = optimizador.run_optimization()

            # Se muestran los resultados de la optimización
            # accediendo a distintos HTML de success o failure
            handler = ResultsHandler(resultado)
            html, script = handler.show_results()

            # Render del html para los resultados
            return render(request, html, script)
    else:
        form = CSVUploadForm()
    
    # Render de html para cargar el csv
    return render(request, 'load_csv.html', {'form': form})