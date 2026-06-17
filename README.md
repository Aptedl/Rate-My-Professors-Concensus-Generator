# Rate-My-Professors-Concensus-Generator
A desktop application that looks up a professor on Rate My Professors, scrapes their reviews, and uses Google Gemini to generate a concise consensus paragraph. It is a first step towards my goal of building a website that allows users to get a Gemini concensus of a course or professor from RMP.

**Installation Instructions (exe):**
1. **Get the .exe file**
Go to releases (on the right side) and select the latest version. Download SourceCode.zip, tell Windows SmartScreen to bypass any warnings (I swear it's not a virus!) and extract the zip (right click -> extract).

2. **Set your Gemini API key**  

The app reads your key from the GEMINI_API_KEY environment variable. To get an API key, go to [Google AI Studio](https://ai.dev), then click Get API Key on the bottom left. It's free and only requires a Google Account. This app uses Gemini 3.1 Flash Lite, which is lightweight and doesn't use too many tokens.

```
**Windows (Command Prompt/Terminal)**:
```
setx GEMINI_API_KEY "your-key-here"
```
3. **Run the app**  

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
export GEMINI_API_KEY = "your-key-here"
```
**Windows (Command Prompt/Terminal)**:
```
setx GEMINI_API_KEY "your-key-here"
```
4. **Run the app via terminal**
```
python (enter file path to Main.py here)
```
