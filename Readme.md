# Worm Editor 
A simple text editor based on Tkinter.

# To-do
## Basic functionality
- [x] Basic window
    - [x] Text area
        - [x] Undo/Redo
- [x] New file / Open file 
    - [x] ctrl+n -> new file 
    - [x] Avoid same file name
        - [x] New file(idx) 
        - [x] Open file(path) 
    - [x] Switch to new opened file
- [x] Close file
    - [x] ctrl+w
    - [x] Remove file path for "same file name" situation if needed
- [ ] Save file
    - [x] ctrl+x
    - [ ] Auto save
- [ ] Refresh file
    - [x] ctrl+r
    - [x] Maintain cursor position 
    - [ ] Auto refresh
- [ ] Add hotkey description in the menu
- [ ] Latex & Markdown support

## Decoration
- [x] Font
    - [x] Family
    - [x] Size
        - [x] ctrl +-
    - [ ] Add recommanded/recently-used font
- [x] Theme

## Advanced functionality
- [ ] Configuration file for default settings
- [ ] Wrong word detection/correction
- [ ] Coding tool
- [ ] Combine with [Simple Remote Workstation](https://github.com/luckyjp6/Simple-remote-workstation) to make it something like remote desktop.