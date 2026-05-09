import requests
import zipfile
import os
import json

# Netlify Drop API - no auth required for manual deploys!
# We'll use Netlify's deploy API with a public upload

def deploy_to_netlify(site_dir):
    """Deploy a static site to Netlify using their manual deploy API"""
    
    # Create a zip file of the site
    zip_path = '/tmp/news-site.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(site_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, site_dir)
                zf.write(file_path, arcname)
    
    # Netlify manual deploy API
    url = "https://api.netlify.com/api/v1/sites"
    
    # First create a site
    headers = {
        "Content-Type": "application/json"
    }
    
    # Netlify allows unauthenticated deploys to temporary sites
    # We use their deploys endpoint
    print("Creating deploy...")
    
    # Upload the zip file
    with open(zip_path, 'rb') as f:
        deploy_url = "https://api.netlify.com/api/v1/sites"
        files = {'file': ('news-site.zip', f, 'application/zip')}
        
        response = requests.post(
            "https://api.netlify.com/api/v1/sites",
            files=files,
            headers={"Content-Type": "multipart/form-data"}
        )
    
    print(f"Response status: {response.status_code}")
    print(f"Response: {response.text[:500]}")
    
    if response.status_code in [200, 201]:
        data = response.json()
        site_url = data.get('url')
        print(f"Deployed to: {site_url}")
        return site_url
    else:
        print("Deploy failed")
        return None

if __name__ == '__main__':
    site_dir = '/Users/maxiaoxu/.openclaw/workspace/news-site'
    deploy_to_netlify(site_dir)
