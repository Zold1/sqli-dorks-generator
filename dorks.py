from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
import random


@dataclass
class DorkConfig:
    """Configuration class to hold file paths for dork generation"""
    sites_file: Path = Path("sites.txt")
    keywords_file: Path = Path("keywords.txt")
    page_types_file: Path = Path("page_types.txt")
    page_parameters_file: Path = Path("page_parameters.txt")
    search_functions_file: Path = Path("search_functions.txt")
    patterns_file: Path = Path("patterns.txt")
    output_file: Path = Path("dorks.txt")


class FileReader:
    """Handles file reading operations with error handling"""
    
    @staticmethod
    def read_lines(file_path: Path) -> List[str]:
        """Read lines from a file and return them as a list of stripped strings"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            raise FileNotFoundError(f"Required file not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error reading file {file_path}: {str(e)}")


class DorkGenerator:
    """Main class for generating Google dorks"""
    
    def __init__(self, config: DorkConfig):
        self.config = config
        self.file_reader = FileReader()
        
    def _load_components(self) -> tuple:
        """Load all necessary components for dork generation"""
        return (
            self.file_reader.read_lines(self.config.sites_file),
            self.file_reader.read_lines(self.config.keywords_file),
            self.file_reader.read_lines(self.config.page_types_file),
            self.file_reader.read_lines(self.config.page_parameters_file),
            self.file_reader.read_lines(self.config.search_functions_file),
            self.file_reader.read_lines(self.config.patterns_file)
        )
    
    def _generate_dork(self, pattern: str, components: dict) -> str:
        """Generate a single dork string using the pattern and components"""
        return (pattern
                .replace("{site}", components['site'])
                .replace("{keyword}", components['keyword'])
                .replace("{page_type}", components['page_type'])
                .replace("{page_parameter}", components['page_parameter'])
                .replace("{search_function}", components['search_function']))
    
    def generate_dorks(self) -> List[str]:
        """Generate all possible dork combinations"""
        sites, keywords, page_types, page_parameters, search_functions, patterns = self._load_components()
        
        dorks = []
        for pattern in patterns:
            for site in sites:
                for keyword in keywords:
                    for page_type in page_types:
                        for page_parameter in page_parameters:
                            for search_function in search_functions:
                                components = {
                                    'site': site,
                                    'keyword': keyword,
                                    'page_type': page_type,
                                    'page_parameter': page_parameter,
                                    'search_function': search_function
                                }
                                dork = self._generate_dork(pattern, components)
                                dorks.append(dork)
        
        return dorks
    
    def save_dorks(self, dorks: List[str], randomize: bool = True) -> None:
        """Save generated dorks to a file, optionally randomizing them first"""
        if randomize:
            random.shuffle(dorks)
            
        try:
            with open(self.config.output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(dorks))
        except Exception as e:
            raise Exception(f"Error saving dorks to {self.config.output_file}: {str(e)}")


def get_user_input(prompt: str, default: str) -> str:
    """Get user input with a default value"""
    user_input = input(f"{prompt} ({default}): ").strip()
    return user_input if user_input else default


def main():
    """Main function to run the dork generator"""
    try:
        # Get configuration from user input
        config = DorkConfig(
            sites_file=Path(get_user_input("Sites file", "sites.txt")),
            keywords_file=Path(get_user_input("Keywords file", "keywords.txt")),
            page_types_file=Path(get_user_input("Page types file", "page_types.txt")),
            page_parameters_file=Path(get_user_input("Page parameters file", "page_parameters.txt")),
            search_functions_file=Path(get_user_input("Search functions file", "search_functions.txt")),
            patterns_file=Path(get_user_input("Patterns file", "patterns.txt"))
        )
        
        # Initialize and run dork generator
        generator = DorkGenerator(config)
        
        print("Generating dorks...")
        dorks = generator.generate_dorks()
        
        print("Saving dorks...")
        generator.save_dorks(dorks)
        
        print(f"Successfully generated {len(dorks)} dorks and saved to {config.output_file}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
