Summary:	P.I.P.S. - PIPS Is POSIX on Symbian
Summary(pl.UTF-8):	P.I.P.S. - POSIX na Symbianie
Name:		symbian-openc
Version:	1.07
Release:	1
License:	LGPL/BSD/zlib/openssl
Group:		Developement
Source0:	http://www.martin.st/symbian/gnupoc-package-%{version}.tar.gz
# Source0-md5:	4d3f903c3952b028b54e3ff5c657e527
Source1:	s60_openc_plugin_MR.zip
URL:		http://www.forum.nokia.com/main/resources/technologies/open_c/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1
%define		_noautoreq	/c/Perl/bin/perl

%description
Open C SDK Plug-In for S60 3rd Edition SDKs.

%description -l pl.UTF-8
Wtyczka Open C SDK dla SDK S60 3rd Edition.

%prep
%setup -n gnupoc-package-%{version}

%build
mkdir _e
unzip -qn %{SOURCE1} -d _e

cd _e
unzip -qLo Rpipe_3.1.zip

../sdks/lowercase epoc32/release

../sdks/lowercase epoc32/include
../sdks/fixinclude epoc32/include

../sdks/lowercase s60opencex
../sdks/fixinclude s60opencex
../sdks/fixexamples s60opencex

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/symbian/s60v3fp1

cp -r _e/epoc32 $RPM_BUILD_ROOT%{_datadir}/symbian/s60v3fp1
cp -r _e/s60opencdoc $RPM_BUILD_ROOT%{_datadir}/symbian/s60v3fp1
cp -r _e/s60opencex $RPM_BUILD_ROOT%{_datadir}/symbian/s60v3fp1
cp -r _e/s60opencsis $RPM_BUILD_ROOT%{_datadir}/symbian/s60v3fp1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc _e/s60opencreleasenotes.txt _e/Symbian\ Redistribution\ and\ Use\ Licence\ v1.0\ 12.03.07\ final.doc

%{_datadir}/symbian/s60v3fp1/epoc32/include/*
%{_datadir}/symbian/s60v3fp1/epoc32/release/armv5/lib/*
%{_datadir}/symbian/s60v3fp1/epoc32/release/armv5/udeb/*
%{_datadir}/symbian/s60v3fp1/epoc32/release/armv5/urel/*
%{_datadir}/symbian/s60v3fp1/epoc32/release/winscw/udeb/*
%{_datadir}/symbian/s60v3fp1/epoc32/winscw/c/resource/*
%{_datadir}/symbian/s60v3fp1/epoc32/winscw/c/system/data/*

%{_datadir}/symbian/s60v3fp1/s60opencdoc
%{_datadir}/symbian/s60v3fp1/s60opencex
%{_datadir}/symbian/s60v3fp1/s60opencsis
