import numpy as np
from scipy.optimize import linprog

class OptimizationModel():
    '''
    Clase: OptimizationModel. Modelo de optimización.

    Args:
        model_parameters (dict): Diccionario con los parámetros
                                 para el modelo. 
    
    Variables: 
        parameters (dict):          Parámetros del modelo
        precios (array):            Array de numpy con los datos asocidados
                                    a los parámetros de precio
        matrix_conditions (array):  Array de numpy con los datos asociadaos a 
                                    la matriz de condiciones (A_ub) de la 
                                    desigualdad en la ecuación lineal
        vector_conditions (array):  Array de numpy con los datos asociadaos al 
                                    vector resultante (b_ub) de la desigualdad 
                                    en la ecuación lineal.
        product_A (tuple):          Tupla con valores mínimo y máximo (0, None)
                                    para la cantidad de productos de A. Se define
                                    como valores positivos sin límite máximo.
        product_B (tuple):          Tupla con valores mínimo y máximo (0, None)
                                    para la cantidad de productos de B. Se define
                                    como valores positivos sin límite máximo.
    '''

    def __init__(self, model_parameters):
        # Verificando que parámetros se reciban como diccionario
        assert isinstance(model_parameters, dict)
        # Verificando que diccionario contenga un total de 8 valores
        assert len(model_parameters.keys()) == 8

        self.parameters = model_parameters

        self.precios = np.array([-model_parameters['ProdA_Price'],
                                -model_parameters['ProdB_Price']])

        # Matriz de desigualdad A_ub
        self.matrix_conditions = np.array([[model_parameters['ProdA_ProdT_Mach1'],
                                            model_parameters['ProdB_ProdT_Mach1']],
                                            [model_parameters['ProdA_ProdT_Mach2'],
                                            model_parameters['ProdB_ProdT_Mach2']]])
        
        # Vector resultante de desigualdad b_ub
        self.vector_conditions = np.array([model_parameters['Mach1_Hours'],
                                            model_parameters['Mach2_Hours']])

        # Valores minimo y maxiomo para productos A y B >= 0.
        self.product_A = (0,None)
        self.product_B = (0,None)

    def run_optimization(self):
        '''
        Función para ejecutar la optimización de la función lineal objetivo utilizando
        el modelo linprog de scipy. Func: Z = P_A*x_A + P_B*x_B.

        Args:
            -
        
        Returns:
            result (scipy.optimize): Resultados de la optimización de scipy.

        '''
        # Se definen los límites para las variables Product A y B.
        bounds = [self.product_A, self.product_B]

        # Modelo linprog. Recibe precios, matriz A_ub, vector b_ub, los valores límites, y el
        # parámetro integrality [1,1] para considerar únicamente valores enteros para las va-
        # riables a optimizar
        result = linprog(self.precios,
                        A_ub=self.matrix_conditions,
                        b_ub=self.vector_conditions,
                        bounds=bounds, integrality=[1, 1])

        return result