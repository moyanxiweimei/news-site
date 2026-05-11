#!/bin/bash
set -e

IMGDIR="$HOME/.openclaw/workspace/news-site/images"
cd "$IMGDIR"

echo "Downloading featured images from pollinations.ai..."

# Featured images only - most important
declare -a featured=(
  "medical_1:AI medical diagnosis doctor tablet hospital"
  "education_1:AI classroom robot teaching students"
  "aerospace_1:rocket launch space fire"
  "products_1:home appliances electronics kitchen"
  "auto_1:Brazil Rio de Janeiro travel"
  "vc_1:startup office technology AI business"
)

for item in "${featured[@]}"; do
  name="${item%%:*}"
  prompt="${item#*:}"
  encoded=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$prompt'))")
  url="https://image.pollinations.ai/prompt/${encoded}?width=800\u0026height=450\u0026nologo=true"
  
  echo -n "  $name.jpg ... "
  if curl -sL --max-time 50 "$url" -o "$name.jpg" 2>/dev/null; then
    size=$(stat -f%z "$name.jpg" 2>/dev/null || stat -c%s "$name.jpg" 2>/dev/null)
    if [ "$size" -gt 5000 ]; then
      echo "OK ($size bytes)"
    else
      echo "FAIL (small: $size bytes)"
      # Try again once
      echo -n "    Retrying $name.jpg ... "
      sleep 20
      curl -sL --max-time 50 "$url" -o "$name.jpg" 2>/dev/null
      size=$(stat -f%z "$name.jpg" 2>/dev/null || stat -c%s "$name.jpg" 2>/dev/null)
      if [ "$size" -gt 5000 ]; then
        echo "OK ($size bytes)"
      else
        echo "FAIL again"
      fi
    fi
  else
    echo "FAIL (timeout)"
  fi
  sleep 20
done

echo "Downloading remaining images from picsum.photos..."

# Regular images from picsum (fast, reliable, random but high quality)
declare -a regular=(
  "tech_2" "tech_3" "medical_2" "medical_3" "medical_4" "medical_5"
  "education_2" "education_3" "education_4" "education_5"
  "aerospace_2" "aerospace_3" "aerospace_4" "aerospace_5"
  "products_2" "auto_2" "vc_2" "finance_3"
)

SEED=500
for name in "${regular[@]}"; do
  url="https://picsum.photos/seed/${SEED}/800/450"
  echo -n "  $name.jpg ... "
  curl -sL --max-time 15 "$url" -o "$name.jpg" 2>/dev/null
  size=$(stat -f%z "$name.jpg" 2>/dev/null || stat -c%s "$name.jpg" 2>/dev/null)
  if [ "$size" -gt 5000 ]; then
    echo "OK ($size bytes)"
  else
    echo "FAIL ($size bytes)"
  fi
  SEED=$((SEED + 7))
done

echo ""
echo "Results:"
for f in *.jpg; do
  size=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f" 2>/dev/null)
  if [ "$size" -gt 5000 ]; then
    echo "  ✓ $f ($size bytes)"
  else
    echo "  ✗ $f ($size bytes)"
  fi
done
