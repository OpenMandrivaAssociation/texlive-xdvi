%global tl_name xdvi
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A DVI previewer for the X Window System
Group:		Publishing
URL:		https://www.ctan.org/pkg/xdvi
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xdvi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xdvi.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(xdvi.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The canonical previewer for use on Unix and other X-windows based
systems. The distribution has been integrated with that of xdvik (no
longer separately available), so that it will build with web2c "out of
the box". It is included in TeX Live.

