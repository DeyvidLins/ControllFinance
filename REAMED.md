Como Transformar um arquivo IU(Feito arquivo XML em um script .py):

1 - Vá no diretório onde está instalado o seu python e cópie o caminho:
Ex.: C:\Users\NAME_USER\AppData\Local\Programs\Python\Python39;

2 - Abra o prompt de comando de sua preferência e cole o caminho:

3 - Entre na pasta scripts:
Ex.: cd scrpts;

4 - Localize se existi o arquivo pyuic5.exe pois será útil para a conversão;

5 - Digite o comando no terminal:

>pyuic5.exe -x "C:\Users\NAME_USER\Desktop\Formulario-ControleFinanceiro.ui" -o "C:\Users\NAME_USER\Desktop\Formulario-ControleFinanceiro.py"

6 - Pronto, foi gerado seu novo arquivo python

