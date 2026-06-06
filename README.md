# Rate-My-Professors-Concensus-Generator
A desktop application that looks up a professor on Rate My Professors, scrapes their reviews, and uses Google Gemini to generate a concise consensus paragraph.

**Installation Instructions (exe):**
1. **Set your Gemini API key**  

The app reads your key from the GEMINI_API_KEY environment variable.  

**macOS / Linux**:
```
export GEMINI_API_KEY="your-key-here"
```
**Windows (Command Prompt/Terminal)**:
```
set GEMINI_API_KEY="your-key-here"
```
2. **Run the app**  

Run the .exe file. The app may crash if the Gemini model used (3.1 Flash Lite) is overloaded.


**Installation Instructions (non-exe):**
1. **Clone the repository**
```
git clone <https://github.com/Aptedl/Rate-My-Professors-Concensus-Generator>
cd rmp-consensus-generator
```
2. **Install dependencies**
```
pip install pyqt6 requests beautifulsoup4 google-genai ddgs
```
3. **Set your Gemini API key**  

The app reads your key from the GEMINI_API_KEY environment variable.  

**macOS / Linux**:
```
export GEMINI_API_KEY="your-key-here"
```
**Windows (Command Prompt)**:
```
set GEMINI_API_KEY="your-key-here"
```
4. **Run the app**
```
python (enter file path to Main.py here)
```
