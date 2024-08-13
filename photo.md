---
layout: archive
title: Photo
permalink: /photo/
author: Chris Brockett
author_profile: true
---


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Carousel</title>
    <link rel="stylesheet" href="{{ site.baseurl }}/assets/css/styles.css">
</head>
<body>
    <div class="carousel">
        <div class="carousel-inner" id="carouselInner">
            <!-- Images will be inserted here dynamically -->
        </div>
        <button class="prev" onclick="changeSlide(-1)">&#10094;</button>
        <button class="next" onclick="changeSlide(1)">&#10095;</button>
    </div>

    <script src="{{ site.baseurl }}/assets/js/scripts.js"></script>
</body>
</html>