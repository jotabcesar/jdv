#!/usr/bin/env bash
set -euo pipefail
MODE=${1:-debug}
APP_DIR="jdv-app"; DIST="dist"; mkdir -p "$DIST"; docker pull kivy/buildozer:latest
if [[ "$MODE" == "debug" ]]; then docker run --rm -v "$PWD":/work -w /work/"$APP_DIR" kivy/buildozer:latest buildozer android debug; else docker run --rm -v "$PWD":/work -w /work/"$APP_DIR" kivy/buildozer:latest buildozer android release; fi
cp -v "$APP_DIR"/bin/* "$DIST"/ || true