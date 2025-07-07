import sys
import os

from utils.resultshandler import ResultsHandler
from models.model import OptimizationModel
from databases.dataloader import ParametersData


def main():
    if len(sys.argv) < 2:
        print('Syntax: python main.py [archivo.csv]')
        return

    # Argumento del csv en la linea de comando 
    archivo_csv = sys.argv[1]

    # Lectura de CSV
    dataset = ParametersData(csv_file=archivo_csv)
    # Obtención de parámetros en CSV
    data = dataset[0]
    # Optimizador con datos
    optimizador = OptimizationModel(data)
    # Ejecución del optimizador
    resultado = optimizador.run_optimization()
    # Manejo de resultados
    handler = ResultsHandler(resultado)
    _,show = handler.show_results()

    
    if resultado.success:
        print('\n\nSolución óptima encontrada: \n',
                'Cantidad de producto A: ',show['ProductA'],'\n',
                'Cantidad de producto B: ',show['ProductB'],'\n',
                'Máximo ingreso diario: ',show['Income'],'\n\n')
    
    else:
        print('\n\n',show['Resultado'],'\n\n')
if __name__ == '__main__':
    main()