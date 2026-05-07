# Arquitetura do Projeto

## Visão Geral
Aplicação web estática (Single Page Application) sem backend. Todo o processamento
ocorre no navegador do usuário utilizando APIs modernas do HTML5.

## Estrutura de Camadas

```
+-----------------------------------+
|       Interface (HTML/CSS)        |
+-----------------------------------+
|     Lógica de Negócio (JS)        |
|  - Upload Handler                 |
|  - PDF Renderer (pdf.js)          |
|  - ZIP Builder (jszip)            |
|  - File Downloader (FileSaver)    |
+-----------------------------------+
|      APIs do Navegador            |
|  - FileReader API                 |
|  - Canvas API                     |
|  - Drag & Drop API                |
+-----------------------------------+
```

## Fluxo de Dados
1. Usuário seleciona ou arrasta um arquivo PDF
2. FileReader lê o arquivo como ArrayBuffer
3. pdf.js carrega e renderiza cada página em um canvas
4. O canvas é exportado como dataURL PNG
5. As imagens são exibidas na interface e armazenadas em memória
6. O usuário faz download individual ou via ZIP (jszip + FileSaver)

## Arquivos Principais
| Arquivo               | Responsabilidade                      |
|-----------------------|---------------------------------------|
| index.html            | Estrutura, estilos e lógica principal |
| src/main.py           | Script auxiliar de build/validação    |
| src/utils/            | Utilitários reutilizáveis             |
| config/settings.json  | Parâmetros de configuração            |
