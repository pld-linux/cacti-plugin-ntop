%define		plugin	ntop
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Plugin for Cacti - Provides an iFrame to point to your NTop Server
Summary(pl.UTF-8):	Wtyczka do Cacti - Ntop
Name:		cacti-plugin-ntop
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:%{plugin}-v%{version}-1.tgz
# Source0-md5:	29a192e1f935fbb30c7b9bd5384ff78f
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
BuildRequires:	unzip
Requires:	cacti >= 0.8.7e
Requires:	cacti(pia) >= 2.0
Requires:	php-common >= 4:%{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Provide an iFrame to point to your NTop Server.

%description -l pl.UTF-8
Wtyczka do Cacti - Ntop.

%prep
%setup -qc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
