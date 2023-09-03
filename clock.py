
# Import the necessary modules
from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route that generates HTML
@app.route('/')
def generate_html():
    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Changing Clock</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #000;
        }

        #clock {
            font-size: 48px;
            color: #fff;
            transition: color 2s ease-in-out;
        }
    </style>
</head>
<body>
    <div id="clock"></div>
    <script>
        function updateClock() {
            const clockElement = document.getElementById('clock');
            const now = new Date();
            const hours = now.getHours();
            const minutes = now.getMinutes();
            const seconds = now.getSeconds();

            // Change clock color every hour
            const colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff'];
            const colorIndex = hours % colors.length;
            const clockColor = colors[colorIndex];

            // Format the time as HH:MM:SS
            const timeString = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

            clockElement.textContent = timeString;
            clockElement.style.color = clockColor;
        }

        // Update the clock every second
        setInterval(updateClock, 1000);

        // Initial call to set the clock
        updateClock();
    </script>
</body>
</html>

    """
    return html_content

if __name__ == '__main__':
    app.run(debug = True)