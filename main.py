import asyncio
import tkinter as tk
from gui.gui import GUI
import customtkinter as ctk

async def main():
    # Create the root window
    root = ctk.CTk()
    gui = GUI(root)

    # Run the GUI
    gui.run()

    # Start the event loop
    await asyncio.get_event_loop().run_in_executor(None, root.mainloop)

if __name__ == '__main__':
    # Run the main function in the event loop
    asyncio.run(main())





