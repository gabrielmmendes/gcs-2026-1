# Conversor PDF para PNG

Converta qualquer PDF em imagens PNG de alta qualidade, diretamente no navegador.

## Funcionalidades

- Upload via clique ou arrastar e soltar
- Conversao pagina a pagina com previa instantanea
- Controle de qualidade: 1x ate 3x de escala
- Download individual (PNG) ou em massa (ZIP)
- Barra de progresso em tempo real
- 100% local — seus arquivos nunca saem do dispositivo

## Como usar

1. Abra o arquivo `index.html` em qualquer navegador moderno
2. Selecione ou arraste um arquivo PDF
3. Ajuste a qualidade desejada
4. Clique em **Converter PDF**
5. Faca download das paginas ou clique em **Baixar Todas (ZIP)**

## Desenvolvimento

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
python src/main.py
bash scripts/build.sh
```

## Dependencias (CDN)

| Biblioteca   | Versao  | Uso                    |
|--------------|---------|------------------------|
| pdf.js       | 3.4.120 | Renderizacao de PDF    |
| jszip        | 3.10.1  | Criacao de arquivo ZIP |
| FileSaver.js | 2.0.5   | Download de arquivos   |

## Licenca

MIT
