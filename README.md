![Google Dork Generator](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&text=Dork%20Generator&section=header&desc=Creates%20search%20patterns%20for%20web%20reconnaissance&descAlignY=55&fontAlignY=35&descAlign=50&descSize=20&animation=fadeIn&fontSize=50 "Google Dork Generator")

# Google Dork Generator

A Python-based tool for generating Google dorks by combining different search patterns and parameters. This tool helps security researchers and penetration testers create comprehensive lists of Google dorks for their research.

💡 **Pro Tip**: Star this repository to keep it handy for future reference!

## 🔍 Features

- Generates Google dorks using customizable patterns and parameters
- Supports multiple input files for different dork components
- Randomizes generated dorks
- Error handling and validation
- Cross-platform compatibility
- Easy to extend and customize

## 📋 Requirements

- Python 3.7+
- No external dependencies required

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/AhmedOsamaMath/sqli-dorks-generator.git
cd dork-generator
```

2. Make sure you have the required input files (see Input Files section below)

## 💻 Usage

Run the script:
```bash
python dorks.py
```

The script will prompt you for input file locations. Press Enter to use default filenames:
- sites.txt
- keywords.txt
- page_types.txt
- page_parameters.txt
- search_functions.txt
- patterns.txt

Output will be saved to `dorks.txt`.

## 📁 Input Files Format

Create the following text files in the same directory as the script:

### sites.txt
```
site:example.com
site:*.example.com
```

### keywords.txt
```
password
admin
login
```

### page_types.txt
```
filetype:pdf
filetype:doc
ext:php
```

### page_parameters.txt
```
inurl:admin
inurl:login
intitle:admin
```

### search_functions.txt
```
intext:
intitle:
inurl:
```

### patterns.txt
```
{site} {keyword} {page_type}
{site} {page_parameter} {search_function}{keyword}
```

## 🔧 Customization

You can modify the input files to customize the generated dorks according to your needs. Each component will be combined according to the patterns specified in `patterns.txt`.

## 📊 Project Structure

```
dork-generator/
├── dorks.py
├── README.md
├── sites.txt
├── keywords.txt
├── page_types.txt
├── page_parameters.txt
├── search_functions.txt
└── patterns.txt
```

## 🚩 Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions, suggestions, or issues, please open an issue in the GitHub repository.
