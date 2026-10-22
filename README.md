# ⏱️ Stopwatch

A simple desktop stopwatch application built with **Python** and **PyQt5**.

The application provides an easy way to measure elapsed time with start, stop, and reset controls. The timer displays hours, minutes, seconds, and hundredths of a second.

## ✨ Features

- ▶️ Start the stopwatch
- ⏸️ Stop the timer
- 🔄 Reset the elapsed time
- ⏱️ Display time with hundredths of a second
- 🎨 Simple and clean graphical user interface
- ⚡ Automatic display updates every 10 milliseconds

## 🛠️ Technologies

- **Python** — application logic
- **PyQt5** — graphical user interface
- **QTimer** — periodic timer updates
- **QTime** — time representation and formatting

## 📸 Preview

*Add a screenshot of your application here.*

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/stopwatch.git
```

### 2. Navigate to the project directory

```bash
cd stopwatch
```

### 3. Install dependencies

```bash
pip install PyQt5
```

### 4. Run the application

```bash
python main.py
```

## 📂 Project Structure

```text
stopwatch/
│
├── main.py       # Main application
├── README.md     # Project documentation
└── .gitignore    # Files excluded from Git
```

## ⚙️ How It Works

1. Click **Start** to begin measuring time.
2. Click **Stop** to pause the stopwatch.
3. Click **Start** again to continue from the current time.
4. Click **Reset** to stop the timer and return the display to zero.

The display uses the following format:

`HH:MM:SS.hh`

Where:
- `HH` — hours
- `MM` — minutes
- `SS` — seconds
- `hh` — hundredths of a second

## 🔮 Future Improvements

- [ ] Add a lap time feature
- [ ] Improve the user interface
- [ ] Add keyboard shortcuts
- [ ] Add a dark mode
- [ ] Improve timing accuracy using elapsed-time measurements

## 👨‍💻 Author

**YOUR NAME**

- GitHub: [@YOUR-USERNAME](https://github.com/YOUR-USERNAME)

---

*Built with Python as a portfolio project.*