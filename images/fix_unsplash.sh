cd /Users/maxiaoxu/.openclaw/workspace/news-site/images

# Use specific Unsplash images with known content
# Car-related
curl -sL "https://images.unsplash.com/photo-1544636331-e26879cd4d9b?w=400&h=300&fit=crop" -o auto_1.jpg
curl -sL "https://images.unsplash.com/photo-1502877338535-766e1452684a?w=400&h=300&fit=crop" -o auto_2.jpg
curl -sL "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?w=400&h=300&fit=crop" -o auto_3.jpg

# Product/electronics
curl -sL "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&h=300&fit=crop" -o products_3.jpg

# Phone/tech
curl -sL "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=300&fit=crop" -o medical_1.jpg

# Chip/tech
curl -sL "https://images.unsplash.com/photo-1518770660439-4636190af475?w=400&h=300&fit=crop" -o finance_2.jpg

# Space/rocket
curl -sL "https://images.unsplash.com/photo-1446776811953-b23d57bd21ee?w=400&h=300&fit=crop" -o aerospace_1.jpg

echo "Done. Validating:"
for f in auto_1.jpg auto_2.jpg auto_3.jpg products_3.jpg medical_1.jpg finance_2.jpg aerospace_1.jpg; do
  size=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f" 2>/dev/null)
  type=$(file "$f" | grep -c "JPEG")
  echo "$f: $size bytes, JPEG=$type"
done
