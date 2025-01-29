import tkinter as tk


MAXSIZE = 4
class CircularQueue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.arr = [None] * MAXSIZE  # Initialize a fixed-size list
        self.first_element = False
        self.last_element = False

    def isFull(self):
        return (self.rear + 1) % MAXSIZE == self.front

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, num):
        if self.isFull():
            print("OVERFLOW")
            return
        else:
            if self.isEmpty():  # First element to be added
                self.front = self.rear = 0

            else:

                self.rear = (self.rear + 1) % MAXSIZE
            self.arr[self.rear] = num

    def dequeue(self):
        if self.isEmpty():
            print("UNDERFLOW")
            return None
        else:
            temp = self.arr[self.front]
            if self.front == self.rear:  # Queue becomes empty
                self.front = self.rear = -1

            else:
                self.front = (self.front + 1) % MAXSIZE

            return temp

    def display(self):
        if self.isEmpty():
            print("UNDERFLOW")
            return
        else:
            start = self.front
            while True:
                print(self.arr[start], end=" ")
                if start == self.rear:
                    break
                start = (start + 1) % MAXSIZE
            print()  # Newline for better output formatting


# Testing the CircularQueue class
q = CircularQueue()

root = tk.Tk()
root.geometry("500x400")
root.title("Circular Queue Visualizer")
root.configure(bg='white')
root.resizable(False, False)

# box_img = Image.open("Boxes.png")
# box_img = box_img.resize((200,200))
# box_img = ImageTk.PhotoImage(box_img)
# image_label = tk.Label(root, image=box_img)
# image_label.pack(pady=100)
#
# label = tk.Label(root, text=q.arr[0], font=("Arial", 16))
# label.place(x=336, y=170)
#
# label = tk.Label(root, text=q.arr[1], font=("Arial", 16))
# label.place(x=336+40*1, y=170)
#
# label = tk.Label(root, text=q.arr[2], font=("Arial", 16))
# label.place(x=336+40*2, y=170)
#
# label = tk.Label(root, text=q.arr[3], font=("Arial", 16))
# label.place(x=336+40*3, y=170)


