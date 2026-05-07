# CONFIG_MAP.md — Mapa de Itens de Configuração (ICs)

> Documento de Gerência de Configuração do projeto **Conversor PDF para PNG**.  
> Registra todos os ICs sob controle, suas versões, localizações e responsáveis.

---

## 1. Política de Versionamento Semântico

Este projeto adota o padrão **Semantic Versioning 2.0.0** ([semver.org](https://semver.org/lang/pt-BR/)).

### Formato

```
MAJOR.MINOR.PATCH[-PRE_RELEASE][+BUILD_METADATA]
```

| Segmento         | Quando incrementar                                                  | Exemplo          |
|------------------|---------------------------------------------------------------------|------------------|
| **MAJOR**        | Mudança incompatível com versão anterior (breaking change)          | `1.0.0` → `2.0.0`|
| **MINOR**        | Nova funcionalidade compatível com versões anteriores               | `1.0.0` → `1.1.0`|
| **PATCH**        | Correção de bug compatível com versões anteriores                   | `1.0.0` → `1.0.1`|
| **PRE_RELEASE**  | Versão instável, identificada com sufixo após hífen                 | `1.1.0-alpha.1`  |
| **BUILD_META**   | Metadados de build, identificados com `+` (não afetam precedência) | `1.0.0+20250101` |

### Exemplos de Progressão

```
1.0.0-alpha.1   → Alpha: funcionalidade incompleta, uso interno
1.0.0-beta.1    → Beta: funcionalidade completa, em testes
1.0.0-rc.1      → Release Candidate: pronto para produção, aguardando aprovação
1.0.0           → Release estável
1.0.1           → Hotfix (correção de bug)
1.1.0           → Nova feature (ex.: suporte a múltiplos PDFs)
2.0.0           → Breaking change (ex.: mudança de API ou formato de saída)
```

### Regras de Nomenclatura de Tags Git

```
v{MAJOR}.{MINOR}.{PATCH}           # Ex.: v1.0.0
v{MAJOR}.{MINOR}.{PATCH}-{PRE}     # Ex.: v1.1.0-beta.2
```

---

## 2. Itens de Configuração (ICs)

### 2.1 Produto Principal

| ID     | Nome          | Tipo      | Versão Atual | Localização       | Responsável     |
|--------|---------------|-----------|--------------|-------------------|-----------------|
| IC-001 | index.html    | Artefato  | `1.0.0`      | `/index.html`     | Equipe Frontend |

---

### 2.2 Documentação

| ID     | Nome              | Tipo          | Versão Atual | Localização               |
|--------|-------------------|---------------|--------------|---------------------------|
| IC-002 | README.md         | Documentação  | `1.0.0`      | `/README.md`              |
| IC-003 | CHANGELOG.md      | Documentação  | `1.0.0`      | `/CHANGELOG.md`           |
| IC-004 | requisitos.md     | Documentação  | `1.0.0`      | `/docs/requisitos.md`     |
| IC-005 | arquitetura.md    | Documentação  | `1.0.0`      | `/docs/arquitetura.md`    |
| IC-006 | CONFIG_MAP.md     | Documentação  | `1.0.0`      | `/CONFIG_MAP.md`          |

---

### 2.3 Código-Fonte

| ID     | Nome             | Tipo           | Versão Atual | Localização                  |
|--------|------------------|----------------|--------------|------------------------------|
| IC-007 | main.py          | Código-fonte   | `1.0.0`      | `/src/main.py`               |
| IC-008 | file_utils.py    | Código-fonte   | `1.0.0`      | `/src/utils/file_utils.py`   |
| IC-009 | __init__.py      | Código-fonte   | `1.0.0`      | `/src/utils/__init__.py`     |

---

### 2.4 Testes

| ID     | Nome           | Tipo   | Versão Atual | Localização              | Cobertura           |
|--------|----------------|--------|--------------|--------------------------|---------------------|
| IC-010 | test_main.py   | Teste  | `1.0.0`      | `/tests/test_main.py`    | file_utils, config  |

---

### 2.5 Scripts e Automação

| ID     | Nome       | Tipo   | Versão Atual | Localização           | Função                       |
|--------|------------|--------|--------------|-----------------------|------------------------------|
| IC-011 | build.sh   | Script | `1.0.0`      | `/scripts/build.sh`   | Instalar deps, testar, validar|

---

### 2.6 Configuração de Ambiente

| ID     | Nome              | Tipo          | Versão Atual | Localização              |
|--------|-------------------|---------------|--------------|--------------------------|
| IC-012 | settings.json     | Configuração  | `1.0.0`      | `/config/settings.json`  |
| IC-013 | config.env        | Configuração  | `1.0.0`      | `/config.env`            |
| IC-014 | requirements.txt  | Configuração  | `1.0.0`      | `/requirements.txt`      |

---

### 2.7 Bibliotecas e Frameworks Externos (Dependências)

#### Frontend (CDN)

| ID     | Nome           | Tipo       | Versão Fixada | Origem (CDN)                                                    | Função                          |
|--------|----------------|------------|---------------|-----------------------------------------------------------------|---------------------------------|
| IC-015 | pdf.js         | Biblioteca | `3.4.120`     | cdnjs.cloudflare.com/ajax/libs/pdf.js/3.4.120/pdf.min.js       | Renderização de PDF no navegador|
| IC-016 | jszip          | Biblioteca | `3.10.1`      | cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js       | Criação de arquivos ZIP         |
| IC-017 | FileSaver.js   | Biblioteca | `2.0.5`       | cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js | Download de arquivos no cliente |

#### Backend / Dev (Python)

| ID     | Nome     | Tipo        | Versão Mínima | Instalação      | Função                   |
|--------|----------|-------------|---------------|-----------------|--------------------------|
| IC-018 | Python   | Runtime     | `3.9.0`       | Sistema         | Execução de scripts      |
| IC-019 | pytest   | Framework   | `7.4.0`       | requirements.txt| Execução de testes       |

---

### 2.8 Controle de Versão e Metadados

| ID     | Nome        | Tipo               | Versão  | Localização      |
|--------|-------------|--------------------|---------|------------------|
| IC-020 | .git/       | Controle de versão | —       | `/.git/`         |
| IC-021 | .gitignore  | Configuração Git   | `1.0.0` | `/.gitignore`    |

---

## 3. Matriz de Rastreabilidade

| IC                | Depende de                        | Usado por                      |
|-------------------|-----------------------------------|--------------------------------|
| IC-001 index.html | IC-015 pdf.js, IC-016 jszip, IC-017 FileSaver | Usuário final              |
| IC-007 main.py    | IC-008 file_utils.py, IC-012 settings.json    | IC-011 build.sh            |
| IC-010 test_main.py | IC-008 file_utils.py, IC-019 pytest         | IC-011 build.sh            |
| IC-011 build.sh   | IC-018 Python, IC-019 pytest                  | CI/CD, desenvolvedor       |
| IC-013 config.env | —                                             | IC-011 build.sh, CI/CD     |

---

## 4. Política de Atualização de Dependências

| Tipo de dependência | Frequência de revisão | Critério de atualização                              |
|---------------------|-----------------------|------------------------------------------------------|
| Bibliotecas CDN     | Trimestral            | Apenas PATCH automático; MINOR/MAJOR após avaliação  |
| Python (runtime)    | Semestral             | Manter suporte às duas últimas versões estáveis      |
| pytest              | Semestral             | Seguir versão compatível com Python em uso           |

---

## 5. Histórico de Revisões deste Documento

| Versão | Data       | Autor      | Descrição                        |
|--------|------------|------------|----------------------------------|
| 1.0.0  | 2025-01-01 | —          | Criação inicial do CONFIG_MAP.md |

