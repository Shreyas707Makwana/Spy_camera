from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('basic.html')

@app.route('/run_main_py')
def run_main_py():
    import tkinter as tk
    import tkinter.font as font
    from in_out import in_out
    from motion import noise
    from rect_noise import rect_noise
    from record import record
    from PIL import Image, ImageTk

    window = tk.Tk()
    window.title("Spy Camera")
    window.iconphoto(False, tk.PhotoImage(file='mn.png'))
    window.geometry('1080x760')

    window.configure(bg='black')
    frame1 = tk.Frame(window,bg='black')

    label_title = tk.Label(frame1, text="Spy Camera",bg='#ff7200')
    label_font = font.Font(size=35, weight='bold',family='Helvetica')
    label_title['font'] = label_font
    label_title.grid(pady=(10,10), column=2)

    icon = Image.open('icons/spy.png')
    icon = icon.resize((150,150), Image.LANCZOS)
    icon = ImageTk.PhotoImage(icon)
    label_icon = tk.Label(frame1, image=icon,bg='#ff7200')
    label_icon.grid(row=1, pady=(5,10), column=2)

  


    btn5_image = Image.open('icons/exit.png')
    btn5_image = btn5_image.resize((50,50), Image.LANCZOS)
    btn5_image = ImageTk.PhotoImage(btn5_image)

    btn3_image = Image.open('icons/security-camera.png')
    btn3_image = btn3_image.resize((50,50), Image.LANCZOS)
    btn3_image = ImageTk.PhotoImage(btn3_image)

    btn6_image = Image.open('icons/incognito.png')
    btn6_image = btn6_image.resize((50,50), Image.LANCZOS)
    btn6_image = ImageTk.PhotoImage(btn6_image)

    btn4_image = Image.open('icons/recording.png')
    btn4_image = btn4_image.resize((50,50), Image.LANCZOS)
    btn4_image = ImageTk.PhotoImage(btn4_image)

    
    btn_font = font.Font(size=25)



    btn_font = font.Font(size=25)
    btn3 = tk.Button(frame1, text='Noise', height=90, width=180, fg='black', bg='#ff7200' ,command=noise, image=btn3_image, compound='left')
    btn3['font'] = btn_font
    btn3.grid(row=5, pady=(20,10))

    btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='black',bg='#ff7200' , command=record, image=btn4_image, compound='left')
    btn4['font'] = btn_font
    btn4.grid(row=5, pady=(20,10), column=3)

    btn6 = tk.Button(frame1, text='In Out', height=90, width=180, fg='black', bg='#ff7200' ,command=in_out, image=btn6_image, compound='left')
    btn6['font'] = btn_font
    btn6.grid(row=4, pady=(20,10), column=2)

    btn5 = tk.Button(frame1, height=90, width=180, fg='black',bg='#ff7200' , command=window.quit, image=btn5_image)
    btn5['font'] = btn_font
    btn5.grid(row=6, pady=(20,10), column=2)

    frame1.pack()
    window.mainloop()

    return jsonify({'message': 'main.py executed successfully'})

if __name__ == '__main__':
    app.run(debug=True)
