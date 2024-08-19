---
layout: archive
title: Photography and Nature
permalink: /photo/
author: Chris Brockett
author_profile: true
---
I love being out in nature and snapping pictures.  Enjoy the show (yes there will be alot of sunsets :smiley:)

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Picture Carousel</title>
    <style>
        .carousel {
            display: flex;
            overflow: hidden;
            width: 50%;
            height: 50%;
            margin: auto;
            position: relative;
        }
        .carousel img {
            min-width: 100%;
            transition: transform 0.5s ease;
        }
        .buttons {
            display: flex;
            justify-content: center;
            margin-top: 10px;
        }
        .buttons button {
            margin: 0 5px;
        }
    </style>
</head>
<body>
    <div class="carousel">
        <img src="/assets/images/barn.jpg" alt="image 1">
        <img src="/assets/images/sset1.jpg" alt="image 2">
        <img src="/assets/images/waterfall.jpg" alt="image 3">
        <img src="/assets/images/sand.jpg" alt="image 4">
        <img src="https://i.imgur.com/ngUGA5d.jpg" alt="image 5">
        <img src="https://i.imgur.com/GPymVn9.jpg" alt="image 6">
        <img src="https://i.imgur.com/rtdtYHd.jpg" alt="image 7">
        <img src="https://i.imgur.com/5ZlhhD2.jpg" alt="image 8">
        <img src="https://i.imgur.com/G1iu0MR.jpg" alt="image 9">
        <img src="https://i.imgur.com/P2tjJ5K.jpg" alt="image 10">
    </div>
    <div class="buttons">
        <button onclick="prev()">Previous</button>
        <button onclick="next()">Next</button>
    </div>

    <script>
        let index = 0;
        const images = document.querySelectorAll('.carousel img');
        const totalImages = images.length;

        function showImage(idx) {
            images.forEach((img, i) => {
                img.style.transform = `translateX(${-(idx * 100)}%)`;
            });
        }

        function next() {
            index = (index + 1) % totalImages;
            showImage(index);
        }

        function prev() {
            index = (index - 1 + totalImages) % totalImages;
            showImage(index);
        }

        showImage(index);
    </script>


<br>
Want to see more sunsets then check out my gallery <a href="https://imgur.com/gallery/sunsets-nPLufLn" target="blank">here</a> or see some <a href= "https://imgur.com/gallery/critters-7dCcZGX" target = "blank"> critters</a>.
</body>
</html>