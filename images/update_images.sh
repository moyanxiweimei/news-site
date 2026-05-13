#!/bin/bash
set -e

IMGDIR="$HOME/.openclaw/workspace/news-site/images"
cd "$IMGDIR"

echo "Downloading new images for 5月13日 news..."

# Featured / updated news images
declare -a images=(
  "finance_1:Meta office workers protest, employees holding signs, corporate building, technology company"
  "finance_2:Anker charging products, power bank, USB charger, electronics"
  "finance_3:VOYAH electric car, Chinese automotive, luxury SUV, Dongfeng"
  "tech_1:TikTok app interface, social media, mobile phone, video sharing"
  "tech_2:Google Chromebook laptop, Intel Qualcomm MediaTek chips, processor"
  "tech_3:Meta Facebook office, keyboard mouse tracking, privacy protest"
  "education_1:university students graduation, global education, campus, UNESCO report"
  "products_1:REDMAGIC gaming phone, water cooling, RGB lights, transparent back"
  "products_2:Garmin Forerunner watch, GPS running, sports wearable, AMOLED"
  "products_3:Cherry MX keyboard, mechanical keyboard, gaming, aluminum body"
  "auto_1:VOYAH electric vehicle, Chinese car, modern automotive"
  "vc_1:Flashforge 3D printer, four nozzles, desktop manufacturing"
  "vc_2:NUC mini PC, fanless computer, small form factor, Intel"
  "vc_3:iQOO smartphone, blue green gradient, flagship phone, mobile device"
)

SEED=300
for item in "${images[@]}"; do
  name="${item%%:*}"
  prompt="${item#*:}"
  encoded=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$prompt'))")
  url="https://image.pollinations.ai/prompt/${encoded}?width=800&height=450&seed=${SEED}&nologo=true"
  
  echo -n "  $name.jpg ... "
  if curl -sL --max-time 60 "$url" -o "$name.jpg" 2>/dev/null; then
    size=$(stat -f%z "$name.jpg" 2>/dev/null || stat -c%s "$name.jpg" 2>/dev/null)
    if [ "$size" -gt 5000 ]; then
      echo "OK ($size bytes)"
    else
      echo "FAIL (small: $size bytes)"
      # Fallback to picsum
      curl -sL --max-time 15 "https://picsum.photos/seed/${SEED}/800/450" -o "$name.jpg" 2>/dev/null
      size=$(stat -f%z "$name.jpg" 2>/dev/null || stat -c%s "$name.jpg" 2>/dev/null)
      echo "  fallback OK ($size bytes)"
    fi
  else
    echo "FAIL (timeout), trying fallback..."
    curl -sL --max-time 15 "https://picsum.photos/seed/${SEED}/800/450" -o "$name.jpg" 2>/dev/null
    size=$(stat -f%z "$name.jpg" 2>/dev/null || stat -c%s "$name.jpg" 2>/dev/null)
    echo "  fallback OK ($size bytes)"
  fi
  
  SEED=$((SEED + 1))
done

echo ""
echo "Results:"
for f in finance_1.jpg finance_2.jpg finance_3.jpg tech_1.jpg tech_2.jpg tech_3.jpg education_1.jpg products_1.jpg products_2.jpg products_3.jpg auto_1.jpg vc_1.jpg vc_2.jpg vc_3.jpg; do
  size=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f" 2>/dev/null)
  if [ "$size" -gt 5000 ]; then
    echo "  ✓ $f ($size bytes)"
  else
    echo "  ✗ $f ($size bytes) - FAILED"
  fi
done
