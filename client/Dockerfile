# 1. For build React app
FROM node:lts AS development
# Set working directory
WORKDIR /client/
#
COPY package.json ./package.json
COPY package-lock.json ./package-lock.json
# Same as npm install
COPY . .
ENV PORT=3000
EXPOSE 3000/tcp
CMD [ "npm", "start" ]

RUN npm run build
