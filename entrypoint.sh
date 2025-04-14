#!/bin/sh

# Fix ownership of /vol directory
echo "Fixing permissions for /vol..."
chown -R app:app /vol

# Execute the original command
exec "$@"
