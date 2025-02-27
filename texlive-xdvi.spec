Name:		texlive-xdvi
Version:	62387
Release:	2
Summary:	A DVI previewer for the X Window System
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/dviware/xdvi
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xdvi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xdvi.doc.r%{version}.tar.xz
Source2:	XDvi-color
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-xdvi.bin
%rename tetex-xdvi
%rename xdvik

%description
The canonical previewer for use on Unix and other X-windows
based systems. The distribution has been integrated with that
of xdvik (no longer separately available), so that it will
build with web2c "out of the box". In practice, it is usually
distributed via Tex-live.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/xdvi/config.xdvi
%{_texmfdistdir}/xdvi/XDvi
%{_texmfdistdir}/xdvi/pixmap/toolbar.xpm
%{_texmfdistdir}/xdvi/pixmap/toolbar2.xpm
%{_datadir}/X11/app-defaults/*
%doc %{_mandir}/man1/xdvi.1*
%doc %{_texmfdistdir}/doc/man/man1/xdvi.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
pushd %{buildroot}%{_datadir}/X11/app-defaults
cp -fpa %{SOURCE2} .
ln -sf %{_texmfdistdir}/xdvi/XDvi .
popd
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
