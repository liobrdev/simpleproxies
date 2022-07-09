FROM node:lts-alpine@sha256:0738b9ee56009d771f70eb8524d524400e02f65d4b7e528d166c6f82d66f9061 AS compiler
RUN apk add --no-cache libc6-compat
WORKDIR /frontend
COPY package*.json ./
COPY tsconfig*.json ./
RUN npm install
COPY . ./
ENV NEXT_TELEMETRY_DISABLED 1
ENV NODE_ENV production
RUN npm run build

FROM node:lts-alpine@sha256:0738b9ee56009d771f70eb8524d524400e02f65d4b7e528d166c6f82d66f9061 AS cleanup
WORKDIR /frontend
COPY --from=compiler /frontend/.next ./.next
COPY --from=compiler /frontend/public ./public
COPY --from=compiler /frontend/package.json ./package.json
COPY --from=compiler /frontend/package-lock.json ./package-lock.json
RUN npm install --only=production

FROM node:lts-alpine@sha256:0738b9ee56009d771f70eb8524d524400e02f65d4b7e528d166c6f82d66f9061 AS runner
WORKDIR /frontend
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
COPY --from=cleanup --chown=nextjs:nodejs /frontend ./
EXPOSE 3000
