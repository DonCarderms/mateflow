#!/bin/bash
echo "Aplicando migrations"
python manage.py makemigrations
python manage.py migrate

echo "Atualizando a versão de colação do banco de dados"
python manage.py dbshell <<EOF
ALTER DATABASE gestao_materiais REFRESH COLLATION VERSION;
EOF

echo "Iniciando o servidor"
python manage.py runserver 0.0.0.0:8000


