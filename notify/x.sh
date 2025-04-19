#!/bin/bash

# Envia um email avisando do inicio.
NOME_DO_JOB="exemplo"
DESCRICAO="Teste de exemplo"
python3 notify_job.py job_run "$NOME_DO_JOB" "$DESCRICAO"
################################################
#
#
# Seu Script
#
#
################################################
# Envia um email avisando que terminou, com os dados da simulação em anexo.
tar --exclude="./tmp" --exclude="notify_job.py" --exclude="KEY-GMAIL.txt" --exclude="./${NAME}.tar.gz" -czf "${NAME}.tar.gz" .
python3 notify_job.py job_end "$NOME_DO_JOB" "$DESCRICAO"  "$(pwd)"

