import display

def main():
    # Create display object
    display1 = display.display()
    display1.draw_interface()
    # Start the loop
    display1.window.mainloop()

if __name__ == "__main__":
    main()