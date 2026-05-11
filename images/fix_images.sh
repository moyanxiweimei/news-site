cd /Users/maxiaoxu/.openclaw/workspace/news-site/images

# Re-download all broken/mismatched images with stable random seeds
# Using picsum.photos which provides reliable, beautiful photography

curl -sL "https://picsum.photos/400/300?random=101" -o auto_1.jpg
curl -sL "https://picsum.photos/400/300?random=102" -o auto_2.jpg
curl -sL "https://picsum.photos/400/300?random=103" -o auto_3.jpg
curl -sL "https://picsum.photos/400/300?random=104" -o products_3.jpg
curl -sL "https://picsum.photos/400/300?random=105" -o medical_1.jpg
curl -sL "https://picsum.photos/400/300?random=106" -o finance_2.jpg
curl -sL "https://picsum.photos/400/300?random=107" -o aerospace_1.jpg

echo "Download complete. Validating..."
for f in auto_1.jpg auto_2.jpg auto_3.jpg products_3.jpg medical_1.jpg finance_2.jpg aerospace_1.jpg; do
  size=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f" 2>/dev/null)
  valid=$(file "$f" | grep -c "JPEG image")
  echo "$f: ${size} bytes, valid=$valid"
done
