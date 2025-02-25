---
layout: emoji_variation
title: Unicode Variation Selector Data Hiding
---

A tool for hiding arbitrary data within Unicode characters using variation selectors (VS1-VS256). Based on [Paul Butler's technique](https://paulbutler.org/2025/smuggling-arbitrary-data-through-an-emoji/), this tool allows you to encode any data into invisible variation selectors attached to a visible character. The data becomes completely invisible when rendered but can be extracted later.

This works by using Unicode's variation selector codepoints (U+FE00 through U+FE0F and U+E0100 through U+E01EF) to encode bytes of data. Since variation selectors are meant to be invisible and preserved during text operations, they create a perfect hiding place for arbitrary data. 