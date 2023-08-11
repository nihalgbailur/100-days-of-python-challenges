import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    if city:
        api_key = 'YOUR_API_KEY'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if data.get('main'):
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            result_label.config(text=f"Temperature: {temperature}°C\nDescription: {description}")
        else:
            result_label.config(text="City not found")

# Create the main application window
app = tk.Tk()
app.title("Weather App")

# Create an entry for city input
city_entry = tk.Entry(app)
city_entry.pack(pady=10)

# Create a button to get weather
get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack()

# Create a label to display weather result
result_label = tk.Label(app, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Start the application event loop
app.mainloop()

