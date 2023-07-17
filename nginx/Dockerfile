# Use a imagem base do Nginx
FROM nginx

# Copie o arquivo de configuração do Nginx para dentro do contêiner
COPY nginx.conf /etc/nginx/nginx.conf

# Exponha a porta 80 para tráfego externo
EXPOSE 80

# Comando de inicialização do Nginx
CMD ["nginx", "-g", "daemon off;"]
