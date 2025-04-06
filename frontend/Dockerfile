# Use a specific Node version (better stability)
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy only package files first (for better caching)
COPY package*.json ./

# Install dependencies (clean install)
RUN npm ci

# Copy the rest of the app
COPY . .

# Set React environment variables (for Docker)
ENV HOST=0.0.0.0
ENV PORT=3000

# Expose port (for documentation)
EXPOSE 3000

# Start the app (React default)
CMD ["npm", "start"]