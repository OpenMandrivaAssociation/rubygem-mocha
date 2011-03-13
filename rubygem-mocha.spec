# Generated from mocha-0.9.12.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	mocha

Summary:	Mocking and stubbing library
Name:		rubygem-%{rbname}

Version:	0.9.12
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://mocha.rubyforge.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Mocking and stubbing library with JMock/SchMock syntax, which allows
mocking and stubbing of methods on real (non-mock) classes.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(examples|test)/'

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*

