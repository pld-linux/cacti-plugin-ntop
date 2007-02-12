%define		namesrc	ntop
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Ntop 
Summary(pl.UTF-8):	Wtyczka do Cacti - Ntop
Name:		cacti-plugin-ntop
Version:	0.1b
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#!!!!problem with version
Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:	e83677a70146354787f8382f3c905c90
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
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc 
%{webcactipluginroot}
