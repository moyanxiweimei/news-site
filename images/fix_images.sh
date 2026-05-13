#!/bin/bash
set -e

IMGDIR="$HOME/.openclaw/workspace/news-site/images"
cd "$IMGDIR"

echo "Re-downloading relevant images for 5月13日 news..."

# Better prompts - shorter, more focused
declare -a images=(
  "finance_1:office workers protest holding signs corporate building"
  "finance_2:USB charger power bank electronic accessories white"
  "finance_3:luxury electric SUV car automotive"
  "tech_1:smartphone social media app interface mobile"
  "tech_2:laptop computer processor chip technology"
  "tech_3:computer keyboard mouse office desk"
  "medical_1:hospital medical doctor healthcare"
  "medical_2:brain digital neural network AI"
  "medical_3:smartwatch wearable health tech"
  "medical_4:medicine pills pharmacy"
  "medical_5:brain implant neuroscience medical"
  "education_1:university graduation students campus"
  "education_2:students computer classroom learning"
  "education_3:VR headset virtual reality education"
  "education_4:workshop technical training school"
  "education_5:children studying classroom school"
  "aerospace_1:rocket launch space fire night"
  "aerospace_2:flying car drone aerial vehicle"
  "aerospace_3:satellite orbit space earth"
  "aerospace_4:moon lunar surface astronaut"
  "aerospace_5:supersonic jet airplane sky"
  "products_1:gaming phone RGB transparent"
  "products_2:sports watch running GPS wearable"
  "products_3:mechanical keyboard gaming RGB"
  "auto_1:electric vehicle modern car"
  "auto_2:electric car charging station"
  "auto_3:smart car autonomous driving"
  "vc_1:3D printer machine manufacturing"
  "vc_2:mini PC computer small"
  "vc_3:smartphone flagship mobile device"
)

SEED=500
for item in "${images[@]}"; do
  name="${item%%:*}"
  prompt="${item#*:}"
  encoded=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$prompt'))")
  url="https://image.pollinations.ai/prompt/${encoded}?width=800&height=450&seed=${SEED}&nologo=true"
  
  echo -n "  $name.jpg ... "
  # Try pollinations first
  if curl -sL --max-time 30 "$url" -o "$name.jpg" 2>/dev/null; then
    size=$(stat -f%z "$name.jpg" 2>/dev/null || stat -c%s "$name.jpg" 2>/dev/null)
    if [ "$size" -gt 8000 ]; then
      echo "OK ($size bytes)"
    else
      echo "FAIL (small: $size bytes), using fallback"
      curl -sL --max-time 15 "https://picsum.photos/seed/${SEED}/800/450" -o "$name.jpg" 2>/dev/null
      size=$(stat -f%z "$name.jpg" 2>/dev/null || stat -c%s "$name.jpg" 2>/dev/null)
      echo "  fallback ($size bytes)"
    fi
  else
    echo "FAIL (timeout), using fallback"
    curl -sL --max-time 15 "https://picsum.photos/seed/${SEED}/800/450" -o "$name.jpg" 2>/dev/null
    size=$(stat -f%z "$name.jpg" 2>/dev/null || stat -c%s "$name.jpg" 2>/dev/null)
    echo "  fallback ($size bytes)"
  fi
  
  SEED=$((SEED + 3))
done

echo ""
echo "Done. Checking all images:"
for f in *.jpg; do
  size=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f" 2>/dev/null)
  if [ "$size" -gt 5000 ]; then
    echo "  ✓ $f ($size bytes)"
  else
    echo "  ✗ $f ($size bytes) - FAILED"
  fi
done
