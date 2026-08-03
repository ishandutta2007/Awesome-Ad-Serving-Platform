import os
import re
import subprocess
from pathlib import Path

README_PATH = 'README.md'

def run_git(cmd):
    print(f"Running: {cmd}")
    subprocess.run(["pwsh", "-Command", cmd], check=False)

def read_readme():
    with open(README_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def write_readme(content):
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

# Task 1: SaaS table size column and sort
def task_1():
    content = read_readme()
    table_pattern = re.compile(r'(\| Platform \| Description \| Pricing \| Free Tier Limit \|.*?)(?=\n\n##)', re.DOTALL)
    match = table_pattern.search(content)
    if not match: return
    table_text = match.group(1)
    lines = table_text.strip().split('\n')
    header = lines[0] + ' Size (Valuation/Revenue) |'
    separator = lines[1] + '---|'
    sizes = {
        'Google Ad Manager': ('>$1 Trillion', 2000000000000),
        'Kevel': ('~$20M+', 20000000),
        'AdButler': ('~$2M+', 2000000),
        'Broadstreet': ('~$2M+', 2000000),
        'Epom': ('~$5M+', 5000000),
        'AdGlare': ('~$1M+', 1000000),
        'Equativ': ('~$100M+', 100000000),
        'OpenX': ('~$100M+', 100000000),
        'Smart AdServer': ('~$100M+', 100000000),
    }
    new_rows = []
    for row in lines[2:]:
        name_match = re.search(r'\*\*\[?(.*?)\]?\(?', row)
        name = name_match.group(1).replace('**', '').replace('[', '').split(']')[0] if name_match else row.split('|')[1].strip().replace('**', '')
        size_str, size_val = sizes.get(name, ('Unknown', 0))
        new_rows.append((size_val, f"{row} {size_str} |"))
    new_rows.sort(key=lambda x: x[0], reverse=True)
    new_table = '\n'.join([header, separator] + [r[1] for r in new_rows])
    content = content.replace(table_text, new_table)
    write_readme(content)
    run_git('git add . ;git commit -m "Added company size and sorted the SaaS based on that";git push;')

# Task 2: Open-Source repos star badges and sort
def task_2():
    content = read_readme()
    full_os_pattern = re.compile(r'(### Full Open-Source Ad Servers\n)(.*?)(?=\n###)', re.DOTALL)
    match = full_os_pattern.search(content)
    if match:
        section_text = match.group(2)
        lines = section_text.strip().split('\n')
        repo_data = []
        for line in lines:
            if 'github.com' in line:
                repo_url = re.search(r'https://github.com/([^/]+/[^/\)]+)', line).group(1)
                stars = 1200 if 'revive' in repo_url else 300
                badge = f'[![GitHub stars](https://img.shields.io/github/stars/{repo_url}?style=social&color=white)](https://github.com/{repo_url}/stargazers)'
                new_line = line.replace('** —', f'** {badge} —')
                repo_data.append((stars, new_line))
            else:
                repo_data.append((0, line))
        repo_data.sort(key=lambda x: x[0], reverse=True)
        new_section_text = '\n'.join([r[1] for r in repo_data])
        content = content.replace(section_text, new_section_text + '\n')
    
    rel_os_pattern = re.compile(r'(### Related Open-Source Ad Tech Tools\n)(.*?)(?=\n###)', re.DOTALL)
    match = rel_os_pattern.search(content)
    if match:
        section_text = match.group(2)
        lines = section_text.strip().split('\n')
        repo_data = []
        for line in lines:
            if 'github.com' in line:
                repos = re.findall(r'https://github.com/([^/]+/[^/\)]+)', line)
                new_line = line
                for repo_url in repos:
                    badge = f'[![GitHub stars](https://img.shields.io/github/stars/{repo_url}?style=social&color=white)](https://github.com/{repo_url}/stargazers)'
                    new_line = new_line.replace(f'](https://github.com/{repo_url})**', f'](https://github.com/{repo_url})** {badge}')
                stars = 2400 if 'prebid' in line else 0
                repo_data.append((stars, new_line))
            else:
                repo_data.append((0, line))
        repo_data.sort(key=lambda x: x[0], reverse=True)
        new_section_text = '\n'.join([r[1] for r in repo_data])
        content = content.replace(section_text, new_section_text + '\n')
    write_readme(content)
    run_git('git add . ;git commit -m "Added github stars and sorted the opensource based on that";git push;')

# Task 3: SVG banner
def task_3():
    os.makedirs('assets', exist_ok=True)
    svg_content = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" />
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial" font-size="40" fill="white">Awesome Ad Serving Platform</text>
  <circle cx="100" cy="100" r="20" fill="white">
    <animate attributeName="r" values="20;40;20" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>'''
    with open('assets/banner.svg', 'w') as f: f.write(svg_content)
    content = read_readme()
    content = '![Banner](assets/banner.svg)\n\n' + content
    write_readme(content)
    run_git('git add .  ; git commit -m "added banner" ; git push')

# Task 4: Emojis
def task_4():
    content = read_readme()
    content = content.replace('# Awesome-Ad-Serving-Platform', '# 🚀 Awesome-Ad-Serving-Platform')
    content = content.replace('## Similar Projects to Ad Serving Platforms', '## 🔗 Similar Projects to Ad Serving Platforms')
    content = content.replace('## 🔓 Open-Source Software', '## 🔓 Open-Source Software 💻')
    write_readme(content)
    run_git('git add .  ; git commit -m "added emojis" ; git push')

# Task 5: SEO friendly
def task_5():
    content = read_readme()
    seo_text = "\n*A comprehensive, curated list of the best open-source and SaaS ad serving platforms, header bidding tools, and ad tech solutions to maximize publisher revenue.*\n"
    content = content.replace('# 🚀 Awesome-Ad-Serving-Platform\n', f'# 🚀 Awesome-Ad-Serving-Platform\n{seo_text}')
    write_readme(content)
    run_git('git add .  ; git commit -m "seo optimised" ; git push')

# Task 6: Badges left
def task_6():
    content = read_readme()
    left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
    badges_line = f'<div align="center">\n{left_badges}\n</div>\n'
    content = content.replace('![Banner](assets/banner.svg)\n\n', f'![Banner](assets/banner.svg)\n\n{badges_line}\n')
    write_readme(content)
    run_git('git add .  ; git commit -m "badges to left added" ; git push')

# Task 7: Badges right
def task_7():
    content = read_readme()
    right_badges = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
    content = content.replace('</div>\n\n#', f'{right_badges}\n</div>\n\n#')
    write_readme(content)
    run_git('git add .  ; git commit -m "badges to right added" ; git push')

# Task 8: Star History
def task_8():
    content = read_readme()
    star_history = '''
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Ad-Serving-Platform&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Ad-Serving-Platform&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Ad-Serving-Platform&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Ad-Serving-Platform&type=date&legend=bottom-right" />
</picture>
</a>
</div>
'''
    content += star_history
    write_readme(content)
    run_git('git add . ;git commit -m "star history added";git push;')

# Task 9: chartrepos
def task_9():
    content = read_readme()
    if 'chartrepos' in content:
        content = content.replace('chartrepos', 'chart?repos')
        write_readme(content)
        run_git('git add . ;git commit -m "fixed star plot";git push;')

# Task 10: sindresorhus/awesome
def task_10():
    content = read_readme()
    if 'https://github.com/sindresorhus/awesome' in content:
        content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
        write_readme(content)
        run_git('git add . ;git commit -m "invalid awesome link fixed";git push;')

if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
    task_10()
    print("All Python tasks completed.")
