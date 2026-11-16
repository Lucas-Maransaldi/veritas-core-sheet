# Veritas Core Sheet

Módulo para Foundry VTT 14.367 e D&D5e 6.0.6.

Esta versão requer Foundry VTT 14.367 ou superior dentro da geração 14 e D&D5e
6.0.6. O manifesto não declara suporte ao Foundry V13 ou ao D&D5e 5.x.

## Instalação

No Foundry, abra **Add-on Modules → Install Module** e use este manifesto:

```text
https://github.com/Lucas-Maransaldi/veritas-core-sheet/releases/latest/download/module.json
```

## Funcionalidades

- Aba **Espectro de Magia** com todos os Fundamentos e Arquétipos de Efeito predefinidos.
- Cada conhecimento possui seu próprio círculo C0 a C13 e progresso percentual.
- Avanço automático a cada 100%, preservando o progresso excedente.
- Grupos arcanos recolhíveis, círculo representado por pentagrama e ajuste de progresso por valores positivos ou negativos.
- Aba **Extra Skills** com cadastro de múltiplas habilidades.
- Maestria de 0 a 6 e progresso percentual independente por habilidade.
- Controles rápidos de ±1%, ±10% e avanço ou redução de círculo/maestria.
- Criação manual de Extra Skills pelo botão ou pela tecla Enter.
- Ícone selecionável, descrição recolhível e maestria representada por seis estrelas.
- Barra de progresso com ajustes positivos ou negativos digitados pelo usuário.
- Busca instantânea por nome nas duas abas, abrindo automaticamente os grupos arcanos encontrados.
- Dados armazenados em flags do ator (`flags.veritas-core-sheet`), sem alterar o schema do D&D5e.
- Cartões personalizados de Extra Skills e Armas respeitam o modo de visibilidade selecionado no chat.

## Instalação para desenvolvimento

Copie ou vincule esta pasta para `Data/modules/veritas-core-sheet`, ative o módulo no mundo e recarregue o Foundry.

## Empacotamento para publicação

Execute `python tools/package-release.py` em um checkout limpo da versão a publicar.
O comando gera `dist/veritas-core-sheet.zip` e `dist/module.json`, incluindo a pasta
`assets` e validando os arquivos do manifesto e as imagens locais dos templates.
Publique os dois arquivos como anexos da release correspondente à versão do manifesto.

## Validação de compatibilidade

A revisão estática foi feita contra as APIs do Foundry V14 e o código oficial do
D&D5e 6.0.6. A validação completa em um mundo com as versões alvo ainda precisa ser
executada. Verifique:

- abertura das abas Espectro de Magia, Extra Skills, Armas, Traços e Reputação;
- edição e persistência dos valores após fechar e reabrir a ficha;
- arrastar e soltar Features, abrir suas fichas e selecionar ícones;
- envio dos cartões de Extra Skills e Armas nos modos público, para o GM, cego e para si;
- funcionamento das abas e dos controles ao destacar e reanexar a janela da ficha.
