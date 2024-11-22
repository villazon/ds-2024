FROM nginx:alpine

# Copy the custom configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Install envsubst (part of gettext package)
RUN apk add --no-cache gettext

