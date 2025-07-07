from django import forms


class CSVUploadForm(forms.Form):
    '''
    Se incluye formulario de Django para asegurar que el archivo 
    de entrada sea un csv.
    '''

    file = forms.FileField(label='Selecciona tu archivo CSV')