#!/usr/bin/env python3
"""
Claude-integrated blog post generator
Combines existing blogger.py functionality with MJ-MCP art generation
"""

import os
import sys
import json
import datetime
import argparse
import subprocess
from pathlib import Path

# Import existing blogger functions
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from blogger import (
    generate_title, generate_filename, generate_header, 
    generate_metadata, generate_blog, reformat_tags,
    HEADER, METADATA, BLOG_TEMPLATE
)

def generate_mj_art(prompt: str, aspect_ratio: str = "16:9") -> str:
    """
    Generate art using Midjourney MCP
    Returns the image path or URL
    """
    try:
        # Call Claude with MCP to generate image
        cmd = [
            "claude", "api",
            "--tool", "midjourney.generating_image",
            "--prompt", prompt,
            "--aspect_ratio", aspect_ratio
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            # Parse the result to get image URL
            return json.loads(result.stdout).get("image_url", "")
        else:
            print(f"MJ generation failed: {result.stderr}")
            return ""
    except Exception as e:
        print(f"Error generating MJ art: {e}")
        return ""

def create_blog_post(content: str, use_mj: bool = True):
    """
    Create a complete blog post with optional MJ art generation
    """
    print("🟣 Dross's Blog Creation Protocol Activated!")
    
    # Generate blog components
    print("📝 Generating title...")
    title = generate_title(content)
    print(f"   Title: {title.title}")
    
    print("📅 Creating filename...")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = generate_filename(title.title, date)
    print(f"   Filename: {filename.filename}")
    
    print("🏷️ Assigning categories and tags...")
    header = generate_header(content)
    bulleted_tags = reformat_tags(header.tags)
    header_string = HEADER.format(
        title=title.title, 
        tags=bulleted_tags, 
        category=header.category.category
    )
    
    # Generate art
    image_path = ""
    if use_mj:
        print("🎨 Generating Midjourney artwork...")
        # Create art prompt based on content
        art_prompt = f"Black and white illustration for blog post about: {title.title}. Style: New Yorker magazine, Atlantic, minimalist, sophisticated --v 6.1"
        image_url = generate_mj_art(art_prompt)
        
        if image_url:
            # Download and save image
            image_filename = f"{date}-{title.title.lower().replace(' ', '-')}.png"
            image_path = f"assets/images/{image_filename}"
            print(f"   Image saved to: {image_path}")
        else:
            print("   ⚠️ MJ generation failed, continuing without image")
    
    # Add image to content if available
    if image_path:
        image_string = f"![](/{image_path}){{: width=\"400\" }}\n"
        content = f"{header_string}\n{image_string}\n{content}"
    else:
        content = f"{header_string}\n{content}"
    
    print("🔗 Generating metadata...")
    metadata = generate_metadata(filename.filename, content)
    metadata_string = METADATA.format(
        og_url=metadata.og_url,
        og_title=metadata.og_title,
        og_description=metadata.og_description,
        og_image=metadata.og_image if metadata.og_image else f"/{image_path}" if image_path else ""
    )
    
    # Assemble final blog
    full_blog = BLOG_TEMPLATE.format(
        content=content,
        metadata=metadata_string
    )
    
    # Save to file
    output_path = Path("tmp_posts") / filename.filename
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        f.write(full_blog)
    
    print(f"\n✅ Blog post created successfully!")
    print(f"📍 Location: {output_path}")
    print(f"\n🚀 Next steps:")
    print(f"   1. Review the post at {output_path}")
    print(f"   2. Move to _posts/ when ready to publish")
    print(f"   3. Commit and push to deploy")
    
    return output_path

def main():
    parser = argparse.ArgumentParser(description="Create blog posts with MJ art")
    parser.add_argument("--content", help="Blog content or topic")
    parser.add_argument("--no-art", action="store_true", help="Skip MJ art generation")
    parser.add_argument("--from-file", help="Read content from file")
    
    args = parser.parse_args()
    
    # Get content
    if args.from_file:
        with open(args.from_file, "r") as f:
            content = f.read()
    elif args.content:
        content = args.content
    else:
        print("Reading from stdin...")
        content = sys.stdin.read()
    
    # Generate blog post
    create_blog_post(content, use_mj=not args.no_art)

if __name__ == "__main__":
    main()