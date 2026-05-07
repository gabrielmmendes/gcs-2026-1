# Requisitos do Projeto

## Descrição
Conversor de PDF para PNG com suporte a download em massa via arquivo ZIP.

## Requisitos Funcionais
- RF01: Permitir upload de arquivo PDF via seleção ou arrastar e soltar
- RF02: Converter cada página do PDF em uma imagem PNG
- RF03: Exibir prévia de cada página convertida
- RF04: Permitir download individual de cada página como PNG
- RF05: Permitir download de todas as páginas em um único arquivo ZIP
- RF06: Exibir progresso da conversão em tempo real
- RF07: Controle de qualidade/escala da imagem (1x a 3x)

## Requisitos Não Funcionais
- RNF01: Interface responsiva (desktop e mobile)
- RNF02: Processamento 100% no lado do cliente (sem envio de dados ao servidor)
- RNF03: Suporte aos navegadores modernos (Chrome, Firefox, Edge, Safari)
- RNF04: Tempo de resposta visual imediato durante a conversão

## Dependências Externas
- pdf.js v3.4.120 — renderização de PDFs no navegador
- jszip v3.10.1 — criação de arquivos ZIP no cliente
- FileSaver.js v2.0.5 — download de arquivos gerados no cliente
