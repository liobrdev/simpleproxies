FROM node:lts-alpine@sha256:53f011c818d294979f7179495b04ebbe0ec6152a84e491b55174bad783131412 AS compiler
RUN apk add --no-cache libc6-compat
WORKDIR /frontend
COPY package*.json ./
COPY tsconfig*.json ./
RUN npm install
COPY . ./
ENV NEXT_TELEMETRY_DISABLED 1
ENV NODE_ENV production
RUN npm run build

FROM node:lts-alpine@sha256:53f011c818d294979f7179495b04ebbe0ec6152a84e491b55174bad783131412 AS cleanup
WORKDIR /frontend
COPY --from=compiler /frontend/.next ./.next
COPY --from=compiler /frontend/public ./public
COPY --from=compiler /frontend/package.json ./package.json
COPY --from=compiler /frontend/package-lock.json ./package-lock.json
RUN npm install --only=production

FROM node:lts-alpine@sha256:53f011c818d294979f7179495b04ebbe0ec6152a84e491b55174bad783131412 AS runner
WORKDIR /frontend
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
COPY --from=cleanup --chown=nextjs:nodejs /frontend ./
EXPOSE 3000
