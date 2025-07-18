<h2 align="center">
    <img height="200" alt="hdelete" src="images/header-hdelete.png" />
    <br>
    hdelete: pattern-matching file deleter for hidden files
</h2>

---

<div align="center">

<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.6%2B-blue.svg" alt="Python 3.6+ supported"></a>
[![Last Commit](https://img.shields.io/github/last-commit/DChason/hdelete.svg)](https://github.com/DChason/hdelete/commits/main)
[![Issues](https://img.shields.io/github/issues/DChason/hdelete.svg)](https://github.com/DChason/hdelete/issues)
[![GitHub stars](https://img.shields.io/github/stars/DChason/hdelete.svg)](https://github.com/DChason/hdelete/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Follow on LinkedIn](https://img.shields.io/badge/Follow%20me-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/damienchason/)

</div>

**hdelete** was initially created to solve a cross-platform annoyance: deleting hidden files like `Thumbs.db`, `.DS_Store`, and `._*` that sneak onto drives when moving files between Windows, macOS, and Linux without having to  memorizing complex `find` commands - now hdelete gives you a simple and flexible CLI tool to quickly find and delete any files matching your desired patterns.

- Focused on deleting hidden files by default: Thumbs.db, .DS_Store, and ._*
- Pattern matching: add to the default patterns or override and specify your own patterns
- Cross-platform: works on Linux, macOS, and Windows

---

## Installation (Linux or macOS)

**Recommended:**
Clone the repository and copy `hdelete` to a directory in your PATH:

```sh
git clone https://github.com/DChason/hdelete.git
cd hdelete
cp hdelete /usr/local/bin/
chmod +x /usr/local/bin/hdelete
```
<br>

**Alternative:**
Download directly via `wget` or `curl`:

```sh
wget https://raw.githubusercontent.com/DChason/hdelete/main/hdelete -O /usr/local/bin/hdelete
chmod +x /usr/local/bin/hdelete
```

or

```sh
curl -o /usr/local/bin/hdelete https://raw.githubusercontent.com/DChason/hdelete/main/hdelete
chmod +x /usr/local/bin/hdelete
```



---

## Flags & Options

- `-h`, `--help`
    - Show the help message and exit.
- `-d`, `--directory`
    - Specify a directory to run hdelete in (defaults to current directory if `-d` is not given).
- `-a`, `--append`
    - Append one or more patterns to the default list (e.g., `-a '*.log' '*.tmp'`).
- `-A`, `--alternative`
    - Use only these patterns, replacing the default list (e.g., `-A '*.bak' '*~'`).
- `-y`, `--yes`
    - Run in non-interactive mode (auto-accept deletes).

---

## Examples

Delete all default hidden files in the current directory and subdirectories:
```sh
hdelete
```
Delete all default hidden files in the specified directory and subdirectories:
```sh
hdelete -d /tmp
```
Delete all default hidden files and any additional patterns you specify:
```sh
hdelete -a '*.log' '*.tmp'
```

Delete any file matching your specified patterns:
```sh
hdelete -A '*.log'
```

---

## Warnings
- The `-a` and `-A` flag allows adding any patterns, and therefore deleting any file, not just hidden files—**double-check your patterns!**
- hdelete permanently deletes files; there is no "move to trash" or undo.

---

## License

hdelete is licensed under the MIT License. See [LICENSE](LICENSE) for details.
