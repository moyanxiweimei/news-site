tell application "Safari"
	activate
	set searchURL to "https://www.baidu.com/s?wd=SpaceX星舰图片"
	make new document with properties {URL:searchURL}
	
	-- 等待页面加载
	delay 3
	
	-- 获取页面中的图片URL
	set jsScript to "
		var images = document.querySelectorAll('img');
		var imageUrls = [];
		for (var i = 0; i < images.length; i++) {
			if (images[i].src && images[i].src.includes('baidu.com')) {
				imageUrls.push(images[i].src);
			}
		}
		imageUrls.join(',');
	"
	set imageList to do JavaScript jsScript in front document
	
	return imageList
end tell
