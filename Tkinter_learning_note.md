# Window
- 可以開多個window喔喔喔喔，就是創建多個instance，然後都呼叫mainloop()即可
- 調整大小：```.resizable(width, height)```
- 限制可調整大小：```.minsize(...)```、```.maxsize(...)```
- 調整透明度：```.attributes('-alpha', 0.5)```

# Widget
- create: 
    ```python
    widget = WidgetName(master, **options)
    e.g., msg = Label(root, "Hello world!")
    ```
- display: create does not display
    ```msg.pack()```
- font: 字體要特別設置，不能直接整個window設置