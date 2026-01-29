# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based personal blog for Joseph Thacker (josephthacker.com) using the Hydeout theme. The blog focuses on hacking, AI, cybersecurity, and personal content.

## Development Commands

### Local Development
```bash
bundle exec jekyll serve
# Serves the site locally at http://localhost:4000
```

### Building
```bash
bundle exec jekyll build
# Builds the site to _site/ directory
```

### Dependencies
```bash
bundle install
# Installs Ruby gems specified in Gemfile
```

### Blog Creation Tool
```bash
python blogger.py
# Interactive tool for creating new blog posts with AI assistance
# Reads content from stdin and generates full blog post with metadata
```

## Architecture

### Content Structure
- **Posts**: Located in `_posts/` with YAML frontmatter including title, layout, categories, and tags
- **Categories**: Limited to `personal`, `ai`, `hacking`, `cybersecurity`
- **Tags**: Include `personal`, `ai`, `hacking`, `cybersecurity`, `productivity`, `art`, `faith`
- **Assets**: Images stored in `assets/images/`, other assets in `assets/`

### Theme Structure
- **Layouts**: Custom layouts in `_layouts/` extending Hydeout theme
- **Includes**: Reusable components in `_includes/`
- **Sass**: Styling in `_sass/hydeout/` with main import in `assets/css/main.scss`

### Automated Blog Creation
The `blogger.py` script uses AI to:
- Generate blog content from raw input
- Create titles, categories, and tags
- Generate metadata for social sharing
- Create banner images using DALL-E
- Format Jekyll frontmatter

### File Naming Convention
Blog posts follow format: `YYYY-MM-DD-title-with-dashes.md`

## Key Files
- `_config.yml`: Main Jekyll configuration
- `blogger.py`: AI-powered blog creation tool
- `_layouts/post.html`: Blog post template
- `_includes/post-meta.html`: Post metadata display

## Content Guidelines
- Posts should include social media metadata at the bottom
- Images should be 400px width with proper attribution
- Categories are single-select, tags are multi-select
- All posts end with author signature and subscription links