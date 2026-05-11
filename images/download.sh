#!/bin/bash
set -e

IMGDIR="$HOME/.openclaw/workspace/news-site/images"
cd "$IMGDIR"

# Array of: filename "prompt text"
declare -a images=(
  "finance_2:Hong Kong skyline businessman corporate real estate"
  "finance_3:BMW car factory automotive manufacturing electric vehicle"
  "tech_2:robotic hand mechanical gripper precision technology"
  "tech_3:humanoid robot android futuristic walking"
  "medical_1:AI medical diagnosis doctor tablet X-ray hospital"
  "medical_2:DNA gene editing CRISPR laboratory biotechnology"
  "medical_3:smartwatch health monitoring wearable device"
  "medical_4:medicine pills pharmacy healthcare drugs"
  "medical_5:brain neural network neuroscience implant"
  "education_1:AI classroom robot teaching students education"
  "education_2:university students computer campus library"
  "education_3:VR headset virtual reality immersive learning"
  "education_4:vocational training workshop technical school"
  "education_5:after school tutoring children studying"
  "aerospace_1:rocket launch space fire night"
  "aerospace_2:SpaceX starship rocket landing mechanical arms"
  "aerospace_3:satellite space orbit earth constellation"
  "aerospace_4:moon lunar surface astronaut exploration"
  "aerospace_5:supersonic jet airplane aviation flight"
  "products_1:home appliances electronics modern kitchen"
  "products_2:gaming smartphone mobile RGB lights"
  "auto_1:Brazil Rio de Janeiro Christ Redeemer travel"
  "auto_2:electric car factory manufacturing automotive"
  "vc_1:startup office technology AI business"
  "vc_2:video creation studio content creator editing"
)

SEED=200
echo "Downloading 25 images from pollinations.ai..."

for item in "${images[@]}"; do
  name="${item%%:*}"
  prompt="${item#*:}"
  encoded=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$prompt'))")
  url="https://image.pollinations.ai/prompt/${encoded}?width=800&height=450&seed=${SEED}&nologo=true"
  
  echo -n "  $name.jpg ... "
  if curl -sL --max-time 45 "$url" -o "$name.jpg"; then
    size=$(stat -f%z "$name.jpg" 2>/dev/null || stat -c%s "$name.jpg" 2>/dev/null)
    if [ "$size" -gt 5000 ]; then
      echo "OK ($size bytes)"
    else
      echo "FAIL (too small: $size bytes)"
    fi
  else
    echo "FAIL (download error)"
  fi
  
  SEED=$((SEED + 1))
done

echo "Done. Checking results:"
for f in *.jpg; do
  size=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f" 2>/dev/null)
  if [ "$size" -gt 5000 ]; then
    echo "  ✓ $f ($size bytes)"
  else
    echo "  ✗ $f ($size bytes) - FAILED"
  fi
done
