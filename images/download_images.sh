#!/bin/bash
# Download images from sogou with proper search queries

cd /Users/maxiaoxu/.openclaw/workspace/news-site/images

# Function to download image from sogou
download_from_sogou() {
    local query="$1"
    local output="$2"
    
    echo "Searching: $query"
    
    # Get image URLs from sogou
    local urls=$(curl -sL -k --max-time 30 "https://pic.sogou.com/pics?query=${query}" | grep -o 'https://img[0-9]*.sogoucdn.com/[^"]*' | head -3)
    
    # Try each URL
    local success=false
    for url in $urls; do
        echo "Trying: $url"
        curl -sL -k --max-time 30 -o "$output" "$url"
        
        # Check if download succeeded and file is valid
        if [ -f "$output" ] && [ $(stat -f%z "$output" 2>/dev/null || stat -c%s "$output" 2>/dev/null) -gt 10000 ]; then
            # Check if it's a valid image
            if file "$output" | grep -q "image"; then
                echo "✓ Downloaded: $output"
                success=true
                break
            fi
        fi
    done
    
    if [ "$success" = false ]; then
        echo "✗ Failed to download: $output"
    fi
}

# Download images
download_from_sogou "SpaceX星舰发射" "aerospace_2.jpg"
download_from_sogou "中国卫星发射" "aerospace_3.jpg"
download_from_sogou "人工智能教育课堂" "education_1.jpg"
download_from_sogou "ChatGPT聊天机器人" "education_2.jpg"
download_from_sogou "VR眼镜虚拟现实" "education_3.jpg"
download_from_sogou "基因编辑DNA" "medical_2.jpg"
download_from_sogou "智能手环健康监测" "medical_3.jpg"
download_from_sogou "创业公司投资" "vc_2.jpg"

echo ""
echo "Download summary:"
ls -la aerospace_2.jpg aerospace_3.jpg education_1.jpg education_2.jpg education_3.jpg medical_2.jpg medical_3.jpg vc_2.jpg