import os

# HTML, SVG, CSS, and JavaScript content for the animation
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ciphertronix Animation</title>
    <link href="https://fonts.googleapis.com/css2?family=Sacramento&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: #000; /* Black background for Mac-like contrast */
            overflow: hidden;
        }
        .container {
            text-align: center;
        }
        svg {
            width: 600px;
            height: 200px;
        }
        text {
            font-family: 'Sacramento', cursive;
            font-size: 100px;
            fill: transparent;
            stroke: url(#gradient);
            stroke-width: 2;
            stroke-dasharray: 2000;
            stroke-dashoffset: 2000;
            animation: draw 5s ease-in-out forwards, gradient 6s linear infinite;
        }
        @keyframes draw {
            to {
                stroke-dashoffset: 0;
            }
        }
        @keyframes gradient {
            0% { stop-color: #2da9da; }    /* Vibrant blue */
            100% { stop-color: #aef055; }  /* Bright greenish-yellow */
        }
    </style>
</head>
<body>
    <div class="container">
        <svg viewBox="0 0 600 200">
            <defs>
                <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" style="stop-color:#2da9da;" />
                    <stop offset="100%" style="stop-color:#aef055;" />
                </linearGradient>
            </defs>
            <text x="50" y="150">Ciphertronix</text>
        </svg>
    </div>
    <script>
        // Restart animation on click
        const text = document.querySelector('text');
        text.addEventListener('click', () => {
            text.style.animation = 'none';
            void text.offsetWidth; // Trigger reflow
            text.style.animation = 'draw 5s ease-in-out forwards, gradient 6s linear infinite';
            text.style.strokeDashoffset = '2000';
        });
    </script>
</body>
</html>
"""

# Write the HTML content to a file
output_file = "ciphertronix_animation.html"
with open(output_file, "w") as f:
    f.write(html_content)

# Open the file in the default browser
if os.name == "nt":  # Windows
    os.startfile(output_file)
elif os.name == "posix":  # macOS or Linux
    os.system(f"open {output_file}" if sys.platform == "darwin" else f"xdg-open {output_file}")

print(f"Animation generated! Check '{output_file}' in your browser.")