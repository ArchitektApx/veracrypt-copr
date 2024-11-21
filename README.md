# VeraCrypt for aarch64

[![⚡️ Powered By: Copr](https://img.shields.io/badge/⚡️_Powered_by-COPR-blue?style=flat-square)](https://copr.fedorainfracloud.org/)
![📦 Architecture: aarch64](https://img.shields.io/badge/📦_Architecture-aarch64-blue?style=flat-square)
[![Latest Version](https://img.shields.io/badge/dynamic/json?color=blue&label=Version&query=builds.latest.source_package.version&url=https%3A%2F%2Fcopr.fedorainfracloud.org%2Fapi_3%2Fpackage%3Fownername%3Darchitektapx%26projectname%3Dveracrypt%26packagename%3Dveracrypt%26with_latest_build%3DTrue&style=flat-square&logoColor=blue)](https://copr.fedorainfracloud.org/coprs/architektapx/veracrypt/package/veracrypt/)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/architektapx/veracrypt/package/veracrypt/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/architektapx/veracrypt/package/veracrypt/)

Automatically updated spec files and [COPR aarch64/arm64 builds](https://copr.fedorainfracloud.org/coprs/architektapx/veracrypt/) for [VeraCrypt](https://github.com/veracrypt/VeraCrypt) packaged for fedora.

## Issue Contacts
Bugs related to VeraCrypt should be reported directly to the VeraCrypt GitHub repo:
<https://github.com/veracrypt/VeraCrypt/issues>

Bugs related to this package should be reported at this Github project:
<https://github.com/ArchitektApx/veracrypt-copr>

## Installation Instructions
1. Enable `architektapx/veracrypt` [Copr](https://copr.fedorainfracloud.org/coprs/architektapx/veracrypt/) repository according to your package manager.

```Shell
# If you are using dnf... (you need to have 'dnf-plugins-core' installed)
sudo dnf copr enable architektapx/veracrypt
# If you are using yum... (you need to have 'yum-plugins-copr' installed)
sudo yum copr enable architektapx/veracrypt
```

2. (Optional) Update your package list.
```Shell
sudo dnf check-update
```

3. Execute the following command to install the package.
```Shell
sudo dnf install veracrypt
```

4. Launch the application from the Application Menu or execute following command in terminal.
```Shell
veracrypt
```
