# 🚀 PRODIGY_CS_03

## 📝 Task Overview

**Task:** Build a Password Complexity Checker  
**Description:** Develop a Python tool that evaluates the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide detailed feedback to users on password strength and calculate the estimated time required to crack the password using entropy-based analysis.  
**Status:** ✅ Completed

---

## 🌟 Features

### 🔒 **Comprehensive Password Evaluation**
- **Criteria Check:** Password is evaluated based on the following criteria:
  - Minimum length of 8 characters.
  - Presence of at least one uppercase letter.
  - Presence of at least one lowercase letter.
  - Presence of at least one number.
  - Presence of at least one special character.
- **Detailed Feedback:** Specific suggestions are provided for improving password strength.

### 🌌 **Entropy Calculation and Crack Time Estimation**
- **Entropy Calculation:** Measures the randomness of the password, taking into account the character pool size and password length.
- **Crack Time Estimation:** Uses entropy to calculate the time required to crack the password based on a realistic attack rate (10 billion guesses per second).
- **Formatted Output:** Provides time estimates in human-readable formats (e.g., seconds, minutes, years).

### 📊 **Visual Representation**
- **Bar Chart for Strength:** Displays the password strength level using a color-coded bar chart.
  - Green for strong passwords.
  - Red for weak passwords.

### 🖥️ **Interactive GUI**
- **Tkinter-Based GUI:** A user-friendly graphical interface allows users to input passwords, view feedback, and visualize strength.
- **Show/Hide Password:** Option to toggle password visibility.

---

## 📦 Dependencies

This project requires the following Python modules:
- **math**: For entropy calculations.
- **tkinter**: For building the GUI.
- **matplotlib**: For plotting the bar chart.

---

## 📥 Installation Instructions

### 1. Install Python
Ensure Python 3.6 or later is installed. Download it from the [official Python website](https://www.python.org/downloads/).

### 2. Install Required Modules

#### For `matplotlib`:
```bash
pip install matplotlib
```

#### For `tkinter` (Linux systems only):
```bash
sudo apt-get install python3-tk
```

---

## ▶️ Usage Instructions

1. 📂 Clone the repository:
   ```bash
   git clone https://github.com/idPriyanshu/PRODIGY_CS_03.git
   ```

2. 📂 Navigate to the project directory:
   ```bash
   cd PRODIGY_CS_03
   ```

3. ▶️ Run the program:
   ```bash
   python password_checker.py
   ```

---

## 📜 How It Works

1. **Input Password:** Users input a password into the GUI.
2. **Check Criteria:** The tool evaluates the password based on defined criteria and provides feedback.
3. **Entropy Calculation:** The entropy of the password is calculated using the formula:
   ```
   entropy = len(password) * log2(pool_size)
   ```
   Where `pool_size` is the size of the character pool (e.g., uppercase, lowercase, numbers, special characters).
4. **Crack Time Estimation:** Estimates the time to crack the password using the formula:
   ```
   time_to_crack = 2 ** entropy / guesses_per_second
   ```
5. **Strength Visualization:** Displays the strength level on a bar chart.

---

## ✨ Example Output

### Input: `Password@123`

**Output:**
- Password Strength: Strong
- Feedback:
  - No feedback required (password meets all criteria).
- Estimated Time to Crack: 13000 centuries
- Visual Chart:
  - A green bar indicating strong password strength.

---

## 🔧 Customization

- **Adjust Guessing Rate:** Modify the `guesses_per_second` variable in the code to simulate different attack scenarios.
- **Criteria Thresholds:** Update the length or other password criteria in the `password_strength` function.
- **Add New Features:** Extend the tool to support additional checks, like detecting dictionary words.

---

## 🛠️ Challenges & Solutions

### 1. **Entropy Calculation**
**Challenge:** Accurately calculate entropy while accounting for character pool size.
**Solution:** Used character sets (lowercase, uppercase, digits, special characters) to dynamically determine the pool size.

### 2. **Dynamic Feedback**
**Challenge:** Provide real-time, actionable feedback based on password evaluation.
**Solution:** Implemented a modular design that checks each criterion separately and appends specific suggestions to a feedback list.

### 3. **Visual Representation**
**Challenge:** Create an intuitive and visually appealing representation of password strength.
**Solution:** Integrated `matplotlib` for dynamic bar chart plotting based on strength levels.

---

## 🌟 Future Improvements

- Add support for advanced password analysis, such as:
  - Identifying common patterns (e.g., repeated characters, dictionary words).
  - Checking against breached password databases.
- Enhance GUI with additional customization options and themes.
- Export results to a report file (e.g., PDF or CSV).

---

## 📂 Repository Structure

```
PRODIGY_CS_03/
├── password_checker.py   # Main Python script
├── README.md             # Documentation file
└── requirements.txt      # List of dependencies
```

---

## 🏆 Credits

- **Developer:** [@idPriyanshu](https://www.github.com/idPriyanshu) 
- **Mentorship:** Prodigy InfoTech Cyber Security Internship Program  

---

## 📧 Contact

For queries or suggestions, reach out at [iiit.Priyanshu@gmail.com](mailto:iiit.priyanshu@gmail.com).

---

## 🔗 Useful Links

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)  
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)  
- [Entropy Calculation Guide](https://en.wikipedia.org/wiki/Password_strength#Entropy)

