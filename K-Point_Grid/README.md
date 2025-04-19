# Geração de Malha de Pontos-k com Espaçamento Uniforme 

Este script Python gera malhas de **pontos-k uniformemente espaçadas** para testes de convergência de pontos-k com espaçamento controlado. O objetivo é manter o mesmo espaçamento entre pontos no espaço recíproco ao variar o número de divisões ao longo do vetor da rede recíproca \( b_1 \).


A malha é gerada no formato `K_POINTS automatic`, variando o número de divisões \( n_1 \) ao longo de um dos vetores da rede recíproca (\( \vec{b}_1 \)) e ajustando automaticamente \( n_2 \) e \( n_3 \) para manter o espaçamento o mais uniforme possível.
 
 
## Algoritmo

1. **Leitura dos parâmetros da célula** no formato `CELL_PARAMETERS angstrom`.
2. **Cálculo dos vetores da rede recíproca** \( \vec{b}_1, \vec{b}_2, \vec{b}_3 \).
3. Para cada valor de \( n_1 \) dentro do intervalo definido:
   - Calcula o espaçamento \( \Delta k \approx |\vec{b}_1| / n_1 \).
   - Estima \( n_2 \) e \( n_3 \) de forma proporcional, para manter \( \Delta k \) constante nas três direções.
   - Evita repetições de malhas idênticas.
4. **Salva a malha gerada** no arquivo `kpoints_uniform_spacing.txt`.

 

## Notas

- A célula deve estar no formato `CELL_PARAMETERS angstrom`.
 