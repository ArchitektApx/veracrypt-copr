%global _hardened_build 1

%define veracrypt_version 1.26.14
%define wxwidgets_version 3.2.6

Summary:       Open-source utility for on-the-fly encryption
Name:          veracrypt
Epoch:         1
Version:       %(echo %{veracrypt_version} | tr -s '-' '.')
Release:       3%{?dist}
License:       ASL 2.0 and TrueCrypt License 3.0
URL:           https://www.veracrypt.fr/en/Home.html
Source0:       https://www.veracrypt.fr/code/VeraCrypt/snapshot/VeraCrypt-VeraCrypt_%{veracrypt_version}.tar.gz
Source1:       https://github.com/wxWidgets/wxWidgets/releases/download/v%{wxwidgets_version}/wxWidgets-%{wxwidgets_version}.tar.bz2
Patch1:        make-flags.patch

BuildRequires: fuse-devel
BuildRequires: gcc-c++
BuildRequires: gtk2-devel
BuildRequires: make
BuildRequires: pcsc-lite-devel
BuildRequires: pkgconf-pkg-config
BuildRequires: yasm

Requires:      fuse-libs
Requires:      gtk2
Requires:      pcsc-lite-libs
Provides:      veracrypt(bin) = %{epoch}:%{version}-%{release}

%description
VeraCrypt is a free open source disk encryption software for Windows, Mac OSX and Linux. Brought to
you by IDRIX (https://www.idrix.fr) and based on TrueCrypt 7.1a.

%prep
tar -xf '%{SOURCE1}'
%autosetup -p2 -n VeraCrypt-VeraCrypt_%{veracrypt_version}/src

%build
%set_build_flags
%make_build WXSTATIC=1 WX_ROOT=%{_builddir}/wxWidgets-%{wxwidgets_version} wxbuild
%make_build WXSTATIC=1

%install
%make_install

# We manage the installation through the package manager.
rm -f %{buildroot}%{_bindir}/veracrypt-uninstall.sh

%files
%{_bindir}/veracrypt
%{_sbindir}/mount.veracrypt
%{_datadir}/applications/veracrypt.desktop
%{_datadir}/mime/packages/veracrypt.xml
%{_datadir}/pixmaps/veracrypt.xpm
%{_datadir}/veracrypt/languages/Language.*.xml
%license %{_datadir}/doc/veracrypt/License.txt
%doc %{_datadir}/doc/veracrypt/HTML/*

%changelog
* Wed Nov 20 2024 ArchitekApx <architektapx@gehinors.ch> - 1.26.14
- Initial fedora arm64 release