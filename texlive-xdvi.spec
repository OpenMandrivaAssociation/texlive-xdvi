# revision 26689
# category TLCore
# catalog-ctan /dviware/xdvi
# catalog-date 2012-04-01 12:39:29 +0200
# catalog-license other-free
# catalog-version 22.85
Name:		texlive-xdvi
Version:	22.85
Release:	1
Summary:	A DVI previewer for the X Window System
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/xdvi
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xdvi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xdvi.doc.tar.xz
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
%{_texmfdir}/xdvi/XDvi
%{_texmfdir}/xdvi/pixmap/toolbar.xpm
%{_texmfdir}/xdvi/pixmap/toolbar2.xpm
%{_texmfdir}/xdvi/xdvi.cfg
%{_datadir}/X11/app-defaults/*
%doc %{_mandir}/man1/xdvi.1*
%doc %{_texmfdir}/doc/man/man1/xdvi.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
pushd %{buildroot}%{_datadir}/X11/app-defaults
    cp -fpa %{SOURCE2} .
    ln -sf %{_texmfdir}/xdvi/XDvi .
popd
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
