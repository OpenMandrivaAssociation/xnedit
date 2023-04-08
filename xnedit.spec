Summary:		A fast and classic X11 text editor, based on NEdit
Name:			xnedit
Version:		1.4.1
Release:		1
License:		GPLv2
Group:			Editors
URL:			https://github.com/unixwork/xnedit
Source0:		https://github.com/unixwork/xnedit/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:			xnedit-1.4.1-compiler_flags.patch
BuildRequires:	bison
BuildRequires:	motif-devel
BuildRequires:	imagemagick
BuildRequires:	librsvg
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xt)

%description
XNEdit is a multi-purpose text editor for the X Window System, which combines
a standard, easy to use, graphical user interface with the thorough
functionality and stability required by users who edit text eight hours a day.
It provides intensive support for development in a wide variety of languages,
text processors, and other tools, but at the same time can be used productively
by just about anyone who needs to edit text.

XNEdit is a fork of the Nirvana Editor (NEdit) and provides new functionality
like antialiased text rendering and support for unicode.

%files
%license LICENSE
%doc CHANGELOG README.md ReleaseNotes
%{_bindir}/%{name}
%{_bindir}/xnc
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm


#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%before_configure
%make_build linux

%install
%make_install

# icons
rm -f %{buildroot}%{_iconsdir}/%{name}.png
# FIXME: imagemagick produces empty images (maybe
#	a bug in inkskape maybe a bug in image)
#	rsvg-convert works properly for png only
for d in 16 32 48 64 72 96 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
#	rsvg-convert -f png -h ${d} -w ${d} resources/desktop/%{sname}-logo.svg \
#			-o %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
	convert -background none -scale "${d}x${d}" resources/desktop/%{name}.png \
			%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
	convert -background none -scale "${d}x${d}" resources/desktop/%{name}.png \
	%{buildroot}%{_datadir}/pixmaps/%{name}.xpm

