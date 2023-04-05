# Use a imagem node como base
FROM node:latest

# Copie os arquivos do aplicativo
COPY . /frontend
WORKDIR /frontend

# Instale as dependências
RUN npm i

# Exponha a porta em que o seu aplicativo será executado
EXPOSE 3000

# Defina o comando de inicialização
CMD ["npm", "start", "0.0.0.0:3000"]

# # Construa o aplicativo
# RUN npm run build

# # Defina o comando de inicialização
# CMD ["npx", "serve", "-s", "build"]
