### Passo a passo para a correta instalação do PackDeliv

1. Baixe e instale o [Node.js](https://nodejs.org/en/blog/release/v6.11.5/).

2. Abra o CMD e rode: ```> npm install -g cordova ionic```

3. Baixe um editor de texto, recomendo: [Visual Studio Code](https://go.microsoft.com/fwlink/?Linkid=852157).

4. Clone este [repositório](https://github.com/InovaUFRPE/PackDeliv).
    1. Use ```$ git clone https://github.com/InovaUFRPE/PackDeliv``` no Git Bash.

5. Abra o editor de texto e abra a pasta clonada do repositório.
http://prntscr.com/h50y94

6. Agora você pode fazer alterações nos arquivos.

7. No cmd se mova para a pasta do projeto.
http://prntscr.com/h50ytc

7. Agora rode o comando: ```> ionic serve```

8. Será solicitado a instalação de modulos, aceite e espere que o servidor seja iniciado no seu navegador padrão.
http://prntscr.com/h50za7
http://prntscr.com/h50zeu

9. Agora abra a pasta Servidor_API e execute o arquivo: Install Requirements.bat(necessária versão do python 3.6)

10. Agora, dentro da pasta Servidor_API execute RestAPI.py. O banco será criado com o nome de packdeliv, e o projeto estará pronto para ser usado.