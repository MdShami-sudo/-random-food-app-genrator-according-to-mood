import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
import numpy as np

class FoodDeliveryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Food Delivery App")
        self.root.geometry("500x400")
        
        # Create a gradient background
        self.create_gradient_background()
        
        # Add widgets
        self.add_widgets()

    def create_gradient_background(self):
        # Create a canvas to draw the gradient
        canvas = tk.Canvas(self.root, width=500, height=400)
        canvas.pack(fill="both", expand=True)
        
        # Create a gradient background
        gradient_color = self.create_linear_gradient((255, 182, 193, 255), (173, 216, 230, 255), 500, 400)  # Light Pink to Pastel Blue
        bg_image = Image.fromarray(gradient_color, 'RGBA')
        self.bg_photo = ImageTk.PhotoImage(image=bg_image)
        
        canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)
        
        # Create a frame on top of the canvas to hold the widgets
        self.frame = tk.Frame(canvas, width=500, height=400)
        self.frame.place(x=0, y=0, width=500, height=400)
    
    def create_linear_gradient(self, color1, color2, width, height):
        gradient = np.zeros((height, width, 4), dtype=np.uint8)
        for y in range(height):
            ratio = y / height
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            a = int(color1[3] * (1 - ratio) + color2[3] * ratio)
            gradient[y, :, :] = [r, g, b, a]
        return gradient

    def add_widgets(self):
        # Add a label
        label = tk.Label(self.frame, text="How are you feeling today?", font=("Arial", 16), fg='black')
        label.pack(pady=20)
        
        # Add a dropdown menu for mood selection
        self.mood_var = tk.StringVar()
        mood_options = ["Happy", "Sad", "Excited", "Bored", "Stressed"]
        mood_menu = ttk.Combobox(self.frame, textvariable=self.mood_var, values=mood_options, state="readonly")
        mood_menu.pack(pady=10)
        
        # Add a button to get the food suggestion
        suggest_button = tk.Button(self.frame, text="Suggest Food", command=self.suggest_food)
        suggest_button.pack(pady=20)
        
        # Add a label to display the food suggestion
        self.result_label = tk.Label(self.frame, text="", font=("Arial", 14), fg='black')
        self.result_label.pack(pady=20)

    def suggest_food(self):
        mood = self.mood_var.get()
        if mood:
            food_suggestions = {
                "Happy": ["Ice Cream", "Pizza", "Cupcakes", "Smoothies"],
                "Sad": ["Comfort Food", "Chocolate", "Soup", "Pasta"],
                "Excited": ["Sushi", "Tacos", "Burgers", "Fries"],
                "Bored": ["Snacks", "Popcorn", "Cookies", "Nachos"],
                "Stressed": ["Tea", "Salad", "Fruit", "Yogurt"]
            }
            food = random.choice(food_suggestions[mood])
            self.result_label.config(text=f"How about some {food}?")
        else:
            self.result_label.config(text="Please select your mood!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodDeliveryApp(root)
    root.mainloop()
