import random
import string
import os
import sys
import argparse
from datetime import datetime
import itertools
from typing import List, Dict

# Clear screen function for cross-platform
def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Color codes for terminal output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def display_banner():
    """Display the WOLF PASS banner"""
    banner = f"""
{Colors.RED}{Colors.BOLD}
██╗    ██╗ ██████╗ ██╗     ███████╗
██║    ██║██╔═══██╗██║     ██╔════╝
██║ █╗ ██║██║   ██║██║     █████╗  
██║███╗██║██║   ██║██║     ██╔══╝  
╚███╔███╔╝╚██████╔╝███████╗██║     
 ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝     
{Colors.GREEN}
██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝███████║███████╗███████╗
██╔═══╝ ██╔══██║╚════██║╚════██║
██║     ██║  ██║███████║███████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
{Colors.CYAN}
WOLF PASS GENERATOR - Advanced Password Generation Tool
{Colors.YELLOW}Version 3.2 | Wolf Security Team | Victim: 30M | Custom Wordlists{Colors.END}
"""
    print(banner)

class PasswordGenerator:
    def __init__(self):
        self.char_sets = {
            'bigalpha': string.ascii_uppercase,
            'smallalpha': string.ascii_lowercase,
            'alpha': string.ascii_letters,
            'numeric': string.digits,
            'special': '!@#$%^&*()_+-=[]{}|;:,.<>?',
            'extended': '!@#$%^&*()_+-=[]{}|;:,.<>?~`',
            'hex': '0123456789ABCDEF',
            'binary': '01',
            'alphanumeric': string.ascii_letters + string.digits,
            'all': string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{}|;:,.<>?'
        }
        
        self.leet_dict = {
            'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7',
            'A': '4', 'E': '3', 'I': '1', 'O': '0', 'S': '5', 'T': '7',
            'l': '1', 'z': '2', 'g': '9', 'b': '8'
        }
        
        self.common_suffixes = ['', '1', '12', '123', '1234', '12345', '!', '!!', '!@', '!@#', 
                               '2020', '2021', '2022', '2023', '2024', '2025', '00', '000', '0000',
                               '007', '69', '99', '100', '101', '111', '222', '333', '444', '555',
                               '666', '777', '888', '999', '0101', '010101']
        
        self.common_prefixes = ['', '!', '!!', '#', '$', '%', '&', '*', 'Admin', 'User', 'Pass', 
                               'Password', 'Secret', 'Secure', 'My', 'The']
        
        self.MAX_RANDOM_PASSWORDS = 10000000  # 10 million limit for random generation
        self.MAX_VICTIM_PASSWORDS = 30000000  # 30 million limit for victim-based generation
        self.MAX_WORDLIST_PASSWORDS = 50000000  # 50 million limit for custom wordlists

    def generate_random_password(self, length=12, format_type='all', count=1):
        """Generate random passwords based on format"""
        # Check password count limit
        if count > self.MAX_RANDOM_PASSWORDS:
            print(f"{Colors.RED}Error: Cannot generate more than {self.MAX_RANDOM_PASSWORDS:,} passwords{Colors.END}")
            return []
            
        passwords = []
        
        if format_type in self.char_sets:
            charset = self.char_sets[format_type]
        else:
            # Handle custom format
            charset = self._parse_custom_format(format_type)
        
        print(f"{Colors.YELLOW}Generating {count} passwords...{Colors.END}")
        for i in range(count):
            password = ''.join(random.choice(charset) for _ in range(length))
            passwords.append(password)
            # Show progress for large generations
            if count > 1000 and i % 1000 == 0:
                print(f"{Colors.CYAN}Progress: {i:,}/{count:,} passwords generated...{Colors.END}")
        
        return passwords

    def _parse_custom_format(self, format_str):
        """Parse custom format string"""
        charset = ""
        i = 0
        while i < len(format_str):
            if format_str[i] == '"':
                # Find closing quote
                end_quote = format_str.find('"', i + 1)
                if end_quote != -1:
                    charset += format_str[i+1:end_quote]
                    i = end_quote + 1
                    continue
            elif format_str[i:i+4] == 'numb':
                charset += self.char_sets['numeric']
                i += 4
                continue
            elif format_str[i:i+5] == 'alpha':
                charset += self.char_sets['alpha']
                i += 5
                continue
            elif format_str[i:i+9] == 'bigalpha':
                charset += self.char_sets['bigalpha']
                i += 9
                continue
            elif format_str[i:i+10] == 'smallalpha':
                charset += self.char_sets['smallalpha']
                i += 10
                continue
            elif format_str[i:i+7] == 'special':
                charset += self.char_sets['special']
                i += 7
                continue
            else:
                charset += format_str[i]
            i += 1
        
        return charset

    def generate_victim_based_passwords(self, victim_info, algorithms=['basic'], count=10):
        """Generate passwords based on victim information"""
        # Check password count limit
        if count > self.MAX_VICTIM_PASSWORDS:
            print(f"{Colors.RED}Error: Cannot generate more than {self.MAX_VICTIM_PASSWORDS:,} passwords{Colors.END}")
            return []
            
        passwords = []
        
        # Extract victim data
        first_name = victim_info.get('first_name', '').lower()
        last_name = victim_info.get('last_name', '').lower()
        birth_year = victim_info.get('birth_year', '')
        pet_name = victim_info.get('pet_name', '').lower()
        company = victim_info.get('company', '').lower()
        keywords = victim_info.get('keywords', [])
        
        base_words = [first_name, last_name, pet_name, company] + keywords
        base_words = [word for word in base_words if word]  # Remove empty strings
        
        if not base_words:
            print(f"{Colors.RED}Error: No valid victim information provided{Colors.END}")
            return []
        
        print(f"{Colors.YELLOW}Generating {count:,} victim-based passwords...{Colors.END}")
        
        # Calculate how many passwords per algorithm we need
        algos_count = len(algorithms)
        passwords_per_algo = min(count // algos_count, 100000)  # Limit per algorithm to avoid memory issues
        
        generated_count = 0
        for algorithm in algorithms:
            if generated_count >= count:
                break
                
            algo_passwords = []
            if algorithm == 'basic':
                algo_passwords = self._basic_algorithm(base_words, birth_year, passwords_per_algo)
            elif algorithm == 'leet':
                algo_passwords = self._leet_algorithm(base_words, birth_year, passwords_per_algo)
            elif algorithm == 'advanced':
                algo_passwords = self._advanced_algorithm(base_words, birth_year, passwords_per_algo)
            elif algorithm == 'combinator':
                algo_passwords = self._combinator_algorithm(base_words, birth_year, passwords_per_algo)
            elif algorithm == 'massive':
                algo_passwords = self._massive_algorithm(base_words, birth_year, passwords_per_algo)
            elif algorithm == 'hybrid':
                algo_passwords = self._hybrid_algorithm(base_words, birth_year, passwords_per_algo)
            
            # Add unique passwords from this algorithm
            for pwd in algo_passwords:
                if pwd not in passwords:
                    passwords.append(pwd)
                    generated_count += 1
                    if generated_count >= count:
                        break
            
            print(f"{Colors.CYAN}{algorithm}: {len(algo_passwords):,} patterns generated ({generated_count:,} total){Colors.END}")
        
        # If we still need more passwords, generate random variations
        if generated_count < count:
            needed = count - generated_count
            print(f"{Colors.YELLOW}Generating {needed:,} additional random variations...{Colors.END}")
            additional = self._random_variations(base_words, birth_year, needed)
            passwords.extend(additional)
        
        return passwords[:count]

    def _basic_algorithm(self, base_words, birth_year, count):
        """Basic password generation algorithm"""
        passwords = []
        special_chars = ['', '!', '@', '#', '$', '%', '&', '*', '_', '-', '+', '=', '.']  # Added empty string
        
        max_per_combination = max(1, count // (len(base_words) * len(special_chars) * 3))
        
        for word in base_words:
            for special in special_chars:
                # Word + special + year variations
                if birth_year:
                    passwords.append(word + special + birth_year)
                    passwords.append(birth_year + special + word)
                    passwords.append(word + special + birth_year[-2:])
                    passwords.append(birth_year[-2:] + special + word)
                
                # Word + special variations
                passwords.append(word + special)
                passwords.append(special + word)
                
                # Case variations
                passwords.append(word.title() + special)
                passwords.append(word.upper() + special)
        
        return passwords[:count]

    def _leet_algorithm(self, base_words, birth_year, count):
        """Leet speak password generation"""
        passwords = []
        
        for word in base_words:
            # Full leet conversion
            leet_word = ''.join(self.leet_dict.get(char, char) for char in word)
            
            # Partial leet conversions (different levels)
            leet_variations = []
            for i in range(1, min(4, len(word))):
                partial = word[:i] + ''.join(self.leet_dict.get(char, char) for char in word[i:])
                leet_variations.append(partial)
            
            leet_variations.append(leet_word)
            
            for leet_version in leet_variations:
                if birth_year:
                    passwords.append(leet_version + birth_year)
                    passwords.append(birth_year + leet_version)
                    passwords.append(leet_version + birth_year[-2:])
                    passwords.append(birth_year[-2:] + leet_version)
                
                # Case variations with leet
                passwords.append(leet_version)
                passwords.append(leet_version.title())
                passwords.append(leet_version.upper())
        
        return passwords[:count]

    def _advanced_algorithm(self, base_words, birth_year, count):
        """Advanced password generation with multiple patterns"""
        passwords = []
        
        for word in base_words:
            # Multiple patterns with various combinations
            base_patterns = [
                word, word.title(), word.upper(), word.lower(),
                word[::-1],  # reversed
                word + word,  # doubled
            ]
            
            for base in base_patterns:
                # Add common suffixes
                for suffix in self.common_suffixes[:20]:  # Use first 20 suffixes
                    passwords.append(base + suffix)
                
                # Add birth year variations
                if birth_year:
                    passwords.append(base + birth_year)
                    passwords.append(base + birth_year[-2:])
                    passwords.append(birth_year + base)
                    passwords.append(birth_year[-2:] + base)
                    
                    # With special characters
                    for special in ['', '!', '@', '#', '_', '-', '.']:
                        passwords.append(base + special + birth_year)
                        passwords.append(birth_year + special + base)
        
        return passwords[:count]

    def _combinator_algorithm(self, base_words, birth_year, count):
        """Combine multiple words"""
        passwords = []
        
        if len(base_words) >= 2:
            # Combine words in different ways
            for i in range(len(base_words)):
                for j in range(len(base_words)):
                    if i != j:
                        # Different combinations
                        combinations = [
                            base_words[i] + base_words[j],
                            base_words[i].title() + base_words[j],
                            base_words[i] + base_words[j].title(),
                            base_words[i].title() + base_words[j].title(),
                            base_words[i] + '_' + base_words[j],
                            base_words[i] + '.' + base_words[j],
                            base_words[i] + base_words[j][0],  # first word + first char of second
                        ]
                        
                        for combo in combinations:
                            if birth_year:
                                passwords.append(combo + birth_year)
                                passwords.append(combo + birth_year[-2:])
                                passwords.append(birth_year + combo)
                            passwords.append(combo)
        
        return passwords[:count]

    def _massive_algorithm(self, base_words, birth_year, count):
        """Massive password generation with extensive variations"""
        passwords = []
        
        # Generate numeric sequences
        numeric_sequences = []
        for i in range(1000):  # Generate 1000 numeric sequences
            length = random.randint(1, 6)
            seq = ''.join(random.choice(string.digits) for _ in range(length))
            numeric_sequences.append(seq)
        
        # Special character combinations
        special_combos = ['', '!', '@', '#', '$', '%', '!@', '#$', '!@#', '$%^']
        
        for word in base_words:
            word_variations = [
                word, word.lower(), word.upper(), word.title(),
                word[::-1], word[0].upper() + word[1:].lower(),
                word + word[0], word[0] + word  # first char duplication
            ]
            
            for variation in word_variations:
                # Add numeric sequences
                for num_seq in numeric_sequences[:100]:  # Use first 100 numeric sequences
                    passwords.append(variation + num_seq)
                    passwords.append(num_seq + variation)
                    
                    # With special characters
                    for special in special_combos:
                        passwords.append(variation + special + num_seq)
                        passwords.append(num_seq + special + variation)
                
                # Birth year combinations
                if birth_year:
                    year_variations = [birth_year, birth_year[-2:], birth_year[-1:], birth_year[:2]]
                    for year in year_variations:
                        passwords.append(variation + year)
                        passwords.append(year + variation)
                        
                        for special in special_combos:
                            passwords.append(variation + special + year)
                            passwords.append(year + special + variation)
        
        return passwords[:count]

    def _hybrid_algorithm(self, base_words, birth_year, count):
        """Hybrid algorithm combining multiple techniques"""
        passwords = []
        
        for word in base_words:
            # Create hybrid variations
            hybrids = []
            
            # Mix case randomly
            mixed_case = ''.join(random.choice([c.upper(), c.lower()]) for c in word)
            hybrids.append(mixed_case)
            
            # Add random leet substitutions
            leet_mixed = ''.join(self.leet_dict.get(c, c) if random.random() > 0.7 else c for c in word)
            hybrids.append(leet_mixed)
            
            # Reverse with leet
            reversed_leet = ''.join(self.leet_dict.get(c, c) for c in word[::-1])
            hybrids.append(reversed_leet)
            
            for hybrid in hybrids:
                # Add various suffixes and prefixes
                for i in range(min(50, count // len(hybrids))):
                    # Random numeric suffix
                    num_suffix = ''.join(random.choice(string.digits) for _ in range(random.randint(1, 4)))
                    
                    # Random special prefix/suffix
                    special_char = random.choice(['', '!', '@', '#', '$', '%', '&', '*'])
                    
                    passwords.append(hybrid + num_suffix)
                    passwords.append(special_char + hybrid + num_suffix)
                    passwords.append(hybrid + special_char + num_suffix)
                    
                    if birth_year:
                        passwords.append(hybrid + birth_year[-2:] + num_suffix)
                        passwords.append(hybrid + special_char + birth_year)
        
        return passwords[:count]

    def _random_variations(self, base_words, birth_year, count):
        """Generate random variations when we need more passwords"""
        passwords = []
        chars = string.ascii_lowercase + string.digits + '!@#'
        
        for _ in range(count):
            base_word = random.choice(base_words)
            
            # Random transformation
            transform_type = random.randint(0, 5)
            if transform_type == 0:
                # Random case
                result = ''.join(random.choice([c.upper(), c.lower()]) for c in base_word)
            elif transform_type == 1:
                # Partial leet
                result = ''.join(self.leet_dict.get(c, c) if random.random() > 0.5 else c for c in base_word)
            elif transform_type == 2:
                # Add random chars
                result = base_word + ''.join(random.choice(chars) for _ in range(random.randint(1, 3)))
            elif transform_type == 3:
                # Reverse and modify
                result = base_word[::-1] + ''.join(random.choice(string.digits) for _ in range(2))
            else:
                # Mixed approach
                result = base_word.title() + ''.join(random.choice(string.digits) for _ in range(random.randint(2, 4)))
            
            passwords.append(result)
        
        return passwords

    def load_rockyou_passwords(self, max_passwords=1000):
        """Load passwords from rockyou.txt file - automatically uses rockyou.txt in same folder"""
        return self.load_custom_wordlist("rockyou.txt", max_passwords)

    def load_custom_wordlist(self, filepath, max_passwords=1000):
        """Load passwords from any custom text file"""
        # Check password count limit
        if max_passwords > self.MAX_WORDLIST_PASSWORDS:
            print(f"{Colors.RED}Error: Cannot load more than {self.MAX_WORDLIST_PASSWORDS:,} passwords{Colors.END}")
            return []
            
        passwords = []
        
        if not os.path.exists(filepath):
            print(f"{Colors.RED}Error: {filepath} not found{Colors.END}")
            return []
        
        try:
            file_size = os.path.getsize(filepath)
            print(f"{Colors.YELLOW}Loading passwords from {filepath}...{Colors.END}")
            print(f"{Colors.CYAN}File size: {file_size:,} bytes{Colors.END}")
            
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                for i, line in enumerate(file):
                    if i >= max_passwords:
                        break
                    password = line.strip()
                    if password:  # Skip empty lines
                        passwords.append(password)
                    # Show progress for large loads
                    if max_passwords > 1000 and i % 10000 == 0:
                        print(f"{Colors.CYAN}Progress: {i:,}/{max_passwords:,} passwords loaded...{Colors.END}")
                        
        except Exception as e:
            print(f"{Colors.RED}Error reading {filepath}: {e}{Colors.END}")
            return []
        
        return passwords

def get_victim_info():
    """Collect victim information from user"""
    print(f"\n{Colors.CYAN}=== Victim Information Collection ==={Colors.END}")
    victim_info = {}
    
    victim_info['first_name'] = input(f"{Colors.YELLOW}First name: {Colors.END}").strip()
    victim_info['last_name'] = input(f"{Colors.YELLOW}Last name: {Colors.END}").strip()
    victim_info['birth_year'] = input(f"{Colors.YELLOW}Birth year (YYYY): {Colors.END}").strip()
    victim_info['pet_name'] = input(f"{Colors.YELLOW}Pet name: {Colors.END}").strip()
    victim_info['company'] = input(f"{Colors.YELLOW}Company: {Colors.END}").strip()
    
    keywords = input(f"{Colors.YELLOW}Additional keywords (comma separated): {Colors.END}").strip()
    victim_info['keywords'] = [k.strip() for k in keywords.split(',')] if keywords else []
    
    return victim_info

def show_algorithms():
    """Display available password generation algorithms"""
    algorithms = {
        'basic': 'Basic combinations with special characters',
        'leet': 'Leet speak substitutions (a->4, e->3, etc.)',
        'advanced': 'Advanced patterns with common suffixes',
        'combinator': 'Combine multiple words together',
        'massive': 'Massive generation with extensive variations',
        'hybrid': 'Hybrid approach with random transformations'
    }
    
    print(f"\n{Colors.CYAN}=== Available Algorithms ==={Colors.END}")
    for algo, description in algorithms.items():
        print(f"{Colors.GREEN}{algo:<12}{Colors.END} - {description}")
    
    print(f"\n{Colors.YELLOW}Recommendations:{Colors.END}")
    print("For small lists (< 1000): basic, leet, advanced")
    print("For large lists (> 1000): massive, hybrid, combinator")
    print("For maximum generation: Use all algorithms together")

def save_passwords(passwords, filename):
    """Save passwords to file"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for password in passwords:
                file.write(password + '\n')
        print(f"{Colors.GREEN}✓ Passwords saved to: {filename}{Colors.END}")
        print(f"{Colors.GREEN}✓ Total passwords saved: {len(passwords):,}{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}✗ Error saving to file: {e}{Colors.END}")

def display_help():
    """Display help information"""
    help_text = f"""
{Colors.CYAN}{Colors.BOLD}WOLF PASS GENERATOR - HELP{Colors.END}

{Colors.YELLOW}USAGE:{Colors.END}
    python wolf_pass_generator.py [OPTIONS]

{Colors.YELLOW}OPTIONS:{Colors.END}
    {Colors.GREEN}-g, --generate{Colors.END}       Generate password list
    {Colors.GREEN}-n, --filename{Colors.END}       Specify output filename
    {Colors.GREEN}-f, --format{Colors.END}         Password format type
    {Colors.GREEN}-l, --length{Colors.END}         Password length (default: 12)
    {Colors.GREEN}-c, --count{Colors.END}          Number of passwords to generate (default: 10, max: 10,000,000)
    {Colors.GREEN}-v, --victim{Colors.END}         Use victim information (max: 30,000,000)
    {Colors.GREEN}-r, --rockyou{Colors.END}        Use rockyou.txt passwords
    {Colors.GREEN}-w, --wordlist{Colors.END}       Use custom wordlist file
    {Colors.GREEN}-a, --algorithm{Colors.END}      Algorithm for victim-based generation
    {Colors.GREEN}-h, --help{Colors.END}           Show this help message

{Colors.YELLOW}FORMAT TYPES:{Colors.END}
    {Colors.GREEN}bigalpha{Colors.END}        Uppercase letters (A-Z)
    {Colors.GREEN}smallalpha{Colors.END}      Lowercase letters (a-z)
    {Colors.GREEN}alpha{Colors.END}           Both uppercase and lowercase letters
    {Colors.GREEN}numeric{Colors.END}         Numbers (0-9)
    {Colors.GREEN}special{Colors.END}         Special characters (!@#$%^&*()_+-= etc.)
    {Colors.GREEN}alphanumeric{Colors.END}    Letters and numbers
    {Colors.GREEN}all{Colors.END}             All character types
    {Colors.GREEN}custom{Colors.END}          Custom format string

{Colors.YELLOW}CUSTOM FORMAT EXAMPLES:{Colors.END}
    {Colors.GREEN}"word"numb{Colors.END}        Literal "word" followed by numbers
    {Colors.GREEN}bigalphasmallalphanumb{Colors.END}  Uppercase + lowercase + numbers
    {Colors.GREEN}alpha"123"special{Colors.END} Letters + "123" + special characters

{Colors.YELLOW}ALGORITHMS:{Colors.END}
    {Colors.GREEN}basic{Colors.END}           Basic combinations
    {Colors.GREEN}leet{Colors.END}            Leet speak substitutions
    {Colors.GREEN}advanced{Colors.END}        Advanced patterns
    {Colors.GREEN}combinator{Colors.END}      Word combinations
    {Colors.GREEN}massive{Colors.END}         Massive generation with extensive variations
    {Colors.GREEN}hybrid{Colors.END}          Hybrid approach with random transformations

{Colors.YELLOW}MAXIMUM LIMITS:{Colors.END}
    {Colors.GREEN}Random Generation:{Colors.END} 10,000,000 passwords
    {Colors.GREEN}Victim-Based:{Colors.END} 30,000,000 passwords  
    {Colors.GREEN}Custom Wordlists:{Colors.END} 50,000,000 passwords

{Colors.YELLOW}EXAMPLES:{Colors.END}
    python wolf_pass_generator.py -g -f bigalphanumb -l 16 -c 5
    python wolf_pass_generator.py -v -a massive,hybrid,combinator -c 50000 -n victim_passwords.txt
    python wolf_pass_generator.py -r -c 1000000 -n common_passwords.txt
    python wolf_pass_generator.py -w /path/to/wordlist.txt -c 50000 -n my_passwords.txt
    python wolf_pass_generator.py -g -c 1000000 -n million_passwords.txt
    """
    print(help_text)

def wait_and_continue():
    """Wait for user input and then clear screen"""
    input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
    clear_screen()
    display_banner()

def interactive_mode():
    """Interactive mode for the password generator"""
    generator = PasswordGenerator()
    
    while True:
        print(f"\n{Colors.CYAN}{Colors.BOLD}=== WOLF PASS GENERATOR MAIN MENU ==={Colors.END}")
        print(f"{Colors.GREEN}1.{Colors.END} Generate random password list")
        print(f"{Colors.GREEN}2.{Colors.END} Generate passwords with victim info")
        print(f"{Colors.GREEN}3.{Colors.END} Use rockyou.txt passwords")
        print(f"{Colors.GREEN}4.{Colors.END} Use custom wordlist file")
        print(f"{Colors.GREEN}5.{Colors.END} Show algorithms and examples")
        print(f"{Colors.GREEN}6.{Colors.END} Help")
        print(f"{Colors.GREEN}7.{Colors.END} Exit")
        
        choice = input(f"\n{Colors.YELLOW}Select option (1-7): {Colors.END}").strip()
        
        if choice == '1':
            clear_screen()
            display_banner()
            print(f"\n{Colors.CYAN}=== Random Password Generation ==={Colors.END}")
            
            format_type = input(f"{Colors.YELLOW}Format type (bigalpha/smallalpha/alpha/numeric/special/alphanumeric/all/custom) [all]: {Colors.END}").strip()
            if not format_type:
                format_type = 'all'
            
            try:
                length = int(input(f"{Colors.YELLOW}Password length [12]: {Colors.END}").strip() or "12")
                count = int(input(f"{Colors.YELLOW}Number of passwords (max 10,000,000) [10]: {Colors.END}").strip() or "10")
            except ValueError:
                print(f"{Colors.RED}Invalid number! Using defaults.{Colors.END}")
                length, count = 12, 10
            
            filename = input(f"{Colors.YELLOW}Save to file (leave empty to display only): {Colors.END}").strip()
            
            passwords = generator.generate_random_password(length, format_type, count)
            
            if passwords:
                print(f"\n{Colors.GREEN}✓ Successfully generated {len(passwords):,} passwords:{Colors.END}")
                # Show only first 20 passwords to avoid flooding the screen
                for i, pwd in enumerate(passwords[:20], 1):
                    print(f"{i:2d}. {pwd}")
                if len(passwords) > 20:
                    print(f"{Colors.YELLOW}... and {len(passwords) - 20:,} more passwords{Colors.END}")
                
                if filename:
                    save_passwords(passwords, filename)
            
            wait_and_continue()
        
        elif choice == '2':
            clear_screen()
            display_banner()
            print(f"\n{Colors.CYAN}=== Victim-Based Password Generation ==={Colors.END}")
            
            victim_info = get_victim_info()
            show_algorithms()
            
            print(f"\n{Colors.YELLOW}Recommended algorithms for large generations:{Colors.END}")
            print("massive, hybrid, combinator, advanced, leet, basic")
            
            algo_input = input(f"{Colors.YELLOW}Algorithms to use (comma separated) [massive,hybrid,combinator]: {Colors.END}").strip()
            algorithms = [a.strip() for a in algo_input.split(',')] if algo_input else ['massive', 'hybrid', 'combinator']
            
            try:
                count = int(input(f"{Colors.YELLOW}Number of passwords to generate (max 30,000,000) [1000]: {Colors.END}").strip() or "1000")
            except ValueError:
                count = 1000
            
            filename = input(f"{Colors.YELLOW}Save to file (leave empty to display only): {Colors.END}").strip()
            
            passwords = generator.generate_victim_based_passwords(victim_info, algorithms, count)
            
            if passwords:
                print(f"\n{Colors.GREEN}✓ Successfully generated {len(passwords):,} passwords:{Colors.END}")
                # Show only first 20 passwords to avoid flooding the screen
                for i, pwd in enumerate(passwords[:20], 1):
                    print(f"{i:2d}. {pwd}")
                if len(passwords) > 20:
                    print(f"{Colors.YELLOW}... and {len(passwords) - 20:,} more passwords{Colors.END}")
                
                if filename:
                    save_passwords(passwords, filename)
            else:
                print(f"{Colors.RED}✗ No passwords generated. Check victim information.{Colors.END}")
            
            wait_and_continue()
        
        elif choice == '3':
            clear_screen()
            display_banner()
            print(f"\n{Colors.CYAN}=== Rockyou.txt Password List ==={Colors.END}")
            print(f"{Colors.YELLOW}Note: Using rockyou.txt from current directory{Colors.END}")
            
            try:
                max_passwords = int(input(f"{Colors.YELLOW}Maximum passwords to load (max 50,000,000) [1000]: {Colors.END}").strip() or "1000")
            except ValueError:
                max_passwords = 1000
            
            filename = input(f"{Colors.YELLOW}Save to file (leave empty to display only): {Colors.END}").strip()
            
            passwords = generator.load_rockyou_passwords(max_passwords)
            
            if passwords:
                print(f"\n{Colors.GREEN}✓ Successfully loaded {len(passwords):,} passwords from rockyou.txt:{Colors.END}")
                for i, pwd in enumerate(passwords[:20], 1):  # Show first 20
                    print(f"{i:2d}. {pwd}")
                if len(passwords) > 20:
                    print(f"{Colors.YELLOW}... and {len(passwords) - 20:,} more passwords{Colors.END}")
                
                if filename:
                    save_passwords(passwords, filename)
            else:
                print(f"{Colors.RED}✗ No passwords loaded.{Colors.END}")
            
            wait_and_continue()
        
        elif choice == '4':
            clear_screen()
            display_banner()
            print(f"\n{Colors.CYAN}=== Custom Wordlist Loading ==={Colors.END}")
            
            filepath = input(f"{Colors.YELLOW}Enter path to wordlist file: {Colors.END}").strip()
            
            if not filepath:
                print(f"{Colors.RED}No file path provided.{Colors.END}")
                wait_and_continue()
                continue
            
            try:
                max_passwords = int(input(f"{Colors.YELLOW}Maximum passwords to load (max 50,000,000) [1000]: {Colors.END}").strip() or "1000")
            except ValueError:
                max_passwords = 1000
            
            filename = input(f"{Colors.YELLOW}Save to file (leave empty to display only): {Colors.END}").strip()
            
            passwords = generator.load_custom_wordlist(filepath, max_passwords)
            
            if passwords:
                print(f"\n{Colors.GREEN}✓ Successfully loaded {len(passwords):,} passwords from {filepath}:{Colors.END}")
                for i, pwd in enumerate(passwords[:20], 1):  # Show first 20
                    print(f"{i:2d}. {pwd}")
                if len(passwords) > 20:
                    print(f"{Colors.YELLOW}... and {len(passwords) - 20:,} more passwords{Colors.END}")
                
                if filename:
                    save_passwords(passwords, filename)
            else:
                print(f"{Colors.RED}✗ No passwords loaded from {filepath}.{Colors.END}")
            
            wait_and_continue()
        
        elif choice == '5':
            clear_screen()
            display_banner()
            show_algorithms()
            wait_and_continue()
        
        elif choice == '6':
            clear_screen()
            display_banner()
            display_help()
            wait_and_continue()
        
        elif choice == '7':
            print(f"{Colors.GREEN}Thank you for using WOLF PASS GENERATOR!{Colors.END}")
            break
        
        else:
            print(f"{Colors.RED}Invalid option! Please select 1-7.{Colors.END}")
            wait_and_continue()

def main():
    """Main function"""
    clear_screen()
    display_banner()
    
    # Command line argument parsing
    parser = argparse.ArgumentParser(description='WOLF PASS GENERATOR - Advanced Password Generation Tool', add_help=False)
    
    parser.add_argument('-g', '--generate', action='store_true', help='Generate password list')
    parser.add_argument('-n', '--filename', type=str, help='Output filename')
    parser.add_argument('-f', '--format', type=str, default='all', help='Password format type')
    parser.add_argument('-l', '--length', type=int, default=12, help='Password length')
    parser.add_argument('-c', '--count', type=int, default=10, help='Number of passwords')
    parser.add_argument('-v', '--victim', action='store_true', help='Use victim information')
    parser.add_argument('-r', '--rockyou', action='store_true', help='Use rockyou.txt')
    parser.add_argument('-w', '--wordlist', type=str, help='Use custom wordlist file')
    parser.add_argument('-a', '--algorithm', type=str, help='Algorithms for victim-based generation')
    parser.add_argument('-h', '--help', action='store_true', help='Show help')
    
    # If no arguments provided, start interactive mode
    if len(sys.argv) == 1:
        interactive_mode()
        return
    
    args = parser.parse_args()
    
    if args.help:
        display_help()
        return
    
    generator = PasswordGenerator()
    
    if args.generate:
        passwords = generator.generate_random_password(args.length, args.format, args.count)
        
        if passwords:
            print(f"{Colors.GREEN}Generated {len(passwords):,} passwords:{Colors.END}")
            for i, pwd in enumerate(passwords[:20], 1):
                print(f"{i:2d}. {pwd}")
            if len(passwords) > 20:
                print(f"{Colors.YELLOW}... and {len(passwords) - 20:,} more{Colors.END}")
        
        if args.filename:
            save_passwords(passwords, args.filename)
    
    elif args.victim:
        victim_info = get_victim_info()
        algorithms = args.algorithm.split(',') if args.algorithm else ['massive', 'hybrid', 'combinator']
        
        passwords = generator.generate_victim_based_passwords(victim_info, algorithms, args.count)
        
        if passwords:
            print(f"{Colors.GREEN}Generated {len(passwords):,} passwords:{Colors.END}")
            for i, pwd in enumerate(passwords[:20], 1):
                print(f"{i:2d}. {pwd}")
            if len(passwords) > 20:
                print(f"{Colors.YELLOW}... and {len(passwords) - 20:,} more{Colors.END}")
        
        if args.filename:
            save_passwords(passwords, args.filename)
    
    elif args.rockyou:
        passwords = generator.load_rockyou_passwords(args.count)
        
        if passwords:
            print(f"{Colors.GREEN}Loaded {len(passwords):,} passwords:{Colors.END}")
            for i, pwd in enumerate(passwords[:20], 1):
                print(f"{i:2d}. {pwd}")
            if len(passwords) > 20:
                print(f"{Colors.YELLOW}... and {len(passwords) - 20:,} more{Colors.END}")
            
            if args.filename:
                save_passwords(passwords, args.filename)
    
    elif args.wordlist:
        passwords = generator.load_custom_wordlist(args.wordlist, args.count)
        
        if passwords:
            print(f"{Colors.GREEN}Loaded {len(passwords):,} passwords from {args.wordlist}:{Colors.END}")
            for i, pwd in enumerate(passwords[:20], 1):
                print(f"{i:2d}. {pwd}")
            if len(passwords) > 20:
                print(f"{Colors.YELLOW}... and {len(passwords) - 20:,} more{Colors.END}")
            
            if args.filename:
                save_passwords(passwords, args.filename)

if __name__ == "__main__":
    main()
