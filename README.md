# ArchMirror-CLI 📦

**ArchMirror** is a simple CLI utility for Arch Linux that backs up your installed packages into a `.toml` file and allows you to restore them easily on a new system
_(without their configs)_.

---

## A brief guide to using the ArchMirror utility

### 🛠 Installation

1. First, navigate to the project directory using the command:  
  `cd <path_to_folder>`  
  *(replace with your actual directory path)*
  
2. Then, run the installation script:  
  `chmod +x install.sh && ./install.sh`
  

The program is now ready to use! 🚀

---

## 🏷️ Main Functionality

### Create a backup

To make a backup, you need to use a special script:  
`./backup.sh` 💾  
*(The manifest will be saved in `/data`)*

### Restore packages

To install packages from the saved `.toml` config, you need the restore script:  
`./restore.sh -p <path_to_file>` 📥  
*(specify the path to your .toml manifest, e.g., `data/manifest_date.toml`)*

---

#### Support ☕

If you really like the utility, or just want to support the author, you can send me a couple of dollars in cryptocurrency _(link on my GitHub page)_.
