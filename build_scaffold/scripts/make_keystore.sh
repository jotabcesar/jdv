#!/usr/bin/env bash
set -euo pipefail
KEYSTORE=${KEYSTORE:-jdv-app/jdv.keystore}
ALIAS=${ALIAS:-jdv}
keytool -genkey -v -keystore "$KEYSTORE" -alias "$ALIAS" -keyalg RSA -keysize 2048 -validity 10000