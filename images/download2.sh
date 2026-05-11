#!/bin/bash
set -e

IMGDIR="$HOME/.openclaw/workspace/news-site/images"
cd "$IMGDIR"

echo "Downloading from pollinations.ai with flux model (better queue)..."

# Use flux model which may have different queue
download() {
  local name="$1"
  local prompt="$2"
  local encoded=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$prompt'))")
  local url="https://image.pollinations.ai/prompt/${encoded}?width=800\u0026height=450\u0026nologo=true\u0026model=flux"
  
  echo -n "  $name.jpg ... "
  if curl -sL --max-time 60 "$url" -o "$name.jpg" 2>/dev/null; then
    local size=$(stat -f%z "$name.jpg" 2>/dev/null || stat -c%s "$name.jpg" 2>/dev/null)
    if [ "$size" -gt 5000 ]; then
      echo "OK ($size bytes)"
      return 0
    else
      echo "FAIL (small: $size bytes)"
      return 1
    fi
  else
    echo "FAIL (timeout)"
    return 1
  fi
}

# Try downloading the failed ones with longer timeout
download "finance_3" "BMW car factory" || true
download "tech_2" "robot hand" || true
download "tech_3" "humanoid robot" || true

echo "Done."
