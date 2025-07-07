from torch.utils.data import Dataset, DataLoader
import pandas as pd
import os

class ParametersData(Dataset):
    '''
    Clase: ParameterData (torch.Dataset)

    Args:
        file (csv): Recibe un archivo csv.
    
    Variables: 
        data (DataFrame): Data del csv se lee con pandas
        variables (list): Lista de variables correspondientes a 
                          las columnas del csv.
    '''
    
    def __init__(self, csv_file):

        self.data = pd.read_csv(csv_file)

        self.variables = ['Product_A_Production_Time_Machine_1',
                        'Product_A_Production_Time_Machine_2',
                        'Product_B_Production_Time_Machine_1',
                        'Product_B_Production_Time_Machine_2',
                        'Machine_1_Available_Hours',
                        'Machine_2_Available_Hours',
                        'Price_Product_A',
                        'Price_Product_B']

        # Verificando tipo numerico
        assert [x=='float64' or x=='int64' for x in self.data.dtypes]     
        # Verificando cantidad de columnas del csv     
        assert len(self.data.columns.values) == 8
        # Verificando que los nombres de las columnas sean los mismos en 
        # variables. 
        assert [x in self.variables for x in self.data.columns.values], \
                f'Parámetro erróneo. Lista de parámetros: {self.variables} '

    def __len__(self):
        '''
        Returns: 
                Largo (filas) del dataset.
        '''
        return len(self.data)

    def __getitem__(self, idx):
        '''
        Args:
            idx (int): Indice de la fila en el csv del cual se extraen los datos
        
        Returns:
            variables (dict): Diccionario con los datos de cada columna para la
                              fila seleccionado

        '''
        variables = {'ProdA_ProdT_Mach1': self.data['Product_A_Production_Time_Machine_1'].values[idx],
                    'ProdA_ProdT_Mach2': self.data['Product_A_Production_Time_Machine_2'].values[idx],
                    'ProdB_ProdT_Mach1': self.data['Product_B_Production_Time_Machine_1'].values[idx],
                    'ProdB_ProdT_Mach2': self.data['Product_B_Production_Time_Machine_2'].values[idx],
                    'Mach1_Hours': self.data['Machine_1_Available_Hours'].values[idx],
                    'Mach2_Hours': self.data['Machine_2_Available_Hours'].values[idx],
                    'ProdA_Price': self.data['Price_Product_A'].values[idx],
                    'ProdB_Price': self.data['Price_Product_B'].values[idx]}

        return variables