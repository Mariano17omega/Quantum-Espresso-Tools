Os arquivos `x.sh` e test-email.qsub são exemplos simplificados de como as funções do `notify.py` devem ser chamadas a partir de um script shell.

O arquivo `KEY-GMAIL.txt` deve conter, em linhas separadas:  
1. E-mail de origem  
2. E-mail de destino  
3. Senha de aplicativo gerada para o e-mail de envio

A senha de aplicativo pode ser gerada em: https://security.google.com/settings/security/apppasswords

A pasta temporaria tmp não será inclusa no arquivo enviado pelo email.

OBS: Os aquivos `notify.py` e `KEY-GMAIL.txt` precisam está nas mesmas pastas que seus scripts para funciona. O Cluster Lucci não aceita que você coloque o `notify.py` fora da pasta onde está chamando, ou seja, precisará ter uma copia desses arquivos em cada pasta de simulação.

A
