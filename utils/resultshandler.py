import numpy as np
import scipy
from scipy.optimize import linprog

from django.shortcuts import render

class ResultsHandler():
    '''
    Clase: ResultsHandler. Manejo de los resultados de optimización.

    Args:
        results (scipy.optimize): Resultados de la optimización de scipy.
    
    Variables: 
        results (scipy.optimize):   Resultados de la optimización.
        message (str):              Mensaje que describe el estado final de la 
                                    optimización. (success o failure)
        success (bool):             True si se alcanzó un resultado, False si no.
        max_income (float):         Valor óptimo de la función objetivo.
        products (array):           Resultados de las variables de decisión con las
                                    que se alcanza el óptimo.
        productA (float):           Valor de la variable de decisión asociada al 
                                    producto A.
        productB (float):           Valor de la variable de decisión asociada al 
                                    producto B.
    '''
  
    def __init__(self, results):
        assert isinstance(results,scipy.optimize._optimize.OptimizeResult)

        self.results = results

        self.message = self.results.message
        self.success = self.results.success

        # Valores de los resultados en la optimización
        self.max_income = -self.results.fun
        self.products = self.results.x
        self.productA = abs(self.products[0])
        self.productB = abs(self.products[1])



    def show_results(self):
        '''
        Función para manejar los resultados que se mostraran.

        Args:
            -
        
        Returns:
            html (str):         Nombre del html que se desplegará según el 
                                resultado obtenido. 
            resultados (dict):  Diccionario con el resultado a desplegar en
                                el html.
        '''
        # Si se tiene éxito, se accede al html de success y se entregan los valores
        # de las variables de decisión y objetivo obtenidas del modelo.
        if self.success:
            return "success_results.html", {'ProductA': f'{self.productA:.0f}',
                                                'ProductB': f'{self.productB:.0f}', 
                                                'Income': f'{self.max_income:.0f}'}
        # Si no, se retorna el nombre del html de failed y se entrega mensaje de 
        # falla para encontrar valores de optimización.
        else:
            return "failed_results.html", {'Resultado':\
                                    'No se encontró una solución óptima según los parámetros introducidos.'}