def start_animation():
    # Get the user-provided number
    user_number = entry.get()
    if not user_number.isdigit():
        label_status.config(text="Please enter a valid number.", fg="red")
        return

    label_status.config(text="")  # Clear any error messages

    if not q.isFull():
        print(f"Is empty?={q.isEmpty()}")
        if q.isEmpty():
            q.first_element=True

        q.enqueue(user_number)
        q.display()
        r = q.rear
        end_x1, end_y1, end_x2, end_y2 = 50 + r * 50, 50, 100 + r * 50, 100
        animate_rf()
        q.first_element = False
    else:
        label_status.config(text="Queue is full.", fg="red")
        return

    # Define the starting rectangle position
    start_x1, start_y1, start_x2, start_y2 = 0, 50, 50, 100

    # Create the box with the number
    box = canvas.create_rectangle(start_x1, start_y1, start_x2, start_y2, fill="blue", outline="black")
    text = canvas.create_text((start_x1 + start_x2) // 2, (start_y1 + start_y2) // 2, text=user_number, fill="white", font=("Arial", 16))

    # Animate the box to the positioned rectangle
    for _ in range(start_x1, end_x1, 5):
        canvas.move(box, 5, 0)
        canvas.move(text, 5, 0)
        canvas.update()
        canvas.after(50)  # Delay for smooth animation

def start_deleteanimation():
    label_status.config(text="")  # Clear any error messages
    if not q.isEmpty():
        print(f"rear={q.rear} front={q.front}")
        if q.rear==q.front:
            q.last_element=True

        f = q.front
        start_x1, start_y1, start_x2, start_y2 = 50 + 50 * f, 50, 100 + 50 * f, 100
        q.dequeue()

        q.display()

        box = canvas.create_rectangle(start_x1, start_y1, start_x2, start_y2, fill="white", outline="black")
        animate_rf()
        q.last_element = False
    else:
        label_status.config(text="Queue is empty.", fg="red")
        return

# def start_rear_animation():
#     global f_xaxis
#     temp = 0
#     global r_xaxis
#
#     if f_xaxis==25 and r_xaxis==25:
#         first_entry=True
#     else:
#         first_entry=False
#     start_x1 = r_xaxis
#     end_x1 = r_xaxis + 50
#     for _ in range(start_x1, end_x1, 5):
#
#         if first_entry:
#             canvas.move(text_f, 5, 0)
#             temp=50
#
#         canvas.move(text_r, 5, 0)
#         canvas.update()
#         canvas.after(50)  # Delay for smooth animation
#     r_xaxis = end_x1
#
#     f_xaxis = f_xaxis + temp
#
# def start_front_animation():
#     global r_xaxis
#     global f_xaxis
#
#     if f_xaxis==175 and r_xaxis==175:
#         last_exit=True
#     else:
#         last_exit=False
#
#     start_x1 = f_xaxis
#
#     if last_exit:
#         end_x1 = 25
#     else:
#         end_x1 = f_xaxis + 50
#     for _ in range(start_x1, end_x1, 5):
#
#         canvas.move(text_f, 5, 0)
#         canvas.update()
#         canvas.after(50)  # Delay for smooth animation
#     f_xaxis = end_x1

def animate_rf():
    global r_xaxis
    global f_xaxis
    start_xr=r_xaxis
    start_xf=f_xaxis

    print(f"First element?={q.first_element} Last element?={q.last_element}")

    if q.first_element:
        print(f"start of r={start_xr} start of f={start_xf}")

        end_x = 75
        for _ in range(start_xr, end_x, 5):
            canvas.move(text_r, 5, 0)
            canvas.move(text_f, 5, 0)
            canvas.update()
            canvas.after(50)
        #start_xr = start_xf = 75
        r_xaxis = r_yaxis = 75
        print(f"start of r={start_xr} start of f={start_xf}")
        return
    if q.last_element:
        print(f"start of r={start_xr} start of f={start_xf}")
        end_x = 25
        for _ in range(start_xr, end_x, -5):
            canvas.move(text_r, -5, 0)
            canvas.move(text_f, -5, 0)
            canvas.update()
            canvas.after(50)
        #start_xr = start_xf = 25
        r_xaxis = r_yaxis = 25
        print(f"start of r={start_xr} start of f={start_xf}")
        return
    print(f"rear={q.rear} front={q.front}")
    end_xr = 25 + 50*(q.rear+1)
    end_xf = 25 + 50*q.front
    print(f"start of r={start_xr} start of f={start_xf}")
    print(f"end of r={end_xr} end of f={end_xf}")
    if start_xf<end_xr or start_xf<end_xf:
        direction=1
    else:
        direction=-1
    if direction==1:
        for _ in range(start_xr, end_xr, 5):
            canvas.move(text_r, 5, 0)
            canvas.update()
            canvas.after(50)
        for _ in range(start_xf, end_xf, 5):
            canvas.move(text_f, 5, 0)
            canvas.update()
            canvas.after(50)
    if direction==-1:
        for _ in range(start_xr, end_xr, -5):
            canvas.move(text_r, -5, 0)
            canvas.update()
            canvas.after(50)
        for _ in range(start_xf, end_xf, 5):
            canvas.move(text_f, -5, 0)
            canvas.update()
            canvas.after(50)
    r_xaxis=end_xr
    f_xaxis=end_xf
    print(f"start of r={r_xaxis} start of f={f_xaxis}")


# Input field for the number
frame = tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame, text="Enter a number:").pack(side="left")
entry = tk.Entry(frame, width=10)
entry.pack(side="left")

tk.Button(frame, text="Insert", command=start_animation).pack(side="left")

tk.Button(frame, text="Delete", command=start_deleteanimation).pack(side="left")

# Status label for feedback
label_status = tk.Label(root, text="", fg="red")
label_status.pack()

# Create a Canvas widget
canvas = tk.Canvas(root, width=300, height=150, bg="white", bd=0)
canvas.pack(pady=60)

# Draw rectangles in a vertical queue
canvas.create_rectangle(50, 50, 100, 100, fill="white", outline="black")
canvas.create_rectangle(100, 50, 150, 100, fill="white", outline="black")
canvas.create_rectangle(150, 50, 200, 100, fill="white", outline="black")
canvas.create_rectangle(200, 50, 250, 100, fill="white", outline="black")

# Draw index above
text = canvas.create_text(25, 38, text="-1", fill="black", font=("Arial", 16))
text = canvas.create_text(75, 38, text="0", fill="black", font=("Arial", 16))
text = canvas.create_text(125, 38, text="1", fill="black", font=("Arial", 16))
text = canvas.create_text(175, 38, text="2", fill="black", font=("Arial", 16))
text = canvas.create_text(225, 38, text="3", fill="black", font=("Arial", 16))

# Draw rear and front
r_xaxis=25
r_yaxis=18
f_xaxis=25
f_yaxis=118
text_r = canvas.create_text(r_xaxis, r_yaxis, text="r", fill="red", font=("Arial", 16))
text_f = canvas.create_text(f_xaxis, f_yaxis, text="f", fill="blue", font=("Arial", 16))

# Run the Tkinter event loop
root.mainloop()
