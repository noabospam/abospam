#!/bin/bash

set -o nounset

pattern='(\+[a-z0-9]+)?'
marker='(ABOSPAM)?'

while IFS=@ read local domain
do
  local=${local//./\\.}
  domain=${domain//./\\.}
  echo "^${local,,}${pattern}@${domain,,}\$${marker}"
done
