%define		namesrc	ntop
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Ntop 
Summary(pl.UTF-8):	Wtyczka do Cacti - Ntop
Name:		cacti-plugin-ntop
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{namesrc}-%{version}.zip
# Source0-md5:	7e5b07df1db6fc8db73aa16da878e0de
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - Ntop.

%description -l pl.UTF-8
Wtyczka do Cacti - Ntop.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README 
%{webcactipluginroot}
