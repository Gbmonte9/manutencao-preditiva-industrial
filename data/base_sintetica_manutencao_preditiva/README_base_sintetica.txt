BASE DE DADOS SINTÉTICA — MANUTENÇÃO PREDITIVA INDUSTRIAL

Objetivo:
Representar, de forma sintética e plausível, dados de uma operação industrial para desenvolvimento e teste de um projeto acadêmico de Big Data em Python e manutenção preditiva.

IMPORTANTE:
Esta base NÃO é composta por dados fornecidos pela empresa parceira. Os dados foram gerados artificialmente para fins acadêmicos, desenvolvimento, testes e demonstração. Caso a empresa forneça dados reais, a base poderá ser substituída/adaptada.

Arquivos:
- maquinas.csv: cadastro dos equipamentos.
- sensores.csv: leituras horárias de sensores e indicadores operacionais.
- paradas.csv: eventos de parada.
- manutencoes.csv: histórico sintético de manutenção.
- falhas.csv: eventos de falha sintéticos.
- base_ml_consolidada.csv: sensores + características das máquinas, adequada para testes iniciais de Machine Learning.
- base_sintetica_manutencao_preditiva.xlsx: todas as tabelas em abas separadas.

Escala:
- 20 máquinas.
- 1 ano de dados de sensores por máquina.
- Frequência: 1 registro por hora.
- Aproximadamente 175 mil registros de sensores.
- 2.200 eventos de parada.
- 900 registros de manutenção.
- Eventos de falha sintéticos.

Observação metodológica:
Foram inseridos padrões de degradação antes de eventos de falha para permitir testes de detecção de padrões e classificação de risco. Esses padrões são artificiais e não devem ser interpretados como relações industriais reais sem validação com dados da empresa.
