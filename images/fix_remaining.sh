cd /Users/maxiaoxu/.openclaw/workspace/news-site/images

# Fix remaining mismatched images with better Unsplash matches
# Electric vehicle / charging for auto_2 (蔚来乐道换电站)
curl -sL "https://images.unsplash.com/photo-1593941707882-a5bba14938c7?w=400&h=300&fit=crop" -o auto_2.jpg

# Hair/beauty appliance for products_3 (吹风机)
curl -sL "https://images.unsplash.com/photo-1522338140262-f46f3e580151?w=400&h=300&fit=crop" -o products_3.jpg

# Android phone / mobile for medical_1 (OPPO - Android brand)
curl -sL "https://images.unsplash.com/photo-1512054502232-10a0a035d672?w=400&h=300&fit=crop" -o medical_1.jpg

echo "Done. Validating:"
for f in auto_2.jpg products_3.jpg medical_1.jpg; do
  size=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f" 2>/dev/null)
  type=$(file "$f" | grep -c "JPEG")
  echo "$f: $size bytes, JPEG=$type"
done
